# Video 33: Trunk Based Development y reglas de calidad

## Título
Trunk Based Development y reglas de calidad

## 🧭 Punto de partida
Vienes de trabajar monorepos con pantsbuild en proyectos reales. No vamos a repetirlo: lo usaremos como punto de partida para estudiar trunk based development y reglas de calidad y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con behavior driven development para alinear equipos.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Monorepos con Pantsbuild en proyectos reales](video-32.md)

[➡️ Video siguiente: Behavior Driven Development para alinear equipos](video-34.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 4: Principios, calidad y trade-offs'. Este video habla de una realidad central en arquitectura de software: no existe una solución perfecta para todos los casos, sino decisiones que equilibran objetivos en conflicto. A menudo el equipo quiere velocidad, el negocio quiere menor costo, la operación quiere estabilidad y el usuario quiere experiencia rápida. La arquitectura de software consiste en resolver esas tensiones con criterio técnico y estratégico.

La idea principal es que la calidad del diseño no se mide solo por cuán elegante es, sino por cuán bien se adapta al problema real. Un sistema puede ser técnicamente sofisticado y aun así ser un mal diseño si no considera costo, complejidad, operatividad y capacidad de evolución. El video enfatiza la importancia de principios, ya que los principios ayudan a tomar decisiones cuando no hay una respuesta única. En la plataforma logística, esto aparece cuando un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar trunk based development y reglas de calidad con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video habla de una realidad central en arquitectura de software: no existe una solución perfecta para todos los casos, sino decisiones que equilibran objetivos en conflicto. A menudo el equipo quiere velocidad, el negocio quiere menor costo, la operación quiere estabilidad y el usuario quiere experiencia rápida. La arquitectura de software consiste en resolver esas tensiones con criterio técnico y estratégico.

La idea principal es que la calidad del diseño no se mide solo por cuán elegante es, sino por cuán bien se adapta al problema real. Un sistema puede ser técnicamente sofisticado y aun así ser un mal diseño si no considera costo, complejidad, operatividad y capacidad de evolución. El video enfatiza la importancia de principios, ya que los principios ayudan a tomar decisiones cuando no hay una respuesta única.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciona esa situación con el proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Aquí aparece el verdadero trabajo arquitectónico. No basta con saber que existe un patrón, una tecnología o una práctica. Necesitamos saber qué problema resuelve en este contexto, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta trunk based development y reglas de calidad como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. No todo en arquitectura es absoluto; muchas decisiones implican trade-offs.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 2. La calidad del diseño depende del contexto, no de una fórmula universal.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 3. Un sistema debe balancear velocidad, claridad, costo, rendimiento y sostenibilidad.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 4. Los principios técnicos ayudan a evitar decisiones impulsivas o improvisadas.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 5. Componer arquitecturas buenas requiere identificar qué realmente importa en ese caso.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 6. La mejor decisión suele ser la que mejor resuelve el problema real y no la más “bonita” en teoría.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué trade-off estoy asumiendo sin darme cuenta en mi proyecto? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy priorizando la solución más elegante o la más adecuada? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué principio me ayuda a tomar mejores decisiones cuando hay conflicto de objetivos? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. La fuente afirma que No todo en arquitectura es absoluto; muchas decisiones implican trade-offs.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La arquitectura no es una búsqueda de perfección abstracta, sino de equilibrio. El arquitecto debe aprender a elegir entre alternativas con sentido, entendiendo que cada decisión tiene consecuencias en costo, mantenimiento y evolución del sistema. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa trunk based development y reglas de calidad en tus propias palabras y relaciónalo con esta fuente: Este video habla de una realidad central en arquitectura de software: no existe una solución perfecta para todos los casos, sino decisiones que equilibran objetivos en conflicto.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué trade-off estoy asumiendo sin darme cuenta en mi proyecto?** Mi respuesta de partida es: No todo en arquitectura es absoluto; muchas decisiones implican trade-offs. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Estoy priorizando la solución más elegante o la más adecuada?** Mi respuesta de partida es: La calidad del diseño depende del contexto, no de una fórmula universal. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Qué principio me ayuda a tomar mejores decisiones cuando hay conflicto de objetivos?** Mi respuesta de partida es: Un sistema debe balancear velocidad, claridad, costo, rendimiento y sostenibilidad. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar trunk based development y reglas de calidad, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia behavior driven development para alinear equipos.

## 🤔 Para pensar antes de continuar
- ¿Qué trade-off estoy asumiendo sin darme cuenta en mi proyecto?
- ¿Estoy priorizando la solución más elegante o la más adecuada?
- ¿Qué principio me ayuda a tomar mejores decisiones cuando hay conflicto de objetivos?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 4: implementación e integración. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
