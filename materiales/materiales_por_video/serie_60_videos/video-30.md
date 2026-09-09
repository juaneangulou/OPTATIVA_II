# Video 30: Intuición vs método en arquitectura de software

## Título
Intuición vs método en arquitectura de software

## 🧭 Punto de partida
Vienes de trabajar cierre del curso de fundamentos. No vamos a repetirlo: lo usaremos como punto de partida para estudiar intuición vs método en arquitectura de software y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con cómo analizar una licitación real con ia.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Cierre del curso de fundamentos](video-29.md)

[➡️ Video siguiente: Cómo analizar una licitación real con IA](video-31.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 1: Intuición vs método en arquitectura de software'. El video parte de una idea clave: muchas personas logran construir software funcional usando solo intuición, experiencia y prueba y error. Eso puede funcionar a corto plazo, pero cuando el sistema crece, aparecen problemas de mantenimiento, complejidad, escalabilidad y entendimiento del negocio. La arquitectura de software deja de ser solo “programar bien” y pasa a ser tomar decisiones con criterio, fundamento y visión de largo plazo.

La discusión central compara dos enfoques: por un lado, la intuición, que permite improvisar y avanzar rápido; por otro, el método, que ayuda a pensar en el sistema como un conjunto de decisiones estratégicas, no solo soluciones técnicas. El video deja claro que el arquitecto no debe depender de la suerte ni de la improvisación constante: debe analizar contexto, restricciones, objetivos de negocio y riesgos. En la plataforma logística, esto aparece cuando un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar intuición vs método en arquitectura de software con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: El video parte de una idea clave: muchas personas logran construir software funcional usando solo intuición, experiencia y prueba y error.

La fuente desarrolla esta situación con más detalle en el bloque anterior. Ahora quiero que hagamos algo distinto: separar el problema esencial de los detalles técnicos que podríamos elegir después.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta intuición vs método en arquitectura de software como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La intuición es útil para comenzar, pero no garantiza que el sistema sobreviva al crecimiento.

Detente en la consecuencia de esta idea: La intuición es útil para comenzar, pero no garantiza que el sistema sobreviva al crecimiento. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. Un software puede “servir” sin ser realmente bueno si no está construido para sostener cambios.

Detente en la consecuencia de esta idea: Un software puede “servir” sin ser realmente bueno si no está construido para sostener cambios. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. La arquitectura de software implica decisiones sobre estructura, acoplamiento, escalabilidad, evolución y costos.

Ahora llévala a un escenario de crecimiento. La arquitectura de software implica decisiones sobre estructura, acoplamiento, escalabilidad, evolución y costos. Imagina que aumenta el tráfico: identifica el primer cuello de botella y decide qué medirías antes de añadir infraestructura.

### 4. El método permite reducir la incertidumbre y tomar decisiones con más base técnica y de negocio.

Detente en la consecuencia de esta idea: El método permite reducir la incertidumbre y tomar decisiones con más base técnica y de negocio. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 5. Un buen arquitecto combina experiencia, análisis y criterio, no solo creatividad.

Detente en la consecuencia de esta idea: Un buen arquitecto combina experiencia, análisis y criterio, no solo creatividad. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. El problema no es solo que el sistema funcione, sino que funcione bien en el tiempo.

Detente en la consecuencia de esta idea: El problema no es solo que el sistema funcione, sino que funcione bien en el tiempo. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué tan frecuente es resolver problemas solo con intuición en mi trabajo? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué problemas aparecen cuando el sistema crece sin una base metodológica? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué decisiones de arquitectura requieren más análisis que código? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. La fuente afirma que La intuición es útil para comenzar, pero no garantiza que el sistema sobreviva al crecimiento.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La diferencia entre intuición y método no es que uno sea bueno y el otro malo; más bien, la intuición es una base de partida y el método es lo que convierte una solución improvisada en una solución sostenible. La arquitectura de software exige pensar más allá del código y decidir con propósito. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa intuición vs método en arquitectura de software en tus propias palabras y relaciónalo con esta fuente: El video parte de una idea clave: muchas personas logran construir software funcional usando solo intuición, experiencia y prueba y error.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué tan frecuente es resolver problemas solo con intuición en mi trabajo?** Mi respuesta de partida es: La intuición es útil para comenzar, pero no garantiza que el sistema sobreviva al crecimiento. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Qué problemas aparecen cuando el sistema crece sin una base metodológica?** Mi respuesta de partida es: Un software puede “servir” sin ser realmente bueno si no está construido para sostener cambios. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Qué decisiones de arquitectura requieren más análisis que código?** Mi respuesta de partida es: La arquitectura de software implica decisiones sobre estructura, acoplamiento, escalabilidad, evolución y costos. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar intuición vs método en arquitectura de software, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia cómo analizar una licitación real con ia.

## 🤔 Para pensar antes de continuar
- ¿Qué tan frecuente es resolver problemas solo con intuición en mi trabajo?
- ¿Qué problemas aparecen cuando el sistema crece sin una base metodológica?
- ¿Qué decisiones de arquitectura requieren más análisis que código?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 4: implementación e integración. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
