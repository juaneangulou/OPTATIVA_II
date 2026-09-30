# Video 24: Durable State vs Event Sourcing en sistemas

## Título
Guardar cómo está un pedido o guardar cada cambio que tuvo

## Resumen
Una aplicación debe recordar la información aunque se reinicie. Una opción es guardar el **estado actual** del pedido: “Entregado”. Otra opción es conservar una secuencia de eventos: “Pedido creado”, “Repartidor asignado” y “Pedido entregado”, y reconstruir el estado aplicando esos hechos.

La primera opción facilita consultar lo que ocurre ahora. **Event Sourcing** permite reconstruir la historia completa, pero requiere organizar los eventos, sus correcciones y la forma de consultarlos. Guardar logs de errores no es lo mismo que usar Event Sourcing.

## Ideas principales
- Persistir es conservar datos para volver a utilizarlos después.
- El estado actual muestra cómo está algo en este momento.
- Event Sourcing guarda como fuente principal los hechos que causaron los cambios.
- Una vista calculada puede resumir eventos para hacer consultas más rápidas.
- La historia completa puede ayudar en auditorías, pero agrega complejidad.
- La alternativa correcta depende de qué necesita conocer el negocio.

## Preguntas para comprobar tu comprensión
- ¿Qué diferencia hay entre estado actual e historia de eventos?
- ¿Un registro técnico de errores basta para llamar Event Sourcing al sistema?
- ¿Qué necesidad podría justificar guardar cada cambio del pedido?
- ¿Qué costo asumiría el equipo al reconstruir el estado desde eventos?
