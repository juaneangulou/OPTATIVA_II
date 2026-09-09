# Video 54: Máquinas de estado finito en el front-end

## Título
Máquinas de estado finito en el front-end

## 🧭 Punto de partida
Vienes de trabajar durable state vs event sourcing. No vamos a repetirlo: lo usaremos como punto de partida para estudiar máquinas de estado finito en el front-end y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con sast, dast y pentesting.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Durable State vs Event Sourcing](video-53.md)

[➡️ Video siguiente: SAST, DAST y pentesting](video-55.md)

## 🎥 La situación que vamos a resolver
La fuente consultada para esta clase es 'Video 25: Riesgos, costos y sostenibilidad financiera'. En nuestro recorrido la conectamos con el tema 'Máquinas de estado finito en el front-end' porque queremos estudiar máquinas de estado finito en el front-end desde un problema real. La fuente plantea: La arquitectura de software también tiene implicaciones económicas. Un sistema no solo debe funcionar desde el punto de vista técnico; también debe ser viable desde el punto de vista financiero, operativo y de mantenimiento. Este video muestra que las decisiones de arquitectura implican costos directos e indirectos: infraestructura, equipos, tiempo, soporte, seguridad, correcciones y capacidad de adaptación.

La sostenibilidad financiera no es solo una preocupación del negocio; también afecta la arquitectura. Si el sistema es demasiado costoso de operar o difícil de mantener, su valor real disminuye. Por ello, el arquitecto debe ser capaz de medir el costo total de una solución y no solo el costo inicial de desarrollo. En la plataforma logística, esto aparece cuando una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. Primero entenderemos la fuente y después construiremos la decisión.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar máquinas de estado finito en el front-end con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: La arquitectura de software también tiene implicaciones económicas.

Ahora voy a separar contigo tres niveles: lo que la fuente afirma, el problema esencial que debemos resolver y las decisiones técnicas que podríamos tomar después. Si confundimos esos niveles, terminaremos usando una tecnología como respuesta a un problema que todavía no hemos definido.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta máquinas de estado finito en el front-end como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La arquitectura tiene un costo real en infraestructura, operación y mantenimiento.

Detente en la consecuencia de esta idea: La arquitectura tiene un costo real en infraestructura, operación y mantenimiento. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. Los riesgos técnicos y financieros deben evaluarse en conjunto.

Detente en la consecuencia de esta idea: Los riesgos técnicos y financieros deben evaluarse en conjunto. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. Un diseño barato al principio puede volverse muy costoso después.

Detente en la consecuencia de esta idea: Un diseño barato al principio puede volverse muy costoso después. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 4. La sostenibilidad financiera depende del equilibrio entre valor y costo.

Detente en la consecuencia de esta idea: La sostenibilidad financiera depende del equilibrio entre valor y costo. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 5. El arquitecto debe considerar el costo total de propiedad del sistema.

Detente en la consecuencia de esta idea: El arquitecto debe considerar el costo total de propiedad del sistema. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. Las decisiones de diseño deben pesar impacto, riesgo y beneficios a largo plazo.

Aquí quiero que mires el riesgo humano de esta idea. Las decisiones de diseño deben pesar impacto, riesgo y beneficios a largo plazo. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué costo total real tiene mi solución? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy optimizando solo el desarrollo inicial o la sostenibilidad del sistema? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué riesgo financiero o operativo estoy aceptando con esta arquitectura? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🔀 Opciones para resolver máquinas de estado finito en el front-end

- **Opción A:** aplicar una solución sencilla dentro de la estructura actual, documentando sus límites.
- **Opción B:** introducir una separación o mecanismo especializado para proteger el riesgo principal de la fuente.

Compara ambas por costo inicial, calidad, operación, facilidad de cambio y evidencia disponible. Elige una solo después de explicar qué problema resuelve y qué costo aceptas.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. La fuente afirma que La arquitectura tiene un costo real en infraestructura, operación y mantenimiento.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: El software no es solo una decisión técnica: es también una decisión financiera y estratégica. Una arquitectura sostenible es la que crea valor sin generar costos ocultos que la vuelvan inviable con el tiempo. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa máquinas de estado finito en el front-end en tus propias palabras y relaciónalo con esta fuente: La arquitectura de software también tiene implicaciones económicas.
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

1. **¿Qué costo total real tiene mi solución?** Mi respuesta de partida es: La arquitectura tiene un costo real en infraestructura, operación y mantenimiento. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Estoy optimizando solo el desarrollo inicial o la sostenibilidad del sistema?** Mi respuesta de partida es: Los riesgos técnicos y financieros deben evaluarse en conjunto. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Qué riesgo financiero o operativo estoy aceptando con esta arquitectura?** Mi respuesta de partida es: Un diseño barato al principio puede volverse muy costoso después. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar máquinas de estado finito en el front-end, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia sast, dast y pentesting.

## 🤔 Para pensar antes de continuar
- ¿Qué costo total real tiene mi solución?
- ¿Estoy optimizando solo el desarrollo inicial o la sostenibilidad del sistema?
- ¿Qué riesgo financiero o operativo estoy aceptando con esta arquitectura?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 5: pruebas, operación y defensa final. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
