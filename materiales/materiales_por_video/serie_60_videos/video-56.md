# Video 56: Fitness functions para medir arquitectura

## Título
Fitness functions para medir arquitectura

## 🧭 Punto de partida
Vienes de trabajar sast, dast y pentesting. No vamos a repetirlo: lo usaremos como punto de partida para estudiar fitness functions para medir arquitectura y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con opentelemetry e ingeniería del caos.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: SAST, DAST y pentesting](video-55.md)

[➡️ Video siguiente: OpenTelemetry e ingeniería del caos](video-57.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 28: Arquitectura con impacto social y ético'. El video introduce un enfoque humanista y ético en la arquitectura de software. Un sistema no solo afecta procesos técnicos y económicos, sino también personas, comunidades y valores. Por eso, la arquitectura debe considerar implicaciones sociales, de privacidad, accesibilidad, inclusión y responsabilidad. Un sistema que funciona técnicamente puede causar daño si no se diseña con criterio ético.

Esto invita a pensar que el arquitecto no actúa solo como técnico, sino también como responsable del impacto de sus decisiones. Cuando se diseña software para personas, su contexto social y sus necesidades humanas deben integrarse en la solución. Este enfoque aporta más valor y reduce consecuencias negativas en el largo plazo. En la plataforma logística, esto aparece cuando durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar fitness functions para medir arquitectura con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: El video introduce un enfoque humanista y ético en la arquitectura de software.

La fuente desarrolla esta situación con más detalle en el bloque anterior. Ahora quiero que hagamos algo distinto: separar el problema esencial de los detalles técnicos que podríamos elegir después.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta fitness functions para medir arquitectura como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La tecnología tiene impacto real sobre personas, comunidades y decisiones humanas.

Aquí quiero que mires el riesgo humano de esta idea. La tecnología tiene impacto real sobre personas, comunidades y decisiones humanas. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

### 2. La ética no es ajena a la arquitectura; es parte de la responsabilidad del diseño.

Aquí quiero que mires el riesgo humano de esta idea. La ética no es ajena a la arquitectura; es parte de la responsabilidad del diseño. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

### 3. La privacidad, la accesibilidad y la inclusión deben considerarse en el sistema.

Aquí quiero que mires el riesgo humano de esta idea. La privacidad, la accesibilidad y la inclusión deben considerarse en el sistema. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

### 4. Un sistema puede tener éxito técnico y aun así fallar socialmente.

Detente en la consecuencia de esta idea: Un sistema puede tener éxito técnico y aun así fallar socialmente. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 5. El arquitecto debe pensar en el impacto más allá del flujo de datos o del algoritmo.

Aquí quiero que mires el riesgo humano de esta idea. El arquitecto debe pensar en el impacto más allá del flujo de datos o del algoritmo. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

### 6. El diseño responsable es una práctica de ingeniería con sentido humano.

Detente en la consecuencia de esta idea: El diseño responsable es una práctica de ingeniería con sentido humano. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué impacto social tiene mi sistema? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy considerando accesibilidad, inclusión y responsabilidad en el diseño? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿La solución que construyo beneficia a todos o solo a ciertos actores? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. La fuente afirma que La tecnología tiene impacto real sobre personas, comunidades y decisiones humanas.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La arquitectura no es neutral. Sus decisiones tienen impacto social y ético. Un buen diseño considera el efecto real que tendrá en las personas y en la sociedad, no solo en la lógica de la aplicación. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa fitness functions para medir arquitectura en tus propias palabras y relaciónalo con esta fuente: El video introduce un enfoque humanista y ético en la arquitectura de software.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué impacto social tiene mi sistema?** Mi respuesta de partida es: La tecnología tiene impacto real sobre personas, comunidades y decisiones humanas. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Estoy considerando accesibilidad, inclusión y responsabilidad en el diseño?** Mi respuesta de partida es: La ética no es ajena a la arquitectura; es parte de la responsabilidad del diseño. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿La solución que construyo beneficia a todos o solo a ciertos actores?** Mi respuesta de partida es: La privacidad, la accesibilidad y la inclusión deben considerarse en el sistema. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar fitness functions para medir arquitectura, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia opentelemetry e ingeniería del caos.

## 🤔 Para pensar antes de continuar
- ¿Qué impacto social tiene mi sistema?
- ¿Estoy considerando accesibilidad, inclusión y responsabilidad en el diseño?
- ¿La solución que construyo beneficia a todos o solo a ciertos actores?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 5: pruebas, operación y defensa final. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
