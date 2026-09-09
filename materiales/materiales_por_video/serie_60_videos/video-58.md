# Video 58: Sabiduría y criterio en arquitectura de software

## Título
Sabiduría y criterio en arquitectura de software

## 🧭 Punto de partida
Vienes de trabajar opentelemetry e ingeniería del caos. No vamos a repetirlo: lo usaremos como punto de partida para estudiar sabiduría y criterio en arquitectura de software y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con riesgos, continuidad y decisiones bajo incertidumbre.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: OpenTelemetry e ingeniería del caos](video-57.md)

[➡️ Video siguiente: Riesgos, continuidad y decisiones bajo incertidumbre](video-59.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 21: Estrategia tecnológica y roadmap'. Este video enfatiza que la arquitectura no debe ir a la deriva. Debe estar guiada por una estrategia tecnológica clara que defina prioridades, inversiones y objetivos a largo plazo. El roadmap transforma la visión en un plan de acción, permitiendo que el sistema evolucione de manera ordenada y con menos improvisación.

Cuando no hay estrategia, cada decisión responde más a una urgencia que a un criterio sostenible. En ese contexto, el sistema crece sin dirección, y la deuda técnica se acumula. El roadmap ayuda a alinear equipo, negocio y tecnología. En la plataforma logística, esto aparece cuando durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar sabiduría y criterio en arquitectura de software con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video enfatiza que la arquitectura no debe ir a la deriva.

La fuente desarrolla esta situación con más detalle en el bloque anterior. Ahora quiero que hagamos algo distinto: separar el problema esencial de los detalles técnicos que podríamos elegir después.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta sabiduría y criterio en arquitectura de software como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La estrategia tecnológica da dirección al sistema.

Detente en la consecuencia de esta idea: La estrategia tecnológica da dirección al sistema. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. Un roadmap ayuda a priorizar y organizar el crecimiento.

Detente en la consecuencia de esta idea: Un roadmap ayuda a priorizar y organizar el crecimiento. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. La arquitectura debe responder a objetivos de negocio y capacidades reales.

Detente en la consecuencia de esta idea: La arquitectura debe responder a objetivos de negocio y capacidades reales. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 4. Sin estrategia, la solución se vuelve reactiva.

Detente en la consecuencia de esta idea: Sin estrategia, la solución se vuelve reactiva. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 5. La planificación anticipa riesgos y fortalece la evolución.

Detente en la consecuencia de esta idea: La planificación anticipa riesgos y fortalece la evolución. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. La intención detrás de cada decisión debe ser clara.

Detente en la consecuencia de esta idea: La intención detrás de cada decisión debe ser clara. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué dirección tecnológica está tomando mi proyecto? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Tengo un plan claro de evolución o solo reacciones inmediatas? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué capacidades necesito priorizar para crecer bien? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. La fuente afirma que La estrategia tecnológica da dirección al sistema.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La estrategia tecnológica es la base que le da sentido a la arquitectura. Sin ella, la solución se vuelve más reactiva y menos sostenida. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa sabiduría y criterio en arquitectura de software en tus propias palabras y relaciónalo con esta fuente: Este video enfatiza que la arquitectura no debe ir a la deriva.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué dirección tecnológica está tomando mi proyecto?** Mi respuesta de partida es: La estrategia tecnológica da dirección al sistema. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Tengo un plan claro de evolución o solo reacciones inmediatas?** Mi respuesta de partida es: Un roadmap ayuda a priorizar y organizar el crecimiento. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Qué capacidades necesito priorizar para crecer bien?** Mi respuesta de partida es: La arquitectura debe responder a objetivos de negocio y capacidades reales. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar sabiduría y criterio en arquitectura de software, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia riesgos, continuidad y decisiones bajo incertidumbre.

## 🤔 Para pensar antes de continuar
- ¿Qué dirección tecnológica está tomando mi proyecto?
- ¿Tengo un plan claro de evolución o solo reacciones inmediatas?
- ¿Qué capacidades necesito priorizar para crecer bien?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 5: pruebas, operación y defensa final. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
