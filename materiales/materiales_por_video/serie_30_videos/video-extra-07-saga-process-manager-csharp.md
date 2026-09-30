# Video extra 7: Saga y Process Manager en C# para coordinar una entrega

## Para estudiar por tu cuenta
Crear una entrega puede requerir reservar inventario, asignar un repartidor y notificar al cliente. Si cada capacidad está en un servicio con su propia base, una transacción SQL local no puede deshacer automáticamente los cambios de todos.

En este capítulo aprenderás a modelar una operación distribuida como pasos, respuestas y acciones compensatorias.

## 1. Por qué una transacción local no alcanza
Una transacción de base de datos controla cambios dentro de un límite administrado por esa base. No puede, por sí sola, bloquear tres servicios HTTP y garantizar que todos confirmen juntos.

Si el inventario reserva unidades pero no se encuentra repartidor, el flujo necesita decidir qué hacer con la reserva. Ese comportamiento debe diseñarse explícitamente.

## 2. Saga y Process Manager
Una **Saga** coordina una operación de negocio larga que atraviesa varias transacciones locales. Si un paso posterior falla, puede ejecutar acciones compensatorias para aproximar una reversión.

Un **Process Manager** guarda el estado del flujo y decide cuál es el siguiente paso cuando llegan eventos o respuestas. Ambos términos están relacionados; según la arquitectura, el coordinador puede iniciar comandos directamente o reaccionar a mensajes.

Ejemplo de flujo:

```text
Pedido confirmado
  -> reservar inventario
  -> asignar repartidor
  -> crear entrega
  -> notificar cliente
```

Si la asignación falla después de reservar:

```text
asignación rechazada
  -> liberar reserva
  -> marcar pedido como pendiente de asignación
  -> informar el resultado
```

## 3. Una máquina de estados explícita
```csharp
public enum EstadoPreparacion
{
    Iniciada,
    InventarioReservado,
    RepartidorAsignado,
    Completada,
    Compensando,
    Fallida
}

public sealed class PreparacionEntrega
{
    public Guid Id { get; init; }
    public Guid PedidoId { get; init; }
    public EstadoPreparacion Estado { get; private set; }

    public void MarcarInventarioReservado()
    {
        if (Estado != EstadoPreparacion.Iniciada)
            throw new InvalidOperationException("Paso fuera de orden.");

        Estado = EstadoPreparacion.InventarioReservado;
    }

    public void MarcarRepartidorAsignado()
    {
        if (Estado != EstadoPreparacion.InventarioReservado)
            throw new InvalidOperationException("Primero reserva inventario.");

        Estado = EstadoPreparacion.RepartidorAsignado;
    }
}
```

El objeto ilustra transiciones válidas. Un Process Manager persistido también debe guardar identificadores de correlación, intentos, fechas y fallas necesarias para reanudar el flujo.

## 4. Compensar no siempre significa borrar
Una compensación es una acción de negocio que corrige el efecto anterior cuando es posible. Liberar una reserva puede compensar reservar inventario; no necesariamente borra el historial.

Algunas acciones no se pueden revertir exactamente. Un SMS enviado no se puede “desenviar”; se puede emitir una notificación correctiva. Por eso, cada paso debe definir qué significa compensarlo.

Las compensaciones también pueden fallar. El coordinador debe poder reintentarlas, registrar el estado y alertar para intervención cuando sea necesario.

## 5. Datos y mensajes
Cada mensaje debe incluir un identificador de flujo, por ejemplo `PreparacionId`, para relacionar las respuestas con la operación correcta. Los consumidores deben tolerar mensajes duplicados y eventos fuera de orden.

No asumas que los mensajes llegan exactamente una vez ni en el orden ideal. Persiste el estado del Process Manager para que un reinicio no pierda el progreso.

## 6. Cuándo usarlo
Una Saga es adecuada para flujos que duran más que una transacción local o cruzan servicios autónomos. Si todas las operaciones están en una base y pueden ejecutarse dentro de una transacción breve, una Saga puede complicar innecesariamente el caso.

También evita convertir cada secuencia de dos métodos en una máquina distribuida. El patrón exige monitoreo, tratamiento de mensajes repetidos, compensaciones y estados operativos.

## 7. Actividad de autoestudio
La reserva funciona, pero el servicio de repartidores no responde.

1. ¿Qué estado debe conservar el coordinador?
2. ¿Debe liberar inventario inmediatamente o puede reintentar asignación?
3. ¿Qué datos necesita para recibir una respuesta tardía?
4. ¿Qué ocurre si la respuesta de asignación llega dos veces?
5. Define una compensación para una notificación ya enviada.

### Respuesta modelo
El estado debe mostrar que el inventario está reservado y que la asignación sigue pendiente o en reintento. La decisión entre esperar y liberar depende del tiempo de reserva y las reglas del negocio. El identificador del flujo y del pedido permiten correlacionar la respuesta. La segunda respuesta no debe crear otra entrega: se reconoce mediante idempotencia y estado actual. Una notificación ya enviada puede compensarse enviando un mensaje correctivo, no borrando el hecho.

## Comprueba lo que aprendiste
1. ¿Qué coordina una Saga?
2. ¿Qué es una compensación?
3. ¿Por qué no se puede prometer un rollback perfecto entre servicios?
4. ¿Qué debe persistir el Process Manager?

### Respuestas
1. Pasos de negocio que ocurren en transacciones locales diferentes.
2. Una acción que corrige el efecto anterior cuando la operación completa falla.
3. Porque algunos efectos externos no se pueden deshacer y cada servicio confirma por separado.
4. El estado del flujo y los datos necesarios para continuar, correlacionar y reintentar.

## Cierre
La Saga hace explícita la coordinación distribuida y las respuestas a fallas parciales. Diseña primero estados, compensaciones y reintentos; luego elige cómo transportar los mensajes.
