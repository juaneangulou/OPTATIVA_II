# Video 51: Comparing consumers para procesamiento en tiempo real

## Título
Comparing consumers para procesamiento en tiempo real

## 🧭 Punto de partida
Vienes de trabajar dead letter queue en sistemas distribuidos. No vamos a repetirlo: lo usaremos como punto de partida para estudiar comparing consumers para procesamiento en tiempo real y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con process manager en flujos complejos.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Dead Letter Queue en sistemas distribuidos](video-50.md)

[➡️ Video siguiente: Process manager en flujos complejos](video-52.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 22: Calidad de servicio y experiencia de usuario'. La arquitectura de software no solo se mide por qué tan bien se ejecuta internamente, sino por la experiencia que entrega a quienes la usan. Si el sistema es técnicamente sólido pero lento, poco intuitivo o inconsistente, la arquitectura termina fallando en la práctica. Este video conecta calidad técnica con calidad percibida por el usuario: tiempo de respuesta, confiabilidad, claridad, disponibilidad y consistencia.

Cuando el sistema es parte de una experiencia de negocio, la calidad de servicio se vuelve una necesidad de diseño. Un sistema puede estar bien estructurado, pero si no entrega valor de forma clara y confiable, no cumple su propósito. La arquitectura debe aportar experiencia y resultados, no solo estructura interna. En la plataforma logística, esto aparece cuando un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar comparing consumers para procesamiento en tiempo real con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: La arquitectura de software no solo se mide por qué tan bien se ejecuta internamente, sino por la experiencia que entrega a quienes la usan. Si el sistema es técnicamente sólido pero lento, poco intuitivo o inconsistente, la arquitectura termina fallando en la práctica. Este video conecta calidad técnica con calidad percibida por el usuario: tiempo de respuesta, confiabilidad, claridad, disponibilidad y consistencia.

Cuando el sistema es parte de una experiencia de negocio, la calidad de servicio se vuelve una necesidad de diseño. Un sistema puede estar bien estructurado, pero si no entrega valor de forma clara y confiable, no cumple su propósito. La arquitectura debe aportar experiencia y resultados, no solo estructura interna.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciona esa situación con el proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Aquí aparece el verdadero trabajo arquitectónico. No basta con saber que existe un patrón, una tecnología o una práctica. Necesitamos saber qué problema resuelve en este contexto, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta comparing consumers para procesamiento en tiempo real como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La experiencia del usuario es una consecuencia del diseño arquitectónico.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 2. Calidad técnica y calidad de servicio no son conceptos separados.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 3. El tiempo de respuesta, la estabilidad y la claridad influyen en la percepción del sistema.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 4. Un servicio bueno no solo funciona; funciona con un nivel de calidad soportable.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 5. La arquitectura debe anticipar la experiencia real del usuario final.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 6. El impacto del software se mide también por la continuidad y confiabilidad que ofrece.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué tan buena es la experiencia de uso de mi sistema? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué factores técnicos afectan la percepción del usuario? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy optimizando para robustez interna sin considerar la calidad percibida? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. La fuente afirma que La experiencia del usuario es una consecuencia del diseño arquitectónico.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La arquitectura debe diseñarse para entregar valor no solo dentro del equipo técnico, sino también en la experiencia real del usuario. La calidad de servicio aparece como indicador de que la solución responde bien a las necesidades del entorno. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa comparing consumers para procesamiento en tiempo real en tus propias palabras y relaciónalo con esta fuente: La arquitectura de software no solo se mide por qué tan bien se ejecuta internamente, sino por la experiencia que entrega a quienes la usan.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué tan buena es la experiencia de uso de mi sistema?** Mi respuesta de partida es: La experiencia del usuario es una consecuencia del diseño arquitectónico. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Qué factores técnicos afectan la percepción del usuario?** Mi respuesta de partida es: Calidad técnica y calidad de servicio no son conceptos separados. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Estoy optimizando para robustez interna sin considerar la calidad percibida?** Mi respuesta de partida es: El tiempo de respuesta, la estabilidad y la claridad influyen en la percepción del sistema. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar comparing consumers para procesamiento en tiempo real, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia process manager en flujos complejos.

## 🤔 Para pensar antes de continuar
- ¿Qué tan buena es la experiencia de uso de mi sistema?
- ¿Qué factores técnicos afectan la percepción del usuario?
- ¿Estoy optimizando para robustez interna sin considerar la calidad percibida?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 4: implementación e integración. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
