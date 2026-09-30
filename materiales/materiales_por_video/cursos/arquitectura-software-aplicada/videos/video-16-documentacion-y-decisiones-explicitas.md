# Video 16: API Gateway como capa de abstracción en microservicios

## Para estudiar por tu cuenta
Lee primero la situación y dibuja el recorrido antes de mirar la solución. Si te atoras, usa estas pistas:

- **Pista 1:** pregunta quién tiene el dato del pedido y quién tiene el dato de la ubicación.
- **Pista 2:** la aplicación no debe recibir una ubicación que ningún servicio confirmó.
- **Pista 3:** al justificar la Gateway, menciona tanto lo que simplifica como la nueva pieza que el equipo debe mantener.

Cuando termines, compara tu respuesta con la solución comentada de la sección anterior. No necesitas dibujar exactamente las mismas flechas; necesitas poder explicar qué hace cada parte y por qué.

## Comprueba lo que aprendiste
Responde sin mirar las secciones anteriores y luego revisa las respuestas:

1. ¿Qué diferencia hay entre una API y una API Gateway?
2. ¿Qué parte conoce si el pedido existe? ¿Cuál conoce la última ubicación?
3. Si llega el estado del pedido pero no la ubicación, ¿qué podrías mostrar sin inventar información?
4. Menciona un motivo para usar una Gateway y un motivo para no usarla.
5. ¿Qué tarea no conviene trasladar a la Gateway si ya pertenece a un servicio?

### Respuestas para revisar tu comprensión
1. La API es el acuerdo sobre cómo pedir y responder. La Gateway es una entrada que recibe solicitudes y las dirige a uno o más servicios.
2. El servicio de pedidos conoce el pedido y su estado; el servicio de seguimiento conoce la última ubicación reportada.
3. Se puede mostrar el estado confirmado y explicar que la ubicación no está disponible. Si se muestra una ubicación anterior, hay que indicar cuándo se registró.
4. Usarla puede evitar que varias aplicaciones conozcan direcciones internas. No usarla puede ser mejor si una aplicación sencilla solo consulta un servicio y la Gateway no resuelve una necesidad real.
5. Una regla del negocio, como decidir si un repartidor puede aceptar otro pedido, debe seguir en el servicio responsable de esa decisión.

Si puedes responder con tus palabras y recorrer el ejemplo sin confundir las responsabilidades, ya comprendiste la idea central. Si no, vuelve a dibujar solo cuatro cajas: aplicación, Gateway, pedidos y seguimiento.

## Conclusión
Una API Gateway es una puerta común entre una aplicación y uno o varios servicios. Puede dirigir solicitudes y, cuando hace falta, organizar respuestas. Oculta algunos detalles internos, pero no elimina los acuerdos ni convierte a la Gateway en dueña de todos los datos.

Antes de agregarla, pregunta qué problema simplifica, qué nueva pieza tendrás que mantener, quién es responsable de cada información y qué respuesta recibirá el cliente cuando falte un dato. Una buena decisión se puede explicar incluyendo tanto su beneficio como su costo.

## Preguntas para llevarte
- ¿Cómo explicarías una API Gateway sin usar la palabra “Gateway”?
- ¿Qué información conoce cada parte del ejemplo?
- ¿Qué respuesta sería honesta si no podemos consultar la ubicación?
- ¿Qué costo nuevo aparece al agregar una puerta de entrada?
