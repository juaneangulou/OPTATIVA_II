# Video extra 4: CQRS en C#: escribir pedidos y leer el tablero logístico

## Para estudiar por tu cuenta
La pantalla operativa necesita registrar cambios y, al mismo tiempo, mostrar pedidos ordenados por estado, zona y hora. En este capítulo aprenderás a separar el modelo que cambia información del modelo que la consulta.

Al terminar podrás describir CQRS, construir un comando y una consulta sencillos y reconocer cuándo la separación añade complejidad innecesaria.

## 1. El problema: escribir y consultar no son la misma tarea
Un **comando** solicita un cambio: crear, confirmar o cancelar un pedido. Tiene efectos y debe validar reglas.

Una **consulta** pide información sin cambiarla: mostrar pedidos pendientes de una zona. No debería modificar el estado del sistema.

En una aplicación pequeña, ambas tareas pueden usar la misma base de datos y las mismas entidades. Sin embargo, sus necesidades son distintas: registrar un pedido protege reglas; la pantalla puede necesitar una proyección preparada para mostrar datos.

## 2. ¿Qué significa CQRS?
CQRS significa **Command Query Responsibility Segregation**: separar la responsabilidad de los comandos y las consultas.

La separación mínima es conceptual y de código:

```text
Comando: entrada -> validar regla -> cambiar y guardar
Consulta: filtros -> leer datos -> formar respuesta
```

CQRS por sí solo **no exige** dos bases de datos, mensajería ni microservicios. Esas decisiones tienen costos y se agregan solo si los requisitos lo justifican.

## 3. Un comando de negocio
```csharp
public sealed record ConfirmarPedidoCommand(Guid PedidoId);

public sealed class ConfirmarPedidoHandler
{
    private readonly IPedidosRepository _pedidos;

    public ConfirmarPedidoHandler(IPedidosRepository pedidos)
    {
        _pedidos = pedidos;
    }

    public async Task EjecutarAsync(
        ConfirmarPedidoCommand command,
        CancellationToken cancellationToken)
    {
        var pedido = await _pedidos.BuscarAsync(
            command.PedidoId,
            cancellationToken);

        if (pedido is null)
            throw new InvalidOperationException("El pedido no existe.");

        pedido.Confirmar();
        await _pedidos.GuardarAsync(cancellationToken);
    }
}
```

El comando expresa intención. El manejador aplica la regla a la entidad y guarda el cambio. No debe aceptar del cliente un estado arbitrario como “Confirmado” si confirmar exige condiciones.

## 4. Una consulta que devuelve una proyección
```csharp
public sealed record PedidoPendienteDto(
    Guid Id,
    string Zona,
    DateTimeOffset CreadoEn,
    int CantidadLineas);

public sealed class ListarPendientesHandler
{
    private readonly LogisticaDbContext _db;

    public ListarPendientesHandler(LogisticaDbContext db)
    {
        _db = db;
    }

    public Task<List<PedidoPendienteDto>> EjecutarAsync(
        string zona,
        CancellationToken cancellationToken) =>
        _db.Pedidos
            .AsNoTracking()
            .Where(pedido => pedido.Estado == "Pendiente"
                && pedido.Zona == zona)
            .OrderBy(pedido => pedido.CreadoEn)
            .Select(pedido => new PedidoPendienteDto(
                pedido.Id,
                pedido.Zona,
                pedido.CreadoEn,
                pedido.Lineas.Count))
            .ToListAsync(cancellationToken);
}
```

La consulta devuelve solo lo que necesita la pantalla. `AsNoTracking` comunica que la consulta no pretende cambiar las entidades rastreadas por EF Core. Comprueba que los tipos y propiedades coincidan con tu modelo real; este fragmento ilustra el patrón.

## 5. Lectura eventualmente consistente
En el diseño inicial, comando y consulta pueden leer la misma base y reflejar el cambio inmediatamente después de guardar.

En sistemas de alto volumen, se puede mantener una vista de lectura separada. Si esa vista se actualiza después del comando, puede tardar un poco: ese intervalo se llama **consistencia eventual**. La pantalla debe tolerar o explicar que el cambio quizá no aparezca de inmediato.

Separar almacenamiento también obliga a resolver sincronización, reintentos, reconstrucción de la vista y errores parciales. No es una optimización gratuita.

## 6. Cuándo usar CQRS
Puede ayudar cuando:

- las reglas de escritura y las consultas tienen formas muy diferentes;
- las consultas necesitan proyecciones específicas;
- varios flujos de escritura deben ser claros y comprobables;
- puedes asumir la complejidad adicional de mantener vistas de lectura.

En un CRUD pequeño con las mismas necesidades de escritura y lectura, separar handlers sin beneficio puede añadir archivos y conceptos sin mejorar el diseño.

## 7. Actividad de autoestudio
Diseña el flujo para cancelar un pedido.

1. Escribe un comando con los datos mínimos.
2. Indica qué regla debería validar la entidad.
3. Decide qué información consultaría una pantalla de pedidos cancelados.
4. Propón una proyección para esa pantalla.
5. Explica si necesitas una base de lectura separada y qué costo introduciría.

### Respuesta modelo
El comando necesita el identificador y, si el negocio lo exige, un motivo. La entidad debe rechazar cancelar un pedido ya entregado. La consulta podría devolver identificador, fecha, motivo y zona mediante un DTO. Una base de lectura separada solo se justificaría si las consultas o la escala lo necesitan; añadiría sincronización y posibles retrasos.

## Comprueba lo que aprendiste
1. ¿Una consulta CQRS debería cambiar datos?
2. ¿CQRS obliga a usar dos bases de datos?
3. ¿Qué riesgo aparece con una vista de lectura asíncrona?
4. ¿Por qué devolver un DTO de consulta puede ser útil?

### Respuestas
1. No; su responsabilidad es leer.
2. No; la separación puede ser solo de responsabilidades en código.
3. La vista puede quedar temporalmente desactualizada.
4. Devuelve solo los campos que necesita el consumidor y evita exponer detalles internos.

## Cierre
Separa comandos y consultas cuando esa distinción haga más claras las reglas o resuelva necesidades reales de lectura. Empieza con una separación lógica; usa bases independientes solo cuando puedas asumir sus costos.
