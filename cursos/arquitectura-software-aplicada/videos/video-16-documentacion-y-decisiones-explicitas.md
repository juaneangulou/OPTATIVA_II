# Video 16: API Gateway como capa de abstracción en microservicios

## Título
Cómo crear una puerta de entrada para que una aplicación encuentre los servicios que necesita

## Resumen
Cuando un programa está dividido en varias partes, cada parte puede encargarse de una tarea. En una plataforma logística, una parte conoce los pedidos y otra conoce las rutas. Una aplicación que necesita mostrar el seguimiento podría tener que preguntar a ambas y juntar las respuestas.

Una API Gateway funciona como una puerta de entrada común: recibe la solicitud, la dirige a los servicios que tienen la información y devuelve una respuesta organizada. Así, la aplicación no necesita conocer todos los detalles internos del sistema.

La Gateway no es necesaria en todos los proyectos y no resuelve por sí sola los problemas de velocidad o disponibilidad. También es una pieza nueva que el equipo debe mantener. Cada servicio debe conservar clara su responsabilidad, y la Gateway no debe inventar datos ni concentrar toda la lógica del negocio.

## El ejemplo del video
El cliente pregunta “¿dónde está mi pedido?”. La aplicación envía la consulta a la Gateway; esta la dirige al servicio de pedidos y al de seguimiento. Pedidos confirma el pedido y su estado; Seguimiento informa la última ubicación registrada.

Si Seguimiento no responde, la aplicación puede mostrar el estado confirmado y avisar que la ubicación no está disponible. No se debe inventar una ubicación ni presentar una ubicación antigua como actual.

## Ideas principales
- Una API es una forma acordada para que dos programas se pidan información.
- Un servicio es una parte del sistema responsable de una tarea concreta.
- Una API Gateway es una puerta de entrada que dirige solicitudes a uno o varios servicios.
- La Gateway puede reunir información, pero cada servicio sigue siendo dueño de sus datos y decisiones.
- Si la Gateway falla o recibe demasiadas responsabilidades, puede afectar muchas solicitudes.
- Antes de agregarla, hay que identificar qué problema resuelve y quién la operará.

## Conclusión
Una API Gateway puede simplificar la comunicación entre una aplicación y varios servicios, pero agrega otra pieza al sistema. La decisión tiene sentido cuando el beneficio de una entrada común supera el costo de mantenerla y cuando sus responsabilidades están bien delimitadas.

## Preguntas para pensar
- ¿Qué información del pedido conoce cada servicio?
- ¿Qué simplifica la Gateway para la aplicación del cliente?
- ¿Qué respuesta debería recibir el cliente si un servicio no está disponible?
- ¿Qué tendría que pasar para que una Gateway fuera innecesaria?

## Para comprobar tu comprensión
- Una **API** es el acuerdo que explica cómo pedir información y entender la respuesta.
- Una **Gateway** es la puerta de entrada que dirige esas solicitudes.
- El servicio que conoce un dato debe seguir siendo responsable de ese dato.
- La Gateway conviene cuando resuelve un problema concreto; también agrega trabajo de mantenimiento.
