# Video 5: Requisitos funcionales y no funcionales

## Título
Requisitos funcionales y no funcionales

## 🧭 Punto de partida
Vienes de trabajar negocio, usuarios y contexto. No vamos a repetirlo: lo usaremos como punto de partida para estudiar requisitos funcionales y no funcionales y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con calidad observable: rendimiento, seguridad y disponibilidad.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Negocio, usuarios y contexto](video-04.md)

[➡️ Video siguiente: Calidad observable: rendimiento, seguridad y disponibilidad](video-06.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 5: Documentar decisiones y mantener claridad'. Este video profundiza en la importancia de dejar explícitas las decisiones de arquitectura. Muchas veces el problema no es solo que el sistema funcione, sino que se vuelva difícil de entender por quien lo revisa después. Cuando las decisiones no se documentan, cada persona asume una interpretación distinta y eso termina generando inconsistencias.

La idea es documentar el contexto, la intención, los riesgos, las restricciones y las alternativas descartadas. Esa práctica no solo ayuda al mantenimiento, sino también a que el equipo pueda evaluar si una solución sigue siendo apropiada con el tiempo. La documentación debe ser clara, viva y útil. En la plataforma logística, esto aparece cuando la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar requisitos funcionales y no funcionales con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video profundiza en la importancia de dejar explícitas las decisiones de arquitectura.

La fuente desarrolla esta situación con más detalle en el bloque anterior. Ahora quiero que hagamos algo distinto: separar el problema esencial de los detalles técnicos que podríamos elegir después.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta requisitos funcionales y no funcionales como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. Las decisiones de arquitectura deben dejarse escritas.

Detente en la consecuencia de esta idea: Las decisiones de arquitectura deben dejarse escritas. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. La documentación ayuda a preservar conocimiento y continuidad.

Detente en la consecuencia de esta idea: La documentación ayuda a preservar conocimiento y continuidad. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. Debe aclarar intención, restricciones, riesgos y alternativas.

Detente en la consecuencia de esta idea: Debe aclarar intención, restricciones, riesgos y alternativas. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 4. La arquitectura viva reduce la ambigüedad y mejora la evolución.

Detente en la consecuencia de esta idea: La arquitectura viva reduce la ambigüedad y mejora la evolución. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 5. El código por sí solo no siempre explica el porqué del diseño.

Detente en la consecuencia de esta idea: El código por sí solo no siempre explica el porqué del diseño. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. Documentar ayuda a la comprensión del presente y del futuro.

Detente en la consecuencia de esta idea: Documentar ayuda a la comprensión del presente y del futuro. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Estoy escribiendo solo el resultado o también el razonamiento detrás de la solución? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué decisiones clave del proyecto podrían perderse si se cambia de equipo? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Mi documentación refleja la realidad actual del sistema? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. La fuente afirma que Las decisiones de arquitectura deben dejarse escritas.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La documentación no es burocracia: es una forma de mantener la claridad del sistema y evitar que el conocimiento se pierda. La arquitectura se vuelve más sólida cuando está documentada y compartida. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa requisitos funcionales y no funcionales en tus propias palabras y relaciónalo con esta fuente: Este video profundiza en la importancia de dejar explícitas las decisiones de arquitectura.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Estoy escribiendo solo el resultado o también el razonamiento detrás de la solución?** Mi respuesta de partida es: Las decisiones de arquitectura deben dejarse escritas. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Qué decisiones clave del proyecto podrían perderse si se cambia de equipo?** Mi respuesta de partida es: La documentación ayuda a preservar conocimiento y continuidad. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Mi documentación refleja la realidad actual del sistema?** Mi respuesta de partida es: Debe aclarar intención, restricciones, riesgos y alternativas. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar requisitos funcionales y no funcionales, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia calidad observable: rendimiento, seguridad y disponibilidad.

## 🤔 Para pensar antes de continuar
- ¿Estoy escribiendo solo el resultado o también el razonamiento detrás de la solución?
- ¿Qué decisiones clave del proyecto podrían perderse si se cambia de equipo?
- ¿Mi documentación refleja la realidad actual del sistema?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 1: diagnóstico y contexto arquitectónico. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
