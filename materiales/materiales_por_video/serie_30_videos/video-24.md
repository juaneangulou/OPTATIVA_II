# Video 24: Mensajes, eventos y productor-consumidor

## Fuentes de este video
- [Mensajes vs eventos en microservicios](https://platzi.com/cursos/software-avanzado/mensajes-vs-eventos-en-microservicios/)
- [Patrón productor-consumidor y fan-in/fan-out](https://platzi.com/cursos/software-avanzado/patron-productor-consumidor-vs-fan-in-y/)

## Navegación
[⬅️ Video anterior: Bounded Context e infraestructura como código](video-23.md) | [📚 Índice de la serie](README.md) | [➡️ Video siguiente: Dead Letter Queue y consumidores en tiempo real](video-25.md)

## Para estudiar por tu cuenta
Pedidos, Inventario, Entregas y Notificaciones necesitan coordinarse sin esperar siempre una llamada inmediata entre ellos. Para entender esa comunicación, primero distingue si una parte pide una acción o anuncia un hecho que ya ocurrió. Después sigue quién crea y quién procesa el trabajo.

## 1. Qué es un mensaje
Un **mensaje** es información que un componente envía a otro. La palabra describe el transporte; el contenido puede tener intenciones diferentes.

Hay dos intenciones comunes:

- **Comando:** pide a un destinatario que haga algo. Ejemplo: “Reserva dos unidades para el pedido 245”.
- **Evento:** comunica un hecho que ya ocurrió. Ejemplo: “El pedido 245 fue confirmado”.

La diferencia importa. Si un comando falla, alguien puede necesitar un resultado. Un evento informa un hecho; los componentes interesados deciden qué hacer con él.

## 2. Una comparación cotidiana
“Cierra la puerta” es una instrucción: pide una acción que aún no se hizo.

“La puerta quedó cerrada” es un evento: informa un hecho terminado.

En software, `ReservarInventario` es una petición; `InventarioReservado` solo debe publicarse después de que la reserva ocurra realmente.

## 3. Productor y consumidor
Un **productor** crea una tarea o mensaje. Un **consumidor** lo recibe y realiza un trabajo.

En el ejemplo logístico:

- Pedidos produce una tarea de preparación.
- Entregas consume esa tarea y prepara una ruta.

Una **cola** conserva trabajo pendiente entre el productor y el consumidor:

```text
Pedidos (productor) -> Cola de entregas -> Entregas (consumidor)
```

La cola permite que Pedidos termine su trabajo sin esperar a que Entregas esté libre. No garantiza que la tarea se complete: el sistema también debe manejar retrasos, errores y reintentos.

## 4. El pedido 245 paso a paso

### Paso 1: el pedido queda confirmado
Pedidos valida sus reglas y guarda el nuevo estado. El hecho `PedidoConfirmado` puede interesar a Inventario, Entregas y Notificaciones.

### Paso 2: se publica el evento
Publicar significa dejar el evento disponible para consumidores interesados. El evento no significa que Inventario ya reservó unidades; solo informa que el pedido se confirmó.

### Paso 3: un consumidor inicia su tarea
Inventario puede recibir `PedidoConfirmado` y decidir reservar los productos. La reserva es otra acción y puede tener su propio resultado.

### Paso 4: una instrucción solicita algo concreto
Si el diseño separa el trabajo, un componente puede enviar el comando `ReservarProductos` dirigido a Inventario. El consumidor intenta cumplirlo y responde con un resultado.

### Paso 5: se publica el resultado
Si la reserva ocurrió, Inventario comunica `ProductosReservados`. Entregas puede entonces crear su tarea de preparación.

La secuencia no es una obligación idéntica para todo sistema. El equipo decide si una parte publica eventos, comandos o ambos, con nombres que describan su intención.

## 5. Ejemplo de datos de un evento
Un evento debe identificar el hecho y el elemento afectado. Un tipo C# sencillo podría ser:

```csharp
public sealed record PedidoConfirmado(
    Guid PedidoId,
    DateTimeOffset OcurridoEn);
```

`PedidoId` indica a qué pedido se refiere; `OcurridoEn` indica cuándo ocurrió el hecho. En un sistema real el mensaje puede requerir versión, origen u otros datos. Incluye solo lo necesario y evita información personal que los consumidores no necesitan.

El nombre en pasado ayuda a leerlo como hecho. No publiques `PedidoConfirmado` antes de guardar la confirmación; otros componentes podrían actuar sobre algo que luego no ocurrió.

## 6. Cola de trabajo y evento compartido no son lo mismo
Una cola de trabajo compartida suele distribuir tareas entre varios trabajadores: cada mensaje lo procesa uno de ellos.

Un evento puede interesar a varios componentes. Si Inventario, Entregas y Notificaciones deben enterarse de `PedidoConfirmado`, el sistema tiene que entregar la información a cada consumidor interesado; no debe repartirla entre ellos como si solo uno necesitara verla.

Pregunta clave: **¿quieres que una persona del grupo haga la tarea, o quieres que varias áreas sepan que ocurrió el hecho?**

## 7. Qué pasa si el consumidor recibe dos veces el mismo mensaje
Un mensaje puede repetirse si el consumidor hizo el trabajo pero la confirmación se perdió. Si procesa de nuevo `CrearEntrega`, puede crear una segunda entrega para el pedido.

El consumidor debe reconocer repeticiones que no deberían duplicar efectos. Una forma es conservar el identificador del mensaje o una clave de operación y revisar si ya se procesó.

Esto no significa que todos los errores se resuelvan ignorando mensajes duplicados. El consumidor tiene que distinguir una repetición idéntica de una nueva solicitud legítima.

## 8. Cuando un mensaje falla
Si la tarea no se puede procesar:

- un error temporal puede justificar un reintento limitado;
- un dato incorrecto necesita corrección, no repetición infinita;
- si tras varios intentos sigue fallando, puede enviarse a una cola de fallidos para investigar;
- el consumidor debe conservar suficiente contexto para relacionar el error con el pedido, sin exponer secretos.

Los siguientes videos profundizan en las tareas fallidas y en los flujos con más pasos.

## 9. Actividad de autoestudio
Clasifica cada mensaje como comando o evento y explica quién debería recibirlo:

1. `ReservarProductos(pedido 245)`.
2. `PedidoConfirmado(pedido 245)`.
3. `EnviarAvisoDeRetraso(pedido 245)`.
4. `AvisoDeRetrasoEnviado(pedido 245)`.
5. `AsignarRepartidor(pedido 245)`.
6. `RepartidorAsignado(pedido 245)`.

Después dibuja el camino de `PedidoConfirmado` hasta que Entregas recibe una tarea.

### Respuesta modelo
1. Comando: Inventario recibe una petición para reservar.
2. Evento: comunica un hecho que ya ocurrió; puede interesar a varios consumidores.
3. Comando: Notificaciones debe intentar enviar un aviso.
4. Evento: informa que el aviso ya se envió.
5. Comando: el servicio de asignación debe buscar un repartidor.
6. Evento: informa que un repartidor quedó asignado.

El camino puede ser: Pedidos confirma y publica el evento; Inventario reserva; al confirmarse la reserva se informa el resultado; Entregas recibe una tarea para preparar la ruta. Cada transición tiene un resultado explícito.

## Comprueba lo que aprendiste
1. ¿Qué diferencia hay entre comando y evento?
2. ¿Quién produce y quién consume en la tarea de preparar una entrega?
3. ¿Por qué una cola compartida no significa que todos los consumidores reciban cada mensaje?
4. ¿Qué protección evita crear una entrega duplicada?

### Respuestas
1. Un comando pide una acción; un evento comunica un hecho ocurrido.
2. Pedidos produce la tarea y Entregas la consume.
3. Una cola de trabajo suele repartir cada tarea entre los trabajadores disponibles.
4. El consumidor identifica la solicitud ya procesada y evita repetir el efecto.

## Conclusión
Mensajes es el término general. Un comando pide una acción a alguien; un evento informa algo que ya sucedió. Productor-consumidor separa quién crea el trabajo de quién lo procesa, a menudo con una cola que conserva tareas pendientes.

El diseño debe dejar claras la intención, la responsabilidad y la respuesta ante repetición o fallo. Si una parte no puede explicar qué mensaje produce y quién debe consumirlo, el contrato aún no está suficientemente claro.