# Video 25: Escalabilidad, seguridad y ética

## Título
Escalabilidad, seguridad y ética

## 🧭 Punto de partida
Vienes de trabajar arquitectura como responsabilidad humana. No vamos a repetirlo: lo usaremos como punto de partida para estudiar escalabilidad, seguridad y ética y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con principios de diseño y fundamentos de estructura.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Arquitectura como responsabilidad humana](video-24.md)

[➡️ Video siguiente: Principios de diseño y fundamentos de estructura](video-26.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 7: Escalabilidad, seguridad y ética'. Este video reúne varios ejes esenciales de la arquitectura: escalabilidad, seguridad y ética. La idea es que un sistema no puede considerarse bueno solo porque escala bien o porque funciona bajo carga. Si no protege datos, no piensa en accesibilidad ni considera el impacto humano, termina generando problemas más allá de lo técnico.

La arquitectura debe equilibrar rendimiento con responsabilidad. Un diseño escalable y seguro es valioso, pero si ignora principios éticos o de inclusión, su impacto puede ser negativo. La arquitectura debe pensarse como un conjunto de decisiones integradas, no como políticas aisladas. En la plataforma logística, esto aparece cuando una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar escalabilidad, seguridad y ética con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video reúne varios ejes esenciales de la arquitectura: escalabilidad, seguridad y ética.

La fuente desarrolla esta situación con más detalle en el bloque anterior. Ahora quiero que hagamos algo distinto: separar el problema esencial de los detalles técnicos que podríamos elegir después.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta escalabilidad, seguridad y ética como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. Escalabilidad sin seguridad es una solución incompleta.

Aquí quiero que mires el riesgo humano de esta idea. Escalabilidad sin seguridad es una solución incompleta. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

### 2. La seguridad debe pensarse desde el diseño, no como parche final.

Aquí quiero que mires el riesgo humano de esta idea. La seguridad debe pensarse desde el diseño, no como parche final. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

### 3. La ética no es un tema ajeno; forma parte del valor del sistema.

Aquí quiero que mires el riesgo humano de esta idea. La ética no es un tema ajeno; forma parte del valor del sistema. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

### 4. Un sistema debe ser útil y responsable al mismo tiempo.

Detente en la consecuencia de esta idea: Un sistema debe ser útil y responsable al mismo tiempo. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 5. La calidad arquitectónica incluye impacto humano, no solo desempeño técnico.

Aquí quiero que mires el riesgo humano de esta idea. La calidad arquitectónica incluye impacto humano, no solo desempeño técnico. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

### 6. La construcción de software implica decisiones que afectan a personas reales.

Detente en la consecuencia de esta idea: La construcción de software implica decisiones que afectan a personas reales. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Mi sistema considera cuestiones de seguridad y ética desde el inicio? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué tan preparado está para crecer sin perder responsabilidad? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué impacto real puede tener mi diseño en personas o comunidades? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. La fuente afirma que Escalabilidad sin seguridad es una solución incompleta.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La arquitectura sólida combina crecimiento, protección y responsabilidad. Un sistema digno de confianza debe pensar en la gente que lo usa, no solo en la eficiencia técnica. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa escalabilidad, seguridad y ética en tus propias palabras y relaciónalo con esta fuente: Este video reúne varios ejes esenciales de la arquitectura: escalabilidad, seguridad y ética.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Mi sistema considera cuestiones de seguridad y ética desde el inicio?** Mi respuesta de partida es: Escalabilidad sin seguridad es una solución incompleta. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Qué tan preparado está para crecer sin perder responsabilidad?** Mi respuesta de partida es: La seguridad debe pensarse desde el diseño, no como parche final. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Qué impacto real puede tener mi diseño en personas o comunidades?** Mi respuesta de partida es: La ética no es un tema ajeno; forma parte del valor del sistema. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar escalabilidad, seguridad y ética, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia principios de diseño y fundamentos de estructura.

## 🤔 Para pensar antes de continuar
- ¿Mi sistema considera cuestiones de seguridad y ética desde el inicio?
- ¿Qué tan preparado está para crecer sin perder responsabilidad?
- ¿Qué impacto real puede tener mi diseño en personas o comunidades?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 3: diseño y dominio. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
