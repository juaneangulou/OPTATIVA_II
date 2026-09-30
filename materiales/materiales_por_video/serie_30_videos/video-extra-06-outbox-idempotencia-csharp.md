# Video extra 6: Transactional Outbox e idempotencia en C#

## Para estudiar por tu cuenta
Cuando se confirma un pedido, otra parte del sistema debe iniciar la preparación. Guardar el pedido y publicar un mensaje son dos operaciones distintas. Si una ocurre y la otra falla, pueden quedar datos incoherentes.

En este capítulo aprenderás a guardar un evento pendiente junto con el cambio de negocio y a procesarlo de forma segura ante reintentos.

## 1. La falla de las dos escrituras
Supón que el sistema hace lo siguiente:

1. Guarda el pedido en la base de datos.
2. Publica `PedidoConfirmado` en una cola.

Si se guarda el pedido y la aplicación se cae antes de publicar, la preparación nunca recibe el evento. Si publica primero y falla el guardado, otro componente puede preparar un pedido que no existe.

Una transacción de base de datos no incluye automáticamente una cola externa.

## 2. Transactional Outbox
Una **outbox transaccional** es una tabla de mensajes pendientes en la misma base de datos que el cambio de negocio.

En una transacción se guardan:

- el pedido confirmado;
- un registro `PedidoConfirmado` en la tabla outbox.

Así ambos cambios se confirman juntos. Un proceso posterior lee la outbox y publica el mensaje en el broker. **Broker** significa el sistema que recibe, conserva y entrega mensajes a otros componentes.

```text
Una transacción local:
  actualizar Pedido
  insertar OutboxMessage

Un worker posterior:
  leer mensaje pendiente
  publicar en cola
  marcar como enviado
```

## 3. Modelo simplificado del mensaje
```csharp
public sealed class OutboxMessage
{
    public Guid Id { get; set; }
    public string Type { get; set; } = "";
    public string Payload { get; set; } = "";
    public DateTimeOffset CreatedAt { get; set; }
    public DateTimeOffset? PublishedAt { get; set; }
}
```

Al confirmar el pedido, la aplicación agrega el mensaje al mismo `DbContext` antes de llamar a `SaveChangesAsync`:

```csharp
pedido.Confirmar();

_db.OutboxMessages.Add(new OutboxMessage
{
    Id = Guid.NewGuid(),
    Type = "PedidoConfirmado",
    Payload = JsonSerializer.Serialize(new
    {
        pedido.Id,
        pedido.ClienteId
    }),
    CreatedAt = DateTimeOffset.UtcNow
});

await _db.SaveChangesAsync(cancellationToken);
```

Configura y prueba la transacción según el proveedor de base de datos. El mensaje debe contener los datos necesarios para su propósito, no una copia indiscriminada de toda la entidad.

## 4. Publicar el mensaje no es “exactamente una vez”
Un worker puede publicar el mensaje y caerse antes de marcarlo como publicado. Al reiniciarse, puede publicarlo de nuevo.

Por eso, la entrega de mensajes suele diseñarse como **al menos una vez**: puede haber duplicados. En lugar de prometer que nunca se repetirá, el consumidor se protege contra repeticiones.

Una operación **idempotente** produce el mismo efecto aunque se ejecute más de una vez con la misma solicitud. Por ejemplo, procesar dos veces el evento con el mismo `MessageId` no debe descontar el inventario dos veces.

## 5. Registrar mensajes procesados
El consumidor puede guardar los identificadores procesados en una tabla con una restricción única:

```text
ProcessedMessages
  MessageId (único)
  ProcessedAt
```

Dentro de una transacción local, comprueba o inserta el `MessageId` y aplica el efecto. Si ya existe, reconoce que el mensaje fue atendido y no repite el cambio.

La comprobación y el efecto deben protegerse frente a dos entregas simultáneas. Una restricción única de base de datos ayuda a resolver la carrera; no dependas solo de “consultar y luego insertar” sin control de concurrencia.

## 6. Operación del worker
Un worker real también necesita:

- procesar lotes pequeños y limitar concurrencia;
- reintentar errores transitorios con espera;
- registrar intentos y última falla;
- mover mensajes problemáticos a un estado revisable;
- alertar si la cola pendiente crece;
- evitar mantener filas bloqueadas mientras espera una llamada de red.

El diseño exacto depende del motor, broker y volumen. El fragmento describe la secuencia, no una implementación completa de concurrencia.

## 7. Actividad de autoestudio
Diseña el evento `EntregaAsignada`.

1. ¿Qué datos mínimos necesita el consumidor?
2. ¿Qué dos escrituras deben quedar en una transacción local?
3. ¿Qué sucede si el worker publica y se cae antes de marcar el mensaje?
4. ¿Cómo evita el consumidor asignar dos veces la misma entrega?
5. Nombra una métrica que ayude a detectar problemas.

### Respuesta modelo
El consumidor puede necesitar identificador de entrega, pedido y repartidor. La asignación de entrega y el mensaje outbox se guardan juntos. Si el worker cae después de publicar, puede repetirlo; el consumidor registra el identificador del mensaje con unicidad y no vuelve a aplicar el efecto. Una métrica útil es la edad del mensaje pendiente más antiguo o la cantidad acumulada de mensajes.

## Comprueba lo que aprendiste
1. ¿Qué inconsistencia evita la outbox?
2. ¿Por qué el consumidor debe tolerar duplicados?
3. ¿Qué hace idempotente una operación?
4. ¿Por qué el identificador del mensaje debe ser estable?

### Respuestas
1. Que el cambio local se guarde sin que el evento correspondiente quede registrado para publicar, o al revés.
2. Porque el worker puede repetir una publicación después de una falla.
3. Que repetir la misma solicitud no vuelva a aplicar el efecto.
4. Permite reconocer que dos entregas representan el mismo evento lógico.

## Cierre
La outbox hace atómica la escritura del negocio y el registro del mensaje pendiente, no la publicación externa. Diseña el resto del flujo asumiendo reintentos y duplicados; esa suposición es más realista y verificable.
