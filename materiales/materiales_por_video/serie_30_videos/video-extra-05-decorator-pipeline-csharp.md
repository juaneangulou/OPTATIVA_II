# Video extra 5: Decorator y pipeline en C#: añadir capacidades sin ensuciar el caso de uso

## Para estudiar por tu cuenta
Al consultar una entrega, puede ser necesario medir el tiempo, registrar fallas o comprobar autorización. Si cada caso de uso copia la misma lógica, corregirla se vuelve tedioso y los comportamientos empiezan a diferir.

En este capítulo aprenderás el patrón Decorator y cómo una cadena de comportamientos puede rodear una operación sin reemplazar su regla principal.

## 1. Un comportamiento que cruza varios casos
Un comportamiento transversal aparece en distintas operaciones. Ejemplos: registrar duración, aplicar autorización, validar una solicitud o escribir un registro de auditoría.

Un **decorador** implementa la misma interfaz que el objeto decorado. Recibe ese objeto y agrega un comportamiento antes o después de delegar la operación.

```text
Controlador -> Decorador de medición -> Caso de uso -> Repositorio
```

El decorador no debería apropiarse de la regla de negocio que pertenece al caso de uso.

## 2. Contrato del caso de uso
```csharp
public sealed record ConsultarEntregaQuery(Guid EntregaId);
public sealed record EntregaDto(Guid Id, string Estado);

public interface IConsultarEntrega
{
    Task<EntregaDto?> EjecutarAsync(
        ConsultarEntregaQuery query,
        CancellationToken cancellationToken);
}
```

La interfaz define una operación que puede ser implementada por el caso de uso y por sus decoradores.

## 3. Implementación principal
```csharp
public sealed class ConsultarEntrega : IConsultarEntrega
{
    private readonly IEntregasRepository _entregas;

    public ConsultarEntrega(IEntregasRepository entregas)
    {
        _entregas = entregas;
    }

    public async Task<EntregaDto?> EjecutarAsync(
        ConsultarEntregaQuery query,
        CancellationToken cancellationToken)
    {
        var entrega = await _entregas.BuscarAsync(
            query.EntregaId,
            cancellationToken);

        return entrega is null
            ? null
            : new EntregaDto(entrega.Id, entrega.Estado);
    }
}
```

Esta clase resuelve la consulta. Mantenerla enfocada facilita entender qué ocurre con una solicitud válida.

## 4. Decorador de medición
```csharp
public sealed class MedirConsultaEntrega : IConsultarEntrega
{
    private readonly IConsultarEntrega _siguiente;
    private readonly ILogger<MedirConsultaEntrega> _logger;

    public MedirConsultaEntrega(
        IConsultarEntrega siguiente,
        ILogger<MedirConsultaEntrega> logger)
    {
        _siguiente = siguiente;
        _logger = logger;
    }

    public async Task<EntregaDto?> EjecutarAsync(
        ConsultarEntregaQuery query,
        CancellationToken cancellationToken)
    {
        var inicio = Stopwatch.GetTimestamp();
        try
        {
            return await _siguiente.EjecutarAsync(query, cancellationToken);
        }
        finally
        {
            var duracion = Stopwatch.GetElapsedTime(inicio);
            _logger.LogInformation(
                "ConsultarEntrega terminó en {DuracionMs} ms",
                duracion.TotalMilliseconds);
        }
    }
}
```

El decorador delega la consulta y registra la duración incluso si la operación falla, porque el bloque `finally` siempre se ejecuta. En código real importa no registrar datos personales o secretos.

## 5. Pipeline: una cadena de comportamientos
Un **pipeline** encadena varios comportamientos alrededor de un manejador. Por ejemplo:

```text
Validar -> Autorizar -> Medir -> Manejador
```

Cada paso puede continuar, rechazar o transformar la operación según el contrato. Las bibliotecas de mediación suelen ofrecer pipelines listos, pero primero entiende el flujo y revisa cómo registra y ordena los comportamientos la biblioteca elegida.

El orden importa. Si autorización se ejecuta después del manejador, llega demasiado tarde. Si el registro de medición debe incluir fallas de validación, debe envolver también la validación.

## 6. No todo debe ser un decorador
- **Regla de negocio:** pertenece al dominio o caso de uso, por ejemplo impedir una transición inválida.
- **Comportamiento transversal:** puede ser candidato a decorador, por ejemplo medición común.
- **Detalle de infraestructura:** puede pertenecer al adaptador, por ejemplo abrir una conexión.

No escondas una regla central detrás de una cadena larga y difícil de rastrear. Un desarrollador debe poder descubrir el orden efectivo de ejecución.

## 7. Actividad de autoestudio
Agrega un decorador que rechace la consulta si el identificador está vacío y delegue los demás casos.

1. ¿Qué interfaz debe implementar?
2. ¿En qué momento debe llamar a `_siguiente`?
3. ¿Qué prueba demuestra que la consulta inválida no llegó al manejador?
4. ¿Por qué no conviene agregar una política de negocio solo para evitar modificar la clase principal?

### Respuesta modelo
Implementa `IConsultarEntrega`. Antes de delegar, comprueba `Guid.Empty` y rechaza. Una prueba usa un manejador falso que registra si fue invocado; con un identificador vacío, verifica que no se llamó. Una regla de negocio debe permanecer visible en el dominio/caso de uso, no ocultarse como infraestructura transversal.

## Comprueba lo que aprendiste
1. ¿Qué interfaz comparte un decorador con el objeto que envuelve?
2. ¿Qué aporta `finally` en el ejemplo?
3. ¿Por qué importa el orden de un pipeline?
4. ¿Qué dato sensible debes evitar escribir en logs?

### Respuestas
1. La misma interfaz pública de la operación.
2. Permite medir también cuando la operación lanza una excepción.
3. Porque un comportamiento como la autorización debe ejecutarse antes del manejador.
4. Contraseñas, tokens, datos personales u otra información que no sea necesaria.

## Cierre
Decorator permite añadir comportamientos alrededor de una operación sin duplicarlos en cada caso de uso. Conserva el flujo visible, limita el número de capas y deja las reglas de negocio en un lugar comprensible.
