# Video 43: Strangler Fig para migraciones

## Título
Strangler Fig para migraciones

## 🧭 Punto de partida
Vienes de trabajar métricas cuantitativas para evaluar arquitecturas. No vamos a repetirlo: lo usaremos como punto de partida para estudiar strangler fig para migraciones y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con migraciones de base de datos con flyway.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Métricas cuantitativas para evaluar arquitecturas](video-42.md)

[➡️ Video siguiente: Migraciones de base de datos con Flyway](video-44.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 12: Datos y almacenamiento'. El video presenta la importancia decisiva de la estrategia de datos dentro de la arquitectura. Una aplicación no es solo lógica de negocio; también es un sistema de lectura, escritura, consulta y persistencia. La forma en que se almacenan los datos afecta directamente rendimiento, consistencia, recuperación, costos, y capacidad de evolución. Elegir una base de datos o un patrón de almacenamiento equivale a definir parte del comportamiento del sistema.

Se enfatiza que no existe una base de datos “mejor” en abstracto, sino una opción más adecuada para cada problema. La arquitectura debe evaluar volumen, tipos de consulta, consistencia requerida, latencia, integridad y costo operativo. A partir de ahí, se pueden elegir modelos relacionales, NoSQL, colas, caché o arquitecturas híbridas. En la plataforma logística, esto aparece cuando un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar strangler fig para migraciones con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: El video presenta la importancia decisiva de la estrategia de datos dentro de la arquitectura. Una aplicación no es solo lógica de negocio; también es un sistema de lectura, escritura, consulta y persistencia. La forma en que se almacenan los datos afecta directamente rendimiento, consistencia, recuperación, costos, y capacidad de evolución. Elegir una base de datos o un patrón de almacenamiento equivale a definir parte del comportamiento del sistema.

Se enfatiza que no existe una base de datos “mejor” en abstracto, sino una opción más adecuada para cada problema. La arquitectura debe evaluar volumen, tipos de consulta, consistencia requerida, latencia, integridad y costo operativo. A partir de ahí, se pueden elegir modelos relacionales, NoSQL, colas, caché o arquitecturas híbridas.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciona esa situación con el proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Aquí aparece el verdadero trabajo arquitectónico. No basta con saber que existe un patrón, una tecnología o una práctica. Necesitamos saber qué problema resuelve en este contexto, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta strangler fig para migraciones como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La estrategia de datos influye directamente en la arquitectura.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 2. No todas las bases de datos resuelven el mismo tipo de problema.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 3. El almacenamiento debe obedecer al comportamiento real del negocio.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 4. Rendimiento, consistencia y costos son variables que se deben balancear.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 5. Los datos son un activo crítico, no un detalle técnico.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 6. El diseño de persistencia define la evolución futura del sistema.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué tipo de consultas y volumen real tiene mi sistema? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy priorizando velocidad de desarrollo sobre sostenibilidad de datos? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿La estrategia actual de persistencia sigue siendo adecuada si el sistema crece? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. La fuente afirma que La estrategia de datos influye directamente en la arquitectura.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La información es el corazón del sistema. Un diseño arquitectónico sólido toma decisiones inteligentes sobre cómo almacenar, consultar, proteger y evolucionar los datos, porque eso impacta el resto de la solución. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa strangler fig para migraciones en tus propias palabras y relaciónalo con esta fuente: El video presenta la importancia decisiva de la estrategia de datos dentro de la arquitectura.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué tipo de consultas y volumen real tiene mi sistema?** Mi respuesta de partida es: La estrategia de datos influye directamente en la arquitectura. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Estoy priorizando velocidad de desarrollo sobre sostenibilidad de datos?** Mi respuesta de partida es: No todas las bases de datos resuelven el mismo tipo de problema. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿La estrategia actual de persistencia sigue siendo adecuada si el sistema crece?** Mi respuesta de partida es: El almacenamiento debe obedecer al comportamiento real del negocio. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar strangler fig para migraciones, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia migraciones de base de datos con flyway.

## 🤔 Para pensar antes de continuar
- ¿Qué tipo de consultas y volumen real tiene mi sistema?
- ¿Estoy priorizando velocidad de desarrollo sobre sostenibilidad de datos?
- ¿La estrategia actual de persistencia sigue siendo adecuada si el sistema crece?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 4: implementación e integración. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
