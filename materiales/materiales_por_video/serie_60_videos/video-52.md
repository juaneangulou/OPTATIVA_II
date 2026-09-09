# Video 52: Process manager en flujos complejos

## Título
Process manager en flujos complejos

## 🧭 Punto de partida
Vienes de trabajar comparing consumers para procesamiento en tiempo real. No vamos a repetirlo: lo usaremos como punto de partida para estudiar process manager en flujos complejos y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con durable state vs event sourcing.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Comparing consumers para procesamiento en tiempo real](video-51.md)

[➡️ Video siguiente: Durable State vs Event Sourcing](video-53.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 23: Estrategia tecnológica y roadmap'. El video aborda el papel de la estrategia tecnológica en la arquitectura. No basta con elegir una buena herramienta o un patrón útil; también hace falta una dirección clara para el camino del sistema. Una estrategia tecnológica define hacia dónde va la solución, qué capacidades se priorizan, qué riesgos se asumen y qué inversiones son necesarias para que la arquitectura evolucione de forma ordenada.

El roadmap se convierte en la herramienta que convierte la visión en acción. Cuando hay estrategia y planificación, el equipo evita decisiones aisladas y poco alineadas. El arquitecto tiene un rol importante en definir no solo cómo se construye el sistema, sino también qué se prioriza y en qué orden. En la plataforma logística, esto aparece cuando un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar process manager en flujos complejos con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: El video aborda el papel de la estrategia tecnológica en la arquitectura.

La fuente desarrolla esta situación con más detalle en el bloque anterior. Ahora quiero que hagamos algo distinto: separar el problema esencial de los detalles técnicos que podríamos elegir después.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta process manager en flujos complejos como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La estrategia tecnológica guía la evolución del sistema.

Detente en la consecuencia de esta idea: La estrategia tecnológica guía la evolución del sistema. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. Un roadmap ayuda a convertir visión en decisiones secuenciales.

Detente en la consecuencia de esta idea: Un roadmap ayuda a convertir visión en decisiones secuenciales. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. Las decisiones deben priorizar capacidades que generen valor real.

Detente en la consecuencia de esta idea: Las decisiones deben priorizar capacidades que generen valor real. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 4. Sin estrategia, la arquitectura puede volverse reactiva y caótica.

Detente en la consecuencia de esta idea: Sin estrategia, la arquitectura puede volverse reactiva y caótica. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 5. La planificación evita que el sistema se descontrole por soluciones aisladas.

Detente en la consecuencia de esta idea: La planificación evita que el sistema se descontrole por soluciones aisladas. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. El diseño técnico debe estar alineado con objetivos de negocio y capacidad operativa.

Detente en la consecuencia de esta idea: El diseño técnico debe estar alineado con objetivos de negocio y capacidad operativa. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué dirección tecnológica está tomando mi proyecto? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Tengo una hoja de ruta clara o solo decisiones aisladas? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué capacidades priorizaría para favorecer la evolución del sistema? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. La fuente afirma que La estrategia tecnológica guía la evolución del sistema.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La estrategia y el roadmap son lo que hacen que la arquitectura deje de ser una respuesta improvisada y se convierta en una dirección clara. Un sistema necesita visión para crecer sin perder coherencia. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa process manager en flujos complejos en tus propias palabras y relaciónalo con esta fuente: El video aborda el papel de la estrategia tecnológica en la arquitectura.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué dirección tecnológica está tomando mi proyecto?** Mi respuesta de partida es: La estrategia tecnológica guía la evolución del sistema. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Tengo una hoja de ruta clara o solo decisiones aisladas?** Mi respuesta de partida es: Un roadmap ayuda a convertir visión en decisiones secuenciales. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Qué capacidades priorizaría para favorecer la evolución del sistema?** Mi respuesta de partida es: Las decisiones deben priorizar capacidades que generen valor real. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar process manager en flujos complejos, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia durable state vs event sourcing.

## 🤔 Para pensar antes de continuar
- ¿Qué dirección tecnológica está tomando mi proyecto?
- ¿Tengo una hoja de ruta clara o solo decisiones aisladas?
- ¿Qué capacidades priorizaría para favorecer la evolución del sistema?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 4: implementación e integración. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
