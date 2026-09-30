# Video extra 3: Repositorios con EF Core en C#: cuándo abstraer el acceso a datos

## Para estudiar por tu cuenta
El pedido debe guardarse para que el sistema lo recuerde después de un reinicio. En este capítulo aprenderás qué aporta EF Core, qué es un repositorio y por qué no hace falta envolver cada operación con capas adicionales.

Al terminar podrás seguir un pedido desde una solicitud hasta la base de datos y explicar qué comprobarías con una prueba de integración.

## 1. Persistir significa conservar
**Persistir** significa guardar información para poder recuperarla después. Una base de datos relacional organiza información en tablas, filas y columnas. EF Core es un ORM: traduce operaciones sobre objetos C# a consultas y cambios en una base de datos.

Un **DbContext** representa una sesión de trabajo con la base de datos. EF Core registra qué entidades se añadieron o cambiaron y `SaveChangesAsync` envía esos cambios.

## 2. Modelo de pedido
```csharp
public sealed class Pedido
{
    public Guid Id { get; private set; }
    public Guid ClienteId { get; private set; }
    public string Estado { get; private set; } = "Pendiente";

    private Pedido() { } // EF Core puede usar este constructor.

    public Pedido(Guid id, Guid clienteId)
    {
        if (id == Guid.Empty)
            throw new ArgumentException("El pedido necesita identificador.");
        if (clienteId == Guid.Empty)
            throw new ArgumentException("El pedido necesita un cliente.");

        Id = id;
        ClienteId = clienteId;
    }

    public void Confirmar()
    {
        if (Estado != "Pendiente")
            throw new InvalidOperationException(
                "Solo se puede confirmar un pedido pendiente.");

        Estado = "Confirmado";
    }
}
```

Los setters privados hacen que el cambio de estado pase por una operación que valida la regla. En un proyecto real conviene representar estados con tipos o valores controlados si eso hace más segura la lógica.

## 3. ¿Qué hace el patrón Repository?
Un **repositorio** representa una colección de objetos del negocio y ofrece operaciones como buscar, agregar o guardar. Su objetivo es que el caso de uso trabaje con una intención del dominio, no con detalles de consulta.

```csharp
public interface IPedidosRepository
{
    Task<Pedido?> BuscarAsync(
        Guid id,
        CancellationToken cancellationToken);

    void Agregar(Pedido pedido);
    Task GuardarAsync(CancellationToken cancellationToken);
}
```

Una implementación con EF Core puede ser:

```csharp
public sealed class PedidosRepository : IPedidosRepository
{
    private readonly LogisticaDbContext _db;

    public PedidosRepository(LogisticaDbContext db)
    {
        _db = db;
    }

    public Task<Pedido?> BuscarAsync(
        Guid id,
        CancellationToken cancellationToken) =>
        _db.Pedidos.SingleOrDefaultAsync(
            pedido => pedido.Id == id,
            cancellationToken);

    public void Agregar(Pedido pedido) => _db.Pedidos.Add(pedido);

    public Task GuardarAsync(CancellationToken cancellationToken) =>
        _db.SaveChangesAsync(cancellationToken);
}
```

La configuración depende de cómo esté estructurado el proyecto. El ejemplo muestra la separación, no un archivo completo de arranque.

## 4. EF Core ya aporta comportamientos de repositorio
`DbSet<T>` permite consultar y agregar entidades; `DbContext` rastrea cambios y guarda el trabajo. Por eso EF Core ya ofrece ideas similares a Repository y Unit of Work.

Crear un repositorio propio puede aportar valor si:

- define operaciones del negocio con nombres claros;
- protege una frontera que quieres cambiar o probar;
- limita consultas complejas a una parte del sistema.

Puede ser una capa innecesaria si solo reenvía cada método de `DbSet` sin proteger una regla ni simplificar una prueba. El patrón no debe añadirse solo porque aparece en un diagrama.

## 5. Transacción: varios cambios que deben quedar juntos
Una **transacción** agrupa cambios para que se confirmen todos o ninguno, según las capacidades de la base de datos.

Crear un pedido puede insertar el pedido y sus líneas. Si se guarda el pedido pero no las líneas, la información queda incompleta. EF Core ejecuta los cambios de un `SaveChangesAsync` relacional dentro de una transacción en condiciones habituales; confirma la configuración concreta de tu proveedor.

No mantengas una transacción abierta mientras llamas a una API externa lenta: ocupa recursos y no hace que dos sistemas independientes compartan una transacción segura.

## 6. API DTO y entidad persistida son cosas distintas
Una **entidad** representa información de dominio o persistencia. Un **DTO** (objeto de transferencia) define lo que se recibe o devuelve por una API.

No devuelvas la entidad de EF directamente sin revisar sus campos. Puede exponer identificadores internos o propiedades que el cliente no necesita. Crea una respuesta explícita:

```csharp
public sealed record ResumenPedidoResponse(
    Guid Id,
    string Estado);
```

## 7. Actividad de autoestudio
Diseña cómo guardar un pedido con dos líneas de producto.

1. Identifica qué datos corresponden a pedido y cuáles a línea.
2. Explica qué ocurre si falla el guardado de una línea.
3. Decide si necesitas un repositorio propio; menciona el motivo.
4. Escribe qué campos puede recibir el cliente y cuáles debería devolver la API.
5. Define una prueba que guarde y vuelva a consultar el pedido en una base de ensayo.

### Respuesta modelo
El pedido conserva identificador y cliente; cada línea conserva producto y cantidad. Si ambas inserciones forman una operación de negocio, deben confirmarse juntas o rechazarse juntas. Un repositorio propio tiene sentido si representa operaciones del dominio; si solo reenvía `DbSet`, EF Core puede bastar.

La API puede recibir productos y cantidades, pero no confiar en que el cliente decida el estado final. La respuesta puede incluir identificador y estado, sin exponer navegaciones internas. La prueba de integración inserta el pedido, consulta de nuevo sus líneas y verifica que ambas existan.

## Comprueba lo que aprendiste
1. ¿Qué significa persistir?
2. ¿Qué aporta un repositorio que no aporta un `DbSet` por sí solo?
3. ¿Por qué no conviene llamar a una API externa dentro de una transacción de base de datos?
4. ¿Qué diferencia hay entre entidad y DTO?

### Respuestas
1. Guardar información para recuperarla posteriormente.
2. Puede ofrecer operaciones del dominio y proteger una frontera si se diseña con propósito.
3. La llamada puede tardar y mantener recursos bloqueados; además, las dos partes no forman automáticamente una transacción única.
4. La entidad modela información interna; el DTO define lo que cruza la API.

## Cierre
EF Core ayuda a consultar y guardar datos, y sus abstracciones ya cubren varias necesidades comunes. Usa un repositorio adicional solo si aporta una frontera, una prueba o una operación de negocio más clara.
