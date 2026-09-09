# Video 20: DevOps y automatización de entrega

## Título
DevOps y automatización de entrega

## 🧭 Punto de partida
Vienes de trabajar testing y validación de arquitectura. No vamos a repetirlo: lo usaremos como punto de partida para estudiar devops y automatización de entrega y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con evolución del sistema y mantenimiento.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Testing y validación de arquitectura](video-19.md)

[➡️ Video siguiente: Evolución del sistema y mantenimiento](video-21.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 18: DevOps y automatización de entrega'. Este video conecta arquitectura con entrega continua. La forma en que se construye, prueba, despliega y opera una aplicación influye directamente en su calidad. Si el proceso de entrega es manual y poco repetible, el sistema será más frágil incluso si su diseño inicial es bueno. Por eso DevOps y automatización son parte interesante de la arquitectura moderna.

La entrega automatizada permite reducir errores humanos, aumentar velocidad, mejorar reusabilidad y hacer más segura la evolución del sistema. El objetivo no es solo desplegar más rápido, sino hacerlo de manera controlada y confiable. En la plataforma logística, esto aparece cuando una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar devops y automatización de entrega con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video conecta arquitectura con entrega continua.

La fuente desarrolla esta situación con más detalle en el bloque anterior. Ahora quiero que hagamos algo distinto: separar el problema esencial de los detalles técnicos que podríamos elegir después.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta devops y automatización de entrega como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La entrega continua es parte de la arquitectura.

Detente en la consecuencia de esta idea: La entrega continua es parte de la arquitectura. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. La automatización reduce errores y acelera cambios seguros.

Detente en la consecuencia de esta idea: La automatización reduce errores y acelera cambios seguros. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. Las pruebas y despliegues deben ser repetibles y controlados.

Esta idea solo queda completa cuando podemos comprobarla. Las pruebas y despliegues deben ser repetibles y controlados. Elige una prueba o métrica y explica qué resultado confirmaría o cuestionaría nuestra decisión sobre devops y automatización de entrega.

### 4. La operación y el desarrollo deben alinearse en un mismo flujo.

Detente en la consecuencia de esta idea: La operación y el desarrollo deben alinearse en un mismo flujo. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 5. Un flujo de entrega sólido aumenta la confianza en el sistema.

Detente en la consecuencia de esta idea: Un flujo de entrega sólido aumenta la confianza en el sistema. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. La arquitectura moderna integra proceso y tecnología.

Detente en la consecuencia de esta idea: La arquitectura moderna integra proceso y tecnología. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué tan automatizado está mi proceso de entrega? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué riesgos se reducen o aumentan con el flujo actual? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy priorizando velocidad sin perder control y calidad? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. La fuente afirma que La entrega continua es parte de la arquitectura.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La automatización de entrega no es solo una práctica operativa, sino una decisión arquitectónica que mejora confiabilidad, velocidad y sostenibilidad. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa devops y automatización de entrega en tus propias palabras y relaciónalo con esta fuente: Este video conecta arquitectura con entrega continua.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué tan automatizado está mi proceso de entrega?** Mi respuesta de partida es: La entrega continua es parte de la arquitectura. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Qué riesgos se reducen o aumentan con el flujo actual?** Mi respuesta de partida es: La automatización reduce errores y acelera cambios seguros. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Estoy priorizando velocidad sin perder control y calidad?** Mi respuesta de partida es: Las pruebas y despliegues deben ser repetibles y controlados. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar devops y automatización de entrega, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia evolución del sistema y mantenimiento.

## 🤔 Para pensar antes de continuar
- ¿Qué tan automatizado está mi proceso de entrega?
- ¿Qué riesgos se reducen o aumentan con el flujo actual?
- ¿Estoy priorizando velocidad sin perder control y calidad?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 3: diseño y dominio. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
