# Video 11: Monolito modular: empezar bien sin cerrarse

## Título
Monolito modular: empezar bien sin cerrarse

## 🧭 Punto de partida
Vienes de trabajar estructura del sistema y estilos arquitectónicos. No vamos a repetirlo: lo usaremos como punto de partida para estudiar monolito modular: empezar bien sin cerrarse y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con capas, límites y dependencias.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Estructura del sistema y estilos arquitectónicos](video-10.md)

[➡️ Video siguiente: Capas, límites y dependencias](video-12.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 11: Monolito vs arquitectura distribuida'. Este video compara dos enfoques arquitectónicos muy comunes: el monolito y la arquitectura distribuida. El monolito puede ser una buena opción cuando el sistema es relativamente pequeño o cuando se desea velocidad de desarrollo y menor complejidad operativa. Sin embargo, cuando el proyecto crece y la organización requiere mayor desacople y evolución independiente, la arquitectura distribuida puede ser más apropiada.

La clave no es elegir una opción “mejor” en abstracto, sino seleccionar la que mejor se adapte a la complejidad real del sistema, el tamaño del equipo, la carga de trabajo y los objetivos de negocio. El problema aparece cuando se adopta una solución distribuida solo por moda, sin analizar su costo operativo. En la plataforma logística, esto aparece cuando pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar monolito modular: empezar bien sin cerrarse con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video compara dos enfoques arquitectónicos muy comunes: el monolito y la arquitectura distribuida.

La fuente desarrolla esta situación con más detalle en el bloque anterior. Ahora quiero que hagamos algo distinto: separar el problema esencial de los detalles técnicos que podríamos elegir después.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta monolito modular: empezar bien sin cerrarse como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. El monolito y la arquitectura distribuida tienen ventajas y costos distintos.

Detente en la consecuencia de esta idea: El monolito y la arquitectura distribuida tienen ventajas y costos distintos. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. La elección depende del problema real, no de la tendencia.

Detente en la consecuencia de esta idea: La elección depende del problema real, no de la tendencia. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. El monolito reduce complejidad de operación, pero puede limitar evolución.

Detente en la consecuencia de esta idea: El monolito reduce complejidad de operación, pero puede limitar evolución. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 4. La arquitectura distribuida mejora desacople y escalabilidad, pero aumenta complejidad.

Ahora llévala a un escenario de crecimiento. La arquitectura distribuida mejora desacople y escalabilidad, pero aumenta complejidad. Imagina que aumenta el tráfico: identifica el primer cuello de botella y decide qué medirías antes de añadir infraestructura.

### 5. No todo sistema necesita microservicios para ser bueno.

En esta idea nos interesa el límite entre componentes. No todo sistema necesita microservicios para ser bueno. Dibuja quién consume la información, qué contrato necesita y qué cambio podría romper al consumidor.

### 6. La decisión arquitectónica debe ser funcional y estratégica.

Detente en la consecuencia de esta idea: La decisión arquitectónica debe ser funcional y estratégica. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Mi sistema necesita más desacople o más simplicidad? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy adoptando una arquitectura por moda o por necesidad real? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué costos operativos estoy asumiendo con una distribución de servicios? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. La fuente afirma que El monolito y la arquitectura distribuida tienen ventajas y costos distintos.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: No existe una arquitectura universalmente superior; la mejor opción es la que responde mejor al problema real, a la organización y a la capacidad de evolución del sistema. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa monolito modular: empezar bien sin cerrarse en tus propias palabras y relaciónalo con esta fuente: Este video compara dos enfoques arquitectónicos muy comunes: el monolito y la arquitectura distribuida.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Mi sistema necesita más desacople o más simplicidad?** Mi respuesta de partida es: El monolito y la arquitectura distribuida tienen ventajas y costos distintos. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Estoy adoptando una arquitectura por moda o por necesidad real?** Mi respuesta de partida es: La elección depende del problema real, no de la tendencia. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Qué costos operativos estoy asumiendo con una distribución de servicios?** Mi respuesta de partida es: El monolito reduce complejidad de operación, pero puede limitar evolución. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar monolito modular: empezar bien sin cerrarse, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia capas, límites y dependencias.

## 🤔 Para pensar antes de continuar
- ¿Mi sistema necesita más desacople o más simplicidad?
- ¿Estoy adoptando una arquitectura por moda o por necesidad real?
- ¿Qué costos operativos estoy asumiendo con una distribución de servicios?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 2: requisitos y decisión estructural. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
