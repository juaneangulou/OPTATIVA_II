# Video 53: Durable State vs Event Sourcing

## Título
Durable State vs Event Sourcing

## 🧭 Punto de partida
Vienes de trabajar process manager en flujos complejos. No vamos a repetirlo: lo usaremos como punto de partida para estudiar durable state vs event sourcing y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con máquinas de estado finito en el front-end.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Process manager en flujos complejos](video-52.md)

[➡️ Video siguiente: Máquinas de estado finito en el front-end](video-54.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 24: Evaluación de tecnologías y decisiones de stack'. La elección de tecnologías es una decisión arquitectónica y no una cuestión de moda. Cada stack tiene ventajas, costos y limitaciones. El video insiste en que seleccionar una tecnología debe hacerse con base en el problema, la capacidad del equipo, los requisitos de operación, la curva de aprendizaje y la sostenibilidad a largo plazo.

Muchas veces se adopta una tecnología por popularidad, pero eso no garantiza que se adapte bien al caso real. La evaluación del stack debe incluir mantenimiento, soporte, costos operativos, compatibilidad, seguridad y potencial de crecimiento. Así, la decisión de usar determinada herramienta o framework se vuelve más estratégica y menos impulsiva. En la plataforma logística, esto aparece cuando una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar durable state vs event sourcing con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: La elección de tecnologías es una decisión arquitectónica y no una cuestión de moda.

La fuente desarrolla esta situación con más detalle en el bloque anterior. Ahora quiero que hagamos algo distinto: separar el problema esencial de los detalles técnicos que podríamos elegir después.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta durable state vs event sourcing como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. Las tecnologías deben elegirse por contexto, no por tendencia.

Detente en la consecuencia de esta idea: Las tecnologías deben elegirse por contexto, no por tendencia. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. Cada stack implica costos de operación, entrenamiento y mantenimiento.

Detente en la consecuencia de esta idea: Cada stack implica costos de operación, entrenamiento y mantenimiento. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. Un buen stack debe facilitar velocidad de entrega y sostenibilidad.

Detente en la consecuencia de esta idea: Un buen stack debe facilitar velocidad de entrega y sostenibilidad. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 4. La elección tecnológica debe estar alineada con la estrategia del sistema.

Detente en la consecuencia de esta idea: La elección tecnológica debe estar alineada con la estrategia del sistema. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 5. La popularidad no siempre significa idoneidad.

Detente en la consecuencia de esta idea: La popularidad no siempre significa idoneidad. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. La arquitectura debe equilibrar innovación, estabilidad y costo total.

Ahora llévala a un escenario de crecimiento. La arquitectura debe equilibrar innovación, estabilidad y costo total. Imagina que aumenta el tráfico: identifica el primer cuello de botella y decide qué medirías antes de añadir infraestructura.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Estoy eligiendo tecnología por necesidad o por tendencia? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué tan bien se adapta mi stack a los objetivos del proyecto? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué costo oculto tiene la decisión tecnológica actual? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. La fuente afirma que Las tecnologías deben elegirse por contexto, no por tendencia.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: Elegir tecnologías es una forma de diseñar la capacidad del sistema para seguir funcionando bien en el futuro. La mejor decisión es la que resuelve el problema real con menos deuda técnica y menos riesgo. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa durable state vs event sourcing en tus propias palabras y relaciónalo con esta fuente: La elección de tecnologías es una decisión arquitectónica y no una cuestión de moda.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Estoy eligiendo tecnología por necesidad o por tendencia?** Mi respuesta de partida es: Las tecnologías deben elegirse por contexto, no por tendencia. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Qué tan bien se adapta mi stack a los objetivos del proyecto?** Mi respuesta de partida es: Cada stack implica costos de operación, entrenamiento y mantenimiento. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Qué costo oculto tiene la decisión tecnológica actual?** Mi respuesta de partida es: Un buen stack debe facilitar velocidad de entrega y sostenibilidad. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar durable state vs event sourcing, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia máquinas de estado finito en el front-end.

## 🤔 Para pensar antes de continuar
- ¿Estoy eligiendo tecnología por necesidad o por tendencia?
- ¿Qué tan bien se adapta mi stack a los objetivos del proyecto?
- ¿Qué costo oculto tiene la decisión tecnológica actual?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 5: pruebas, operación y defensa final. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
