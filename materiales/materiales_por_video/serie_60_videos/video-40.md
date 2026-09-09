# Video 40: Técnicas pre-mortem para prevenir fallos

## Título
Técnicas pre-mortem para prevenir fallos

## 🧭 Punto de partida
Vienes de trabajar domain driven design para arquitectura limpia. No vamos a repetirlo: lo usaremos como punto de partida para estudiar técnicas pre-mortem para prevenir fallos y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con premortem como guía de pruebas de arquitectura.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Domain Driven Design para arquitectura limpia](video-39.md)

[➡️ Video siguiente: Premortem como guía de pruebas de arquitectura](video-41.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 9: Seguridad y privacidad'. La seguridad es una parte esencial de la arquitectura, no un tema opcional que se resuelve al final. Un sistema puede ser rápido y funcional, pero si no maneja bien autenticación, autorización, cifrado, validación de datos y control de acceso, puede poner en riesgo información crítica y la confianza del usuario. El video llama la atención sobre el hecho de que los problemas de seguridad no siempre aparecen como fallas técnicas evidentes: muchas veces son decisiones de diseño que dejan brechas invisibles.

También se habla de privacidad como un principio arquitectónico, no solo como cumplimiento. Diseñar con privacidad implica limitar datos, controlar acceso, definir responsabilidades y evitar recopilar más información de la necesaria. La arquitectura debe pensar en la seguridad desde las capas más básicas hasta el comportamiento del sistema en producción. En la plataforma logística, esto aparece cuando durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar técnicas pre-mortem para prevenir fallos con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: La seguridad es una parte esencial de la arquitectura, no un tema opcional que se resuelve al final. Un sistema puede ser rápido y funcional, pero si no maneja bien autenticación, autorización, cifrado, validación de datos y control de acceso, puede poner en riesgo información crítica y la confianza del usuario. El video llama la atención sobre el hecho de que los problemas de seguridad no siempre aparecen como fallas técnicas evidentes: muchas veces son decisiones de diseño que dejan brechas invisibles.

También se habla de privacidad como un principio arquitectónico, no solo como cumplimiento. Diseñar con privacidad implica limitar datos, controlar acceso, definir responsabilidades y evitar recopilar más información de la necesaria. La arquitectura debe pensar en la seguridad desde las capas más básicas hasta el comportamiento del sistema en producción.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciona esa situación con el proyecto: durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. Aquí aparece el verdadero trabajo arquitectónico. No basta con saber que existe un patrón, una tecnología o una práctica. Necesitamos saber qué problema resuelve en este contexto, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta técnicas pre-mortem para prevenir fallos como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La seguridad debe ser un eje arquitectónico, no un detalle a último momento.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 2. La confianza del usuario depende del manejo responsable de datos.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 3. Hay que proteger no solo la aplicación, sino sus flujos de datos y sus dependencias.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 4. La privacidad implica principio de mínimo privilegio y minimización de datos.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 5. Los fallos de seguridad suelen ser resultado de decisiones de diseño y no solo de bugs aislados.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 6. La arquitectura más segura es la que anticipa riesgos antes de que el sistema entre en producción.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué datos sensibles maneja mi sistema? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy limitando el acceso y la exposición de información de forma consciente? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿He diseñado la seguridad a partir del riesgo real o solo de la experiencia de uso? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. La fuente afirma que La seguridad debe ser un eje arquitectónico, no un detalle a último momento.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: Un sistema con buena arquitectura no solo resuelve necesidades funcionales, sino que protege la información, reduce riesgos y genera confianza. La seguridad y la privacidad no se agregan al final: se diseñan desde el principio. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa técnicas pre-mortem para prevenir fallos en tus propias palabras y relaciónalo con esta fuente: La seguridad es una parte esencial de la arquitectura, no un tema opcional que se resuelve al final.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué datos sensibles maneja mi sistema?** Mi respuesta de partida es: La seguridad debe ser un eje arquitectónico, no un detalle a último momento. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Estoy limitando el acceso y la exposición de información de forma consciente?** Mi respuesta de partida es: La confianza del usuario depende del manejo responsable de datos. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿He diseñado la seguridad a partir del riesgo real o solo de la experiencia de uso?** Mi respuesta de partida es: Hay que proteger no solo la aplicación, sino sus flujos de datos y sus dependencias. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar técnicas pre-mortem para prevenir fallos, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia premortem como guía de pruebas de arquitectura.

## 🤔 Para pensar antes de continuar
- ¿Qué datos sensibles maneja mi sistema?
- ¿Estoy limitando el acceso y la exposición de información de forma consciente?
- ¿He diseñado la seguridad a partir del riesgo real o solo de la experiencia de uso?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 5: pruebas, operación y defensa final. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
