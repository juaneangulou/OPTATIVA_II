# Video 17: Bounded context y context maps en microservicios

## Título
Cómo separar partes del sistema cuando las mismas palabras significan cosas distintas

## Resumen
En una plataforma logística, “pedido” puede significar una compra para el equipo comercial y un trabajo de entrega para el equipo de reparto. Si el programa trata ambos significados como si fueran idénticos, puede confundir estados o mezclar responsabilidades.

Un **bounded context** es un límite dentro del cual las palabras y reglas tienen un significado acordado. Un **context map** es un dibujo que muestra esos límites y la información que comparten. En el ejemplo, Compras y Pedidos conserva los datos de la compra; Entregas conserva la asignación, la ruta y la evidencia de recepción.

Primero aclaramos quién es responsable de cada dato y cómo se comparte. Después podemos decidir si esas partes deben ser módulos de una sola aplicación o servicios desplegados por separado. Tener límites claros no obliga a usar microservicios.

## Ideas para recordar
- Los nombres compartidos no siempre significan lo mismo para todas las áreas.
- Cada contexto necesita términos y reglas coherentes para su trabajo.
- Un mapa muestra qué información cruza entre contextos y quién la define.
- No es necesario compartir todos los datos de un área con las demás.
- Los límites de negocio pueden existir dentro de una sola aplicación.
- Crear microservicios agrega trabajo de comunicación y operación; debe responder a una necesidad real.

## Preguntas para comprobar tu comprensión
- ¿Qué diferencia hay entre un pedido comercial y una entrega?
- ¿Quién debería ser responsable de la última ubicación del repartidor?
- ¿Qué información necesita Compras compartir con Entregas?
- ¿Por qué un bounded context no significa automáticamente un microservicio?
