# Video 7: Costos ocultos y deuda técnica

## Título
Costos ocultos y deuda técnica

## 🧭 Punto de partida
Vienes de trabajar calidad observable: rendimiento, seguridad y disponibilidad. No vamos a repetirlo: lo usaremos como punto de partida para estudiar costos ocultos y deuda técnica y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con riesgos y supuestos en diseño.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Calidad observable: rendimiento, seguridad y disponibilidad](video-06.md)

[➡️ Video siguiente: Riesgos y supuestos en diseño](video-08.md)

## 🎥 La situación que vamos a resolver
La fuente consultada para esta clase es 'Video 20: Riesgos, costos y decisiones bajo incertidumbre'. En nuestro recorrido la conectamos con el tema 'Costos ocultos y deuda técnica' porque queremos estudiar costos ocultos y deuda técnica desde un problema real. La fuente plantea: Este video habla de los riesgos y costos que subyacen a cada decisión arquitectónica. No siempre se tiene toda la información antes de elegir una solución. En ese contexto, el arquitecto debe evaluar qué tan reversible es la decisión, cuál es su costo real y qué riesgos conlleva. La incertidumbre es normal, pero la mala gestión de la misma puede generar decisiones impulsivas o demasiado rígidas.

La toma de decisiones bajo incertidumbre exige criterio: priorizar opciones que permitan aprender, adaptarse y cambiar sin grandes pérdidas. Así, el sistema se vuelve más resiliente frente a cambios de negocio o de contexto. En la plataforma logística, esto aparece cuando la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. Primero entenderemos la fuente y después construiremos la decisión.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar costos ocultos y deuda técnica con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video habla de los riesgos y costos que subyacen a cada decisión arquitectónica.

Ahora voy a separar contigo tres niveles: lo que la fuente afirma, el problema esencial que debemos resolver y las decisiones técnicas que podríamos tomar después. Si confundimos esos niveles, terminaremos usando una tecnología como respuesta a un problema que todavía no hemos definido.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta costos ocultos y deuda técnica como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La incertidumbre es parte del trabajo arquitectónico.

Detente en la consecuencia de esta idea: La incertidumbre es parte del trabajo arquitectónico. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. Cada decisión tiene costos y riesgos que no siempre son visibles de inmediato.

Detente en la consecuencia de esta idea: Cada decisión tiene costos y riesgos que no siempre son visibles de inmediato. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. La reversibilidad ayuda a decisión bajo cambios.

Detente en la consecuencia de esta idea: La reversibilidad ayuda a decisión bajo cambios. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 4. La arquitectura debe permitir aprender y ajustar.

Detente en la consecuencia de esta idea: La arquitectura debe permitir aprender y ajustar. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 5. La estrategia debe incluir evaluación de riesgos y costos.

Detente en la consecuencia de esta idea: La estrategia debe incluir evaluación de riesgos y costos. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. El criterio profesional sigue siendo clave en escenarios incompletos.

Detente en la consecuencia de esta idea: El criterio profesional sigue siendo clave en escenarios incompletos. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué decisiones de mi proyecto se están tomando con mucha incertidumbre? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué tan reversible es esta decisión si cambian las condiciones? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy analizando riesgo y costos reales o solo el beneficio inmediato? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🔀 Opciones para resolver costos ocultos y deuda técnica

- **Opción A:** aplicar una solución sencilla dentro de la estructura actual, documentando sus límites.
- **Opción B:** introducir una separación o mecanismo especializado para proteger el riesgo principal de la fuente.

Compara ambas por costo inicial, calidad, operación, facilidad de cambio y evidencia disponible. Elige una solo después de explicar qué problema resuelve y qué costo aceptas.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. La fuente afirma que La incertidumbre es parte del trabajo arquitectónico.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: Bajo incertidumbre, la mejor decisión no siempre es la más ambiciosa, sino la que permite aprender, adaptarse y sostener el sistema con menos riesgo. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa costos ocultos y deuda técnica en tus propias palabras y relaciónalo con esta fuente: Este video habla de los riesgos y costos que subyacen a cada decisión arquitectónica.
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

1. **¿Qué decisiones de mi proyecto se están tomando con mucha incertidumbre?** Mi respuesta de partida es: La incertidumbre es parte del trabajo arquitectónico. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Qué tan reversible es esta decisión si cambian las condiciones?** Mi respuesta de partida es: Cada decisión tiene costos y riesgos que no siempre son visibles de inmediato. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Estoy analizando riesgo y costos reales o solo el beneficio inmediato?** Mi respuesta de partida es: La reversibilidad ayuda a decisión bajo cambios. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar costos ocultos y deuda técnica, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia riesgos y supuestos en diseño.

## 🤔 Para pensar antes de continuar
- ¿Qué decisiones de mi proyecto se están tomando con mucha incertidumbre?
- ¿Qué tan reversible es esta decisión si cambian las condiciones?
- ¿Estoy analizando riesgo y costos reales o solo el beneficio inmediato?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 1: diagnóstico y contexto arquitectónico. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
