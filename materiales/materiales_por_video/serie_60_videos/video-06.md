# Video 6: Calidad observable: rendimiento, seguridad y disponibilidad

## Título
Calidad observable: rendimiento, seguridad y disponibilidad

## 🧭 Punto de partida
Vienes de trabajar requisitos funcionales y no funcionales. No vamos a repetirlo: lo usaremos como punto de partida para estudiar calidad observable: rendimiento, seguridad y disponibilidad y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con costos ocultos y deuda técnica.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Requisitos funcionales y no funcionales](video-05.md)

[➡️ Video siguiente: Costos ocultos y deuda técnica](video-07.md)

## 🎥 La situación que vamos a resolver
La fuente consultada para esta clase es 'Video 7: Escalabilidad y rendimiento'. En nuestro recorrido la conectamos con el tema 'Calidad observable: rendimiento, seguridad y disponibilidad' porque queremos estudiar calidad observable: rendimiento, seguridad y disponibilidad desde un problema real. La fuente plantea: El video aborda la diferencia entre un sistema que funciona con pocos usuarios y un sistema que mantiene calidad cuando la carga aumenta. La escalabilidad no es un concepto abstracto: se refiere a la capacidad del sistema para crecer sin perder rendimiento, estabilidad o calidad de servicio. También se menciona que no siempre la solución correcta es “hacerlo más grande”, sino diseñarlo para adaptarse a la demanda con una estrategia clara.

El rendimiento no depende solo de servidores o hardware; también influye la estructura del sistema, la forma en que se comunican componentes, el uso de caché, la distribución de responsabilidades y la calidad del diseño. Aquí aparece la idea de que la escalabilidad debe planearse desde el inicio, pero no siempre con una arquitectura más compleja que el problema justifique. En la plataforma logística, esto aparece cuando la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. Primero entenderemos la fuente y después construiremos la decisión.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar calidad observable: rendimiento, seguridad y disponibilidad con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: El video aborda la diferencia entre un sistema que funciona con pocos usuarios y un sistema que mantiene calidad cuando la carga aumenta.

Ahora voy a separar contigo tres niveles: lo que la fuente afirma, el problema esencial que debemos resolver y las decisiones técnicas que podríamos tomar después. Si confundimos esos niveles, terminaremos usando una tecnología como respuesta a un problema que todavía no hemos definido.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta calidad observable: rendimiento, seguridad y disponibilidad como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. Escalabilidad significa crecer sin romper el sistema.

Ahora llévala a un escenario de crecimiento. Escalabilidad significa crecer sin romper el sistema. Imagina que aumenta el tráfico: identifica el primer cuello de botella y decide qué medirías antes de añadir infraestructura.

### 2. El rendimiento es un problema de diseño, no solo de infraestructura.

Ahora llévala a un escenario de crecimiento. El rendimiento es un problema de diseño, no solo de infraestructura. Imagina que aumenta el tráfico: identifica el primer cuello de botella y decide qué medirías antes de añadir infraestructura.

### 3. Un sistema puede ser lento por mala arquitectura, no solo por falta de recursos.

Detente en la consecuencia de esta idea: Un sistema puede ser lento por mala arquitectura, no solo por falta de recursos. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 4. Aumentar capacidad no siempre es la mejor solución; a veces hay que mejorar diseño.

Detente en la consecuencia de esta idea: Aumentar capacidad no siempre es la mejor solución; a veces hay que mejorar diseño. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 5. La escalabilidad exige análisis de carga, demanda y evolución del negocio.

Ahora llévala a un escenario de crecimiento. La escalabilidad exige análisis de carga, demanda y evolución del negocio. Imagina que aumenta el tráfico: identifica el primer cuello de botella y decide qué medirías antes de añadir infraestructura.

### 6. La arquitectura debe decidir cuándo escalar horizontal o verticalmente, y qué costo tiene cada opción.

Detente en la consecuencia de esta idea: La arquitectura debe decidir cuándo escalar horizontal o verticalmente, y qué costo tiene cada opción. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Mi sistema está preparado para crecer en usuarios, tráfico o complejidad? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué cuellos de botella reales existen hoy? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy agregando infraestructura sin resolver el problema raíz de diseño? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🔀 Opciones para resolver calidad observable: rendimiento, seguridad y disponibilidad

- **Opción A:** aplicar una solución sencilla dentro de la estructura actual, documentando sus límites.
- **Opción B:** introducir una separación o mecanismo especializado para proteger el riesgo principal de la fuente.

Compara ambas por costo inicial, calidad, operación, facilidad de cambio y evidencia disponible. Elige una solo después de explicar qué problema resuelve y qué costo aceptas.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. La fuente afirma que Escalabilidad significa crecer sin romper el sistema.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La escalabilidad y el rendimiento son indicadores de madurez arquitectónica. Un sistema que puede crecer sin perder calidad no solo sirve mejor, sino que también reduce riesgos operativos y costos de corrección a largo plazo. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa calidad observable: rendimiento, seguridad y disponibilidad en tus propias palabras y relaciónalo con esta fuente: El video aborda la diferencia entre un sistema que funciona con pocos usuarios y un sistema que mantiene calidad cuando la carga aumenta.
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

1. **¿Mi sistema está preparado para crecer en usuarios, tráfico o complejidad?** Mi respuesta de partida es: Escalabilidad significa crecer sin romper el sistema. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Qué cuellos de botella reales existen hoy?** Mi respuesta de partida es: El rendimiento es un problema de diseño, no solo de infraestructura. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Estoy agregando infraestructura sin resolver el problema raíz de diseño?** Mi respuesta de partida es: Un sistema puede ser lento por mala arquitectura, no solo por falta de recursos. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar calidad observable: rendimiento, seguridad y disponibilidad, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia costos ocultos y deuda técnica.

## 🤔 Para pensar antes de continuar
- ¿Mi sistema está preparado para crecer en usuarios, tráfico o complejidad?
- ¿Qué cuellos de botella reales existen hoy?
- ¿Estoy agregando infraestructura sin resolver el problema raíz de diseño?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 1: diagnóstico y contexto arquitectónico. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
