# Video 47: Infraestructura como código en monorepos

## Título
Infraestructura como código en monorepos

## 🧭 Punto de partida
Vienes de trabajar bounded context y context maps. No vamos a repetirlo: lo usaremos como punto de partida para estudiar infraestructura como código en monorepos y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con mensajes vs eventos en microservicios.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Bounded context y context maps](video-46.md)

[➡️ Video siguiente: Mensajes vs eventos en microservicios](video-48.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 17: Cultura de arquitectura en el equipo'. La arquitectura de software no se construye solo con diagramas o decisiones individuales; también depende de la cultura del equipo. Cuando el equipo entiende la importancia de la calidad, la comunicación, la responsabilidad y la evolución del sistema, la arquitectura tiene más posibilidades de ser sólida. Si la cultura del equipo es deficiente, incluso un buen diseño técnico puede terminar diluyéndose por falta de disciplina o consenso.

El video resalta que la arquitectura debe ser una práctica compartida, no un privilegio de unos pocos. Eso implica hablar sobre decisiones, revisar cambios, cuestionar supuestos, aceptar feedback y crear una mentalidad que valore la sostenibilidad por encima de la rapidez improvisada. En la plataforma logística, esto aparece cuando un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar infraestructura como código en monorepos con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: La arquitectura de software no se construye solo con diagramas o decisiones individuales; también depende de la cultura del equipo. Cuando el equipo entiende la importancia de la calidad, la comunicación, la responsabilidad y la evolución del sistema, la arquitectura tiene más posibilidades de ser sólida. Si la cultura del equipo es deficiente, incluso un buen diseño técnico puede terminar diluyéndose por falta de disciplina o consenso.

El video resalta que la arquitectura debe ser una práctica compartida, no un privilegio de unos pocos. Eso implica hablar sobre decisiones, revisar cambios, cuestionar supuestos, aceptar feedback y crear una mentalidad que valore la sostenibilidad por encima de la rapidez improvisada.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciona esa situación con el proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Aquí aparece el verdadero trabajo arquitectónico. No basta con saber que existe un patrón, una tecnología o una práctica. Necesitamos saber qué problema resuelve en este contexto, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta infraestructura como código en monorepos como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La arquitectura se fortalece con una cultura de calidad y reflexión.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 2. Los equipos necesitan una manera clara de discutir y decidir cambios.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 3. La mejora continua es más efectiva que la improvisación aislada.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 4. La construcción de software no es solo técnica; es una práctica colectiva.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 5. La cultura también determina si la arquitectura se mantiene viva o se vuelve obsoleta.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 6. Un equipo alineado toma mejores decisiones y soporta mejor la complejidad.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Mi equipo tiene una cultura clara para discutir decisiones de arquitectura? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Se valora la calidad del sistema por encima de la rapidez individual? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué hábitos del equipo están ayudando o dañando la evolución del software? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. La fuente afirma que La arquitectura se fortalece con una cultura de calidad y reflexión.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La arquitectura madura no vive solo en la solución; vive en la manera en que el equipo trabaja. Si la cultura del equipo favorece la claridad, la responsabilidad y la mejora constante, la arquitectura se fortalece de manera natural. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa infraestructura como código en monorepos en tus propias palabras y relaciónalo con esta fuente: La arquitectura de software no se construye solo con diagramas o decisiones individuales; también depende de la cultura del equipo.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Mi equipo tiene una cultura clara para discutir decisiones de arquitectura?** Mi respuesta de partida es: La arquitectura se fortalece con una cultura de calidad y reflexión. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Se valora la calidad del sistema por encima de la rapidez individual?** Mi respuesta de partida es: Los equipos necesitan una manera clara de discutir y decidir cambios. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Qué hábitos del equipo están ayudando o dañando la evolución del software?** Mi respuesta de partida es: La mejora continua es más efectiva que la improvisación aislada. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar infraestructura como código en monorepos, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia mensajes vs eventos en microservicios.

## 🤔 Para pensar antes de continuar
- ¿Mi equipo tiene una cultura clara para discutir decisiones de arquitectura?
- ¿Se valora la calidad del sistema por encima de la rapidez individual?
- ¿Qué hábitos del equipo están ayudando o dañando la evolución del software?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 4: implementación e integración. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
