# Video 12: Capas, límites y dependencias

## Título
Capas, límites y dependencias

## 🧭 Punto de partida
Vienes de trabajar monolito modular: empezar bien sin cerrarse. No vamos a repetirlo: lo usaremos como punto de partida para estudiar capas, límites y dependencias y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con microservicios y organización por dominios.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Monolito modular: empezar bien sin cerrarse](video-11.md)

[➡️ Video siguiente: Microservicios y organización por dominios](video-13.md)

## 🎥 La situación que vamos a resolver
La fuente consultada para esta clase es 'Video 6: Arquitectura como responsabilidad humana'. En nuestro recorrido la conectamos con el tema 'Capas, límites y dependencias' porque queremos estudiar capas, límites y dependencias desde un problema real. La fuente plantea: Este video conecta la arquitectura con la responsabilidad y el impacto humano. Un gran poder en tecnología trae grandes consecuencias. Cuando se crea software crítico o de alto impacto, cada decisión tiene un peso mucho mayor. La arquitectura ya no es solo un problema técnico; es una responsabilidad con personas, usuarios y contextos reales.

La idea es que un sistema puede cambiar vidas, facilitar decisiones o poner en riesgo seguridad, salud o confianza. Por eso, el arquitecto debe ser consciente de que el software no es neutral ni inofensivo: tiene un impacto concreto en la sociedad. En la plataforma logística, esto aparece cuando pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. Primero entenderemos la fuente y después construiremos la decisión.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar capas, límites y dependencias con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video conecta la arquitectura con la responsabilidad y el impacto humano.

Ahora voy a separar contigo tres niveles: lo que la fuente afirma, el problema esencial que debemos resolver y las decisiones técnicas que podríamos tomar después. Si confundimos esos niveles, terminaremos usando una tecnología como respuesta a un problema que todavía no hemos definido.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta capas, límites y dependencias como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. El poder técnico conlleva responsabilidad.

Aquí quiero que mires el riesgo humano de esta idea. El poder técnico conlleva responsabilidad. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

### 2. Los sistemas críticos requieren más rigor y criterio.

Detente en la consecuencia de esta idea: Los sistemas críticos requieren más rigor y criterio. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. La arquitectura afecta más que el rendimiento técnico.

Ahora llévala a un escenario de crecimiento. La arquitectura afecta más que el rendimiento técnico. Imagina que aumenta el tráfico: identifica el primer cuello de botella y decide qué medirías antes de añadir infraestructura.

### 4. La responsabilidad humana es central en la toma de decisiones.

Aquí quiero que mires el riesgo humano de esta idea. La responsabilidad humana es central en la toma de decisiones. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

### 5. El software puede salvar o poner en riesgo, según cómo se diseñe.

Detente en la consecuencia de esta idea: El software puede salvar o poner en riesgo, según cómo se diseñe. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. No todo problema es técnico; muchos tienen impacto social y ético.

Aquí quiero que mires el riesgo humano de esta idea. No todo problema es técnico; muchos tienen impacto social y ético. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué tipo de impacto tiene el software que estoy diseñando? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy asumiendo una responsabilidad real con las personas que lo usan? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué decisiones de diseño pueden afectar la confianza, seguridad o bienestar de otros? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🔀 Opciones para resolver capas, límites y dependencias

- **Opción A:** aplicar una solución sencilla dentro de la estructura actual, documentando sus límites.
- **Opción B:** introducir una separación o mecanismo especializado para proteger el riesgo principal de la fuente.

Compara ambas por costo inicial, calidad, operación, facilidad de cambio y evidencia disponible. Elige una solo después de explicar qué problema resuelve y qué costo aceptas.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. La fuente afirma que El poder técnico conlleva responsabilidad.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La arquitectura de software tiene un lado humano muy claro. Un buen diseño no solo resuelve un problema; también protege a quienes lo usan y respeta la responsabilidad del creador. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa capas, límites y dependencias en tus propias palabras y relaciónalo con esta fuente: Este video conecta la arquitectura con la responsabilidad y el impacto humano.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🛠️ Resolución paso a paso

1. Define el problema que la fuente ayuda a resolver.
2. Identifica a los actores y el riesgo principal.
3. Compara dos opciones concretas.
4. Elige una solución proporcional al MVP.
5. Declara qué queda fuera y cuándo revisarás la decisión.
6. Define una prueba, métrica o evidencia.
7. Documenta la decisión y sus trade-offs en GitHub.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué tipo de impacto tiene el software que estoy diseñando?** Mi respuesta de partida es: El poder técnico conlleva responsabilidad. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Estoy asumiendo una responsabilidad real con las personas que lo usan?** Mi respuesta de partida es: Los sistemas críticos requieren más rigor y criterio. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Qué decisiones de diseño pueden afectar la confianza, seguridad o bienestar de otros?** Mi respuesta de partida es: La arquitectura afecta más que el rendimiento técnico. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar capas, límites y dependencias, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia microservicios y organización por dominios.

## 🤔 Para pensar antes de continuar
- ¿Qué tipo de impacto tiene el software que estoy diseñando?
- ¿Estoy asumiendo una responsabilidad real con las personas que lo usan?
- ¿Qué decisiones de diseño pueden afectar la confianza, seguridad o bienestar de otros?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 2: requisitos y decisión estructural. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
