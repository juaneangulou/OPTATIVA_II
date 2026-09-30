# Video 23: Qué es el patrón Process Manager

## Título
Coordinar un proceso largo sin perder de vista cada pedido

## Resumen
Preparar una entrega puede requerir reservar productos, asignar un repartidor y avisar al cliente. Un **Process Manager** guarda en qué paso está cada pedido, envía la solicitud siguiente y decide qué hacer cuando un paso falla o tarda.

El Process Manager coordina el proceso completo, pero no reemplaza a los servicios responsables. Inventario sigue decidiendo si hay unidades; Entregas sigue asignando rutas. Si el flujo falla después de reservar productos, el Process Manager puede iniciar una acción de compensación, como liberar la reserva.

Este patrón ayuda cuando hay varios pasos, demoras y rutas de error. Agrega almacenamiento de estado y lógica de coordinación, así que no hace falta para un flujo corto que puede resolverse directamente.

## Ideas principales
- El proceso debe recordar su estado aunque un servicio se reinicie.
- Cada respuesta se relaciona con el pedido correcto.
- Una repetición no debe crear reservas o entregas duplicadas.
- Una compensación es una acción nueva que corrige un efecto anterior.
- Las reglas locales pertenecen a sus servicios; el Process Manager coordina los pasos.
- El patrón aporta claridad, pero también costo de operación y pruebas.

## Preguntas para comprobar tu comprensión
- ¿Qué información debería guardar el Process Manager?
- ¿Qué parte decide si hay inventario disponible?
- ¿Qué harías si no se encuentra repartidor después de reservar productos?
- ¿En qué caso una coordinación directa sería más sencilla?
