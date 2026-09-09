# Video 48: Mensajes vs eventos en microservicios

## Título
Mensajes vs eventos en microservicios

## 🧭 Punto de partida
Vienes de trabajar infraestructura como código en monorepos. No vamos a repetirlo: lo usaremos como punto de partida para estudiar mensajes vs eventos en microservicios y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con productor consumidor y fan-in/fan-out.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Infraestructura como código en monorepos](video-47.md)

[➡️ Video siguiente: Productor consumidor y fan-in/fan-out](video-49.md)

## 🎥 La situación que vamos a resolver
La fuente consultada para esta clase es 'Video 18: Comunicación y negociación técnica'. En nuestro recorrido la conectamos con el tema 'Mensajes vs eventos en microservicios' porque queremos estudiar mensajes vs eventos en microservicios desde un problema real. La fuente plantea: Una gran parte del trabajo de un arquitecto no ocurre en un editor de código, sino en conversaciones. El arquitecto debe comunicar decisiones, explicar trade-offs, escuchar necesidades del negocio y convencer a diferentes actores sobre la dirección correcta de la solución. La comunicación técnica es una competencia esencial porque la arquitectura no se implementa solo con conocimiento; se ejecuta con consenso.

El video subraya que en muchas decisiones arquitectónicas hay conflictos entre necesidades de tiempo, costo, calidad, riesgo y visión. En esos momentos, la capacidad de negociar, sintetizar y explicar la elección correcta es tan importante como el conocimiento técnico. La arquitectura también se trata de ser claro, persuasivo y empático con quienes toman decisiones o se ven afectados por ellas. En la plataforma logística, esto aparece cuando un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Primero entenderemos la fuente y después construiremos la decisión.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar mensajes vs eventos en microservicios con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Una gran parte del trabajo de un arquitecto no ocurre en un editor de código, sino en conversaciones.

Ahora voy a separar contigo tres niveles: lo que la fuente afirma, el problema esencial que debemos resolver y las decisiones técnicas que podríamos tomar después. Si confundimos esos niveles, terminaremos usando una tecnología como respuesta a un problema que todavía no hemos definido.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta mensajes vs eventos en microservicios como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La arquitectura se comunica tanto como se diseña.

Detente en la consecuencia de esta idea: La arquitectura se comunica tanto como se diseña. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. Los stakeholders no siempre hablan el mismo lenguaje técnico.

Detente en la consecuencia de esta idea: Los stakeholders no siempre hablan el mismo lenguaje técnico. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. Los trade-offs deben explicarse de forma clara y útil.

Detente en la consecuencia de esta idea: Los trade-offs deben explicarse de forma clara y útil. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 4. Un arquitecto debe escuchar, explicar y alinear.

Detente en la consecuencia de esta idea: Un arquitecto debe escuchar, explicar y alinear. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 5. La negociación técnica ayuda a evitar decisiones impulsivas o incomprensibles.

Detente en la consecuencia de esta idea: La negociación técnica ayuda a evitar decisiones impulsivas o incomprensibles. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. La capacidad de comunicación convierte una buena idea en una decisión implementada.

En esta idea nos interesa el límite entre componentes. La capacidad de comunicación convierte una buena idea en una decisión implementada. Dibuja quién consume la información, qué contrato necesita y qué cambio podría romper al consumidor.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Estoy logrando comunicar claramente mis decisiones técnicas? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Cómo explico los trade-offs a personas no técnicas? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué decisiones de arquitectura se están bloqueando por falta de alineación o claridad? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🔀 Opciones para resolver mensajes vs eventos en microservicios

- **Opción A:** aplicar una solución sencilla dentro de la estructura actual, documentando sus límites.
- **Opción B:** introducir una separación o mecanismo especializado para proteger el riesgo principal de la fuente.

Compara ambas por costo inicial, calidad, operación, facilidad de cambio y evidencia disponible. Elige una solo después de explicar qué problema resuelve y qué costo aceptas.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. La fuente afirma que La arquitectura se comunica tanto como se diseña.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: El arquitecto no solo resuelve problemas técnicos; también ayuda a que el equipo y la organización compartan una visión común. Sin buena comunicación, incluso una arquitectura excelente puede fracasar por falta de comprensión o aceptación. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa mensajes vs eventos en microservicios en tus propias palabras y relaciónalo con esta fuente: Una gran parte del trabajo de un arquitecto no ocurre en un editor de código, sino en conversaciones.
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

1. **¿Estoy logrando comunicar claramente mis decisiones técnicas?** Mi respuesta de partida es: La arquitectura se comunica tanto como se diseña. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Cómo explico los trade-offs a personas no técnicas?** Mi respuesta de partida es: Los stakeholders no siempre hablan el mismo lenguaje técnico. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Qué decisiones de arquitectura se están bloqueando por falta de alineación o claridad?** Mi respuesta de partida es: Los trade-offs deben explicarse de forma clara y útil. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar mensajes vs eventos en microservicios, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia productor consumidor y fan-in/fan-out.

## 🤔 Para pensar antes de continuar
- ¿Estoy logrando comunicar claramente mis decisiones técnicas?
- ¿Cómo explico los trade-offs a personas no técnicas?
- ¿Qué decisiones de arquitectura se están bloqueando por falta de alineación o claridad?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 4: implementación e integración. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
