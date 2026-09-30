# Video 19: Mensajes vs eventos en microservicios

## Título
La diferencia entre pedir una acción y avisar que algo ocurrió

## Resumen
Cuando varios servicios colaboran, necesitan enviarse información. Un **mensaje** es esa información enviada de una parte a otra. Su intención puede ser pedir una acción o comunicar un hecho que ya ocurrió.

“Reserva productos para el pedido 245” es una instrucción: Inventario todavía debe intentar hacer algo. “El pedido 245 fue confirmado” es un evento: Pedidos informa un hecho terminado que podría interesar a Inventario, Entregas y Notificaciones.

Un evento no garantiza que los demás servicios terminen su trabajo. Puede llegar tarde o repetirse, así que cada consumidor debe manejar esos casos. La diferencia clave es la intención: **¿estamos pidiendo que ocurra algo o contando que ya ocurrió?**

## Ideas principales
- Un mensaje lleva información entre partes de un sistema.
- Una instrucción pide una acción a un destinatario.
- Un evento cuenta un hecho que ya ocurrió y puede interesar a varios servicios.
- No se debe anunciar como ocurrido algo que todavía no se completó.
- Recibir un evento no garantiza que el consumidor terminó su trabajo.
- Una comunicación repetida no debe producir efectos dañinos duplicados.

## Preguntas para comprobar tu comprensión
- ¿“Envía una notificación” es una instrucción o un evento?
- ¿“La notificación fue enviada” es una instrucción o un evento?
- ¿Qué servicios podrían interesarse por el evento “Pedido confirmado”?
- ¿Qué riesgo existe si Inventario procesa dos veces la misma reserva?
