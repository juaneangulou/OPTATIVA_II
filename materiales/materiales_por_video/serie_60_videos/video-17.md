# Video 17: Observabilidad y monitoreo de sistemas

## Título
Observabilidad y monitoreo de sistemas

## 🧭 Punto de partida
Vienes de trabajar infraestructura, despliegue y entorno de ejecución. No vamos a repetirlo: lo usaremos como punto de partida para estudiar observabilidad y monitoreo de sistemas y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con seguridad, datos sensibles y privacidad.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Infraestructura, despliegue y entorno de ejecución](video-16.md)

[➡️ Video siguiente: Seguridad, datos sensibles y privacidad](video-18.md)

## 🎥 La situación que vamos a resolver
La fuente consultada para esta clase es 'Video 15: Observabilidad y monitoreo de sistemas'. En nuestro recorrido la conectamos con el tema 'Observabilidad y monitoreo de sistemas' porque queremos estudiar observabilidad y monitoreo de sistemas desde un problema real. La fuente plantea: La observabilidad es una capacidad esencial en sistemas modernos. Permite entender qué está sucediendo en producción, detectar fallos, identificar cuellos de botella y responder rápidamente ante anomalías. Si un sistema no es observable, el equipo trabaja a ciegas y la resolución de incidentes se vuelve más costosa.

La observabilidad no es solo activar logs; incluye métricas, trazabilidad, alertas y mecanismos para evaluar el comportamiento real del sistema. Cuando se diseña bien, ayuda a prevenir incidentes, entender la carga y tomar decisiones basadas en evidencia. En la plataforma logística, esto aparece cuando una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. Primero entenderemos la fuente y después construiremos la decisión.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar observabilidad y monitoreo de sistemas con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: La observabilidad es una capacidad esencial en sistemas modernos.

Ahora voy a separar contigo tres niveles: lo que la fuente afirma, el problema esencial que debemos resolver y las decisiones técnicas que podríamos tomar después. Si confundimos esos niveles, terminaremos usando una tecnología como respuesta a un problema que todavía no hemos definido.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta observabilidad y monitoreo de sistemas como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La observabilidad permite entender el comportamiento real del sistema.

Detente en la consecuencia de esta idea: La observabilidad permite entender el comportamiento real del sistema. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. Los logs, métricas y trazas son herramientas esenciales de diagnósticos.

Esta idea solo queda completa cuando podemos comprobarla. Los logs, métricas y trazas son herramientas esenciales de diagnósticos. Elige una prueba o métrica y explica qué resultado confirmaría o cuestionaría nuestra decisión sobre observabilidad y monitoreo de sistemas.

### 3. Un sistema difícil de monitorear es más riesgoso en producción.

Detente en la consecuencia de esta idea: Un sistema difícil de monitorear es más riesgoso en producción. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 4. La observabilidad es una decisión arquitectónica, no un detalle final.

Detente en la consecuencia de esta idea: La observabilidad es una decisión arquitectónica, no un detalle final. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 5. La capacidad de detectar y corregir fallos reduce impacto en usuarios y negocio.

Aquí quiero que mires el riesgo humano de esta idea. La capacidad de detectar y corregir fallos reduce impacto en usuarios y negocio. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

### 6. Un buen sistema comunica su estado de forma clara a quien lo opera.

Detente en la consecuencia de esta idea: Un buen sistema comunica su estado de forma clara a quien lo opera. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué tan claro es el estado actual de mi sistema en producción? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy monitoreando lo que realmente importa? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué indicadores me alertan antes de que se vuelva un problema grave? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🔀 Opciones para resolver observabilidad y monitoreo de sistemas

- **Opción A:** aplicar una solución sencilla dentro de la estructura actual, documentando sus límites.
- **Opción B:** introducir una separación o mecanismo especializado para proteger el riesgo principal de la fuente.

Compara ambas por costo inicial, calidad, operación, facilidad de cambio y evidencia disponible. Elige una solo después de explicar qué problema resuelve y qué costo aceptas.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. La fuente afirma que La observabilidad permite entender el comportamiento real del sistema.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La observabilidad es una parte central de la arquitectura porque permite entender, prevenir y corregir problemas antes de que se vuelvan críticos. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa observabilidad y monitoreo de sistemas en tus propias palabras y relaciónalo con esta fuente: La observabilidad es una capacidad esencial en sistemas modernos.
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

1. **¿Qué tan claro es el estado actual de mi sistema en producción?** Mi respuesta de partida es: La observabilidad permite entender el comportamiento real del sistema. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Estoy monitoreando lo que realmente importa?** Mi respuesta de partida es: Los logs, métricas y trazas son herramientas esenciales de diagnósticos. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Qué indicadores me alertan antes de que se vuelva un problema grave?** Mi respuesta de partida es: Un sistema difícil de monitorear es más riesgoso en producción. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar observabilidad y monitoreo de sistemas, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia seguridad, datos sensibles y privacidad.

## 🤔 Para pensar antes de continuar
- ¿Qué tan claro es el estado actual de mi sistema en producción?
- ¿Estoy monitoreando lo que realmente importa?
- ¿Qué indicadores me alertan antes de que se vuelva un problema grave?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 3: diseño y dominio. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
