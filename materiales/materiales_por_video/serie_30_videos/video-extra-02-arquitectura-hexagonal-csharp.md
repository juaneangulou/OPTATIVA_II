# Video extra 2: Arquitectura hexagonal en C#: separar reglas y herramientas

## Para estudiar por tu cuenta
El video extra anterior organizó Pedidos, Inventario y Entregas en módulos. Ahora vas a proteger una regla dentro de Pedidos para que no dependa directamente de una base de datos, de HTTP o del proveedor de inventario.

Al terminar podrás explicar qué son puerto y adaptador, seguir la dirección de una dependencia e implementar una prueba del caso de uso sin iniciar servicios externos.

## 1. El problema
La regla “no confirmar un pedido si falta inventario” pertenece al negocio. Si queda mezclada en un controlador ASP.NET y usa directamente EF Core, será difícil probarla sin levantar la aplicación y la base de datos.

También será costoso reemplazar el proveedor de inventario, aunque la regla siga siendo la misma.

## 2. Arquitectura hexagonal, en palabras sencillas
La **arquitectura hexagonal** organiza el sistema alrededor de sus reglas y casos de uso. Los detalles externos se conectan en los bordes.

Un **puerto** es una interfaz que expresa una capacidad que el caso de uso necesita. Un **adaptador** implementa esa interfaz con una tecnología concreta.

```text
+----------------------+       +------------------------+
| Caso de uso Pedidos  | ----> | IInventario (puerto)   |
+----------------------+       +-----------^------------+
                                           |
                                +----------+-----------+
                                | Adaptador SQL / HTTP |
                                +----------------------+
```

La regla usa el contrato `IInventario`; el adaptador sabe cómo consultar una base o servicio. La dirección de dependencia apunta hacia la regla, no al proveedor externo.

## 3. El puerto y el caso de uso en C#
```csharp
namespace Logistica.Pedidos;

public interface IInventario
{
    Task<bool> HayUnidadesAsync(
        string productoId,
        int cantidad,
        CancellationToken cancellationToken);
}

public sealed record SolicitudConfirmarPedido(
    Guid PedidoId,
    string ProductoId,
    int Cantidad);

public sealed class ConfirmarPedido
{
    private readonly IInventario _inventario;

    public ConfirmarPedido(IInventario inventario)
    {
        _inventario = inventario;
    }

    public async Task EjecutarAsync(
        SolicitudConfirmarPedido solicitud,
        CancellationToken cancellationToken)
    {
        if (solicitud.PedidoId == Guid.Empty)
            throw new ArgumentException("El identificador es obligatorio.");

        if (solicitud.Cantidad <= 0)
            throw new ArgumentOutOfRangeException(nameof(solicitud.Cantidad));

        var hayUnidades = await _inventario.HayUnidadesAsync(
            solicitud.ProductoId,
            solicitud.Cantidad,
            cancellationToken);

        if (!hayUnidades)
            throw new InvalidOperationException("Inventario insuficiente.");

        // En una aplicación completa, aquí se persiste la confirmación.
    }
}
```

`ConfirmarPedido` conoce una interfaz pequeña y la regla de cantidad. No conoce HTTP, SQL ni la estructura de las tablas.

## 4. Un adaptador de prueba
Para probar el caso sin conectar una base, puedes usar una implementación controlada:

```csharp
public sealed class InventarioFalso(bool hayUnidades) : IInventario
{
    public Task<bool> HayUnidadesAsync(
        string productoId,
        int cantidad,
        CancellationToken cancellationToken) =>
        Task.FromResult(hayUnidades);
}
```

Una prueba puede crear `InventarioFalso(true)` para el caso con existencias y `InventarioFalso(false)` para el rechazo.

En la aplicación real, la configuración conecta la interfaz a un adaptador concreto:

```csharp
builder.Services.AddScoped<IInventario, InventarioSql>();
```

`InventarioSql` es quien consulta la base. Si más adelante Inventario pasa a ser un servicio HTTP, puedes crear otro adaptador sin cambiar la regla de confirmar pedido.

## 5. Qué prueba cada cosa
- La prueba del caso de uso comprueba que cantidad inválida o stock insuficiente no confirma el pedido.
- La prueba del adaptador comprueba que la consulta a la fuente de datos se realiza correctamente.
- La prueba de integración comprueba que la configuración real conecta las partes esperadas.

No uses un doble de prueba para afirmar que SQL funciona: el doble verifica el comportamiento del caso de uso, no la consulta a la base real.

## 6. Errores comunes
- Crear interfaces para cada clase aunque no exista una frontera útil.
- Poner lógica de negocio dentro del controlador porque “ya tengo la solicitud ahí”.
- Hacer que el dominio referencie directamente EF Core para una regla sencilla.
- Usar un objeto falso en todas las pruebas y nunca probar la integración real.
- Convertir un puerto en un contrato gigantesco que expone todas las operaciones del proveedor.

## 7. Actividad de autoestudio
Agrega el caso “no hay existencias suficientes”.

1. Escribe qué recibe el caso de uso.
2. Escribe qué método del puerto necesita.
3. Crea un adaptador de prueba que devuelva falta de inventario.
4. Define el resultado esperado.
5. Indica qué prueba adicional necesitarías para validar el adaptador SQL.
6. Explica qué cambia si el proveedor de inventario se reemplaza por una API HTTP.

### Respuesta modelo
El caso recibe identificador de pedido, producto y cantidad; consulta `IInventario`; el adaptador de prueba devuelve `false`; el caso de uso rechaza la confirmación. Una prueba de integración debe comprobar el adaptador SQL contra una base de ensayo. Si cambia el proveedor, cambia el adaptador, no la regla central.

## Comprueba lo que aprendiste
1. ¿Qué representa el puerto `IInventario`?
2. ¿Qué responsabilidad tiene el adaptador?
3. ¿Por qué un caso de uso no debería conocer SQL?
4. ¿Qué no demuestra una prueba con `InventarioFalso`?

### Respuestas
1. La capacidad de consultar disponibilidad que necesita el caso de uso.
2. Traducir esa capacidad a una herramienta concreta.
3. Para que la regla no dependa del proveedor y pueda probarse sin infraestructura.
4. No demuestra que la consulta SQL real funcione; para eso se necesita una prueba de integración.

## Cierre
La arquitectura hexagonal protege reglas y casos de uso de los detalles externos mediante puertos y adaptadores. Crea las interfaces que expresan fronteras reales y prueba cada frontera con el nivel adecuado.
