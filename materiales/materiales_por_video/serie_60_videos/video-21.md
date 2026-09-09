# Video 21: Evolución del sistema y mantenimiento

## Título
Evolución del sistema y mantenimiento

## 🧭 Punto de partida
Vienes de trabajar devops y automatización de entrega. No vamos a repetirlo: lo usaremos como punto de partida para estudiar evolución del sistema y mantenimiento y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con comunicar la arquitectura con claridad.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: DevOps y automatización de entrega](video-20.md)

[➡️ Video siguiente: Comunicar la arquitectura con claridad](video-22.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 21: Diseño para cambio y evolución'. Este video introduce una de las ideas más importantes de la arquitectura moderna: un sistema no solo debe resolver el problema actual, sino prepararse para cambiar cuando cambien las necesidades del negocio o el contexto. El diseño arquitectónico debe pensar en la evolución como una variable esperada, no como una excepción. Por eso se enfatizan principios como la modularidad, la flexibilidad, la separación de responsabilidades y la protección de las capas críticas del sistema.

Cuando el software se diseña para el cambio, se vuelve más sostenible. En cambio, si se construye como una estructura rígida y demasiado acoplada, cualquier cambio pequeño termina convirtiéndose en una tarea riesgosa. La arquitectura entonces deja de ser una estructura estática y pasa a ser una base que permite crecer y adaptarse con menos fricción. En la plataforma logística, esto aparece cuando una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar evolución del sistema y mantenimiento con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video introduce una de las ideas más importantes de la arquitectura moderna: un sistema no solo debe resolver el problema actual, sino prepararse para cambiar cuando cambien las necesidades del negocio o el contexto.

La fuente desarrolla esta situación con más detalle en el bloque anterior. Ahora quiero que hagamos algo distinto: separar el problema esencial de los detalles técnicos que podríamos elegir después.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta evolución del sistema y mantenimiento como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La evolución es una característica normal del software, no un problema excepcional.

Detente en la consecuencia de esta idea: La evolución es una característica normal del software, no un problema excepcional. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. Un buen diseño reduce el costo de cambiar.

Detente en la consecuencia de esta idea: Un buen diseño reduce el costo de cambiar. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. La modularidad permite aislar áreas del sistema y facilitar adaptaciones.

Detente en la consecuencia de esta idea: La modularidad permite aislar áreas del sistema y facilitar adaptaciones. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 4. La arquitectura debe proteger los puntos sensibles del negocio.

Detente en la consecuencia de esta idea: La arquitectura debe proteger los puntos sensibles del negocio. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 5. Los cambios pequeños no deberían provocar grandes reestructuraciones.

Detente en la consecuencia de esta idea: Los cambios pequeños no deberían provocar grandes reestructuraciones. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. Diseñar para el cambio mejora la sostenibilidad a largo plazo.

Detente en la consecuencia de esta idea: Diseñar para el cambio mejora la sostenibilidad a largo plazo. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué partes de mi sistema son difíciles de cambiar? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy diseñando para el futuro o solo para la versión actual? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Dónde está la mayor fragilidad de mi solución ante cambios? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. La fuente afirma que La evolución es una característica normal del software, no un problema excepcional.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La arquitectura más útil es la que acepta que el sistema cambiará. Cuando el diseño está preparado para la evolución, el software se vuelve más robusto, adaptable y sostenible. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa evolución del sistema y mantenimiento en tus propias palabras y relaciónalo con esta fuente: Este video introduce una de las ideas más importantes de la arquitectura moderna: un sistema no solo debe resolver el problema actual, sino prepararse para cambiar cuando cambien las necesidades del negocio o el contexto.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué partes de mi sistema son difíciles de cambiar?** Mi respuesta de partida es: La evolución es una característica normal del software, no un problema excepcional. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Estoy diseñando para el futuro o solo para la versión actual?** Mi respuesta de partida es: Un buen diseño reduce el costo de cambiar. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Dónde está la mayor fragilidad de mi solución ante cambios?** Mi respuesta de partida es: La modularidad permite aislar áreas del sistema y facilitar adaptaciones. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar evolución del sistema y mantenimiento, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia comunicar la arquitectura con claridad.

## 🤔 Para pensar antes de continuar
- ¿Qué partes de mi sistema son difíciles de cambiar?
- ¿Estoy diseñando para el futuro o solo para la versión actual?
- ¿Dónde está la mayor fragilidad de mi solución ante cambios?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 3: diseño y dominio. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
