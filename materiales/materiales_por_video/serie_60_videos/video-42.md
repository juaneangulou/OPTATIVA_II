# Video 42: Métricas cuantitativas para evaluar arquitecturas

## Título
Métricas cuantitativas para evaluar arquitecturas

## 🧭 Punto de partida
Vienes de trabajar premortem como guía de pruebas de arquitectura. No vamos a repetirlo: lo usaremos como punto de partida para estudiar métricas cuantitativas para evaluar arquitecturas y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con strangler fig para migraciones.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Premortem como guía de pruebas de arquitectura](video-41.md)

[➡️ Video siguiente: Strangler Fig para migraciones](video-43.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 10: Integración y contratos de API'. La mayoría de sistemas modernos no existen aislados: dependen de servicios, clientes, proveedores y otras aplicaciones. Por eso, la capacidad de integrar componentes de forma clara y segura es crucial. Este video habla de las APIs como contratos entre sistemas: si esos contratos son ambiguos o cambian sin control, el sistema entera se vuelve frágil y difícil de mantener.

Se enfatiza la idea de que una API no es solo una ruta o un endpoint; es una interfaz formal de comunicación entre partes. Cuando se diseña bien, facilita la colaboración, reduce errores y mejora la evolución del sistema. Cuando se diseña mal, genera compatibilidad, dependencia y cambios difíciles de gestionar. En la plataforma logística, esto aparece cuando durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar métricas cuantitativas para evaluar arquitecturas con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: La mayoría de sistemas modernos no existen aislados: dependen de servicios, clientes, proveedores y otras aplicaciones.

La fuente desarrolla esta situación con más detalle en el bloque anterior. Ahora quiero que hagamos algo distinto: separar el problema esencial de los detalles técnicos que podríamos elegir después.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta métricas cuantitativas para evaluar arquitecturas como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. Las APIs son contratos que facilitan la integración entre sistemas.

En esta idea nos interesa el límite entre componentes. Las APIs son contratos que facilitan la integración entre sistemas. Dibuja quién consume la información, qué contrato necesita y qué cambio podría romper al consumidor.

### 2. Cambios sin versionado pueden romper dependencias.

Detente en la consecuencia de esta idea: Cambios sin versionado pueden romper dependencias. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. Debe existir claridad en formatos, validaciones, errores y semántica.

Detente en la consecuencia de esta idea: Debe existir claridad en formatos, validaciones, errores y semántica. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 4. La integración eficiente reduce riesgos de acoplamiento y mejora la escalabilidad.

Ahora llévala a un escenario de crecimiento. La integración eficiente reduce riesgos de acoplamiento y mejora la escalabilidad. Imagina que aumenta el tráfico: identifica el primer cuello de botella y decide qué medirías antes de añadir infraestructura.

### 5. El diseño de APIs debe considerar estabilidad y evolución.

Ahora llévala a un escenario de crecimiento. El diseño de APIs debe considerar estabilidad y evolución. Imagina que aumenta el tráfico: identifica el primer cuello de botella y decide qué medirías antes de añadir infraestructura.

### 6. La buena arquitectura comunica bien entre servicios, equipos y aplicaciones.

En esta idea nos interesa el límite entre componentes. La buena arquitectura comunica bien entre servicios, equipos y aplicaciones. Dibuja quién consume la información, qué contrato necesita y qué cambio podría romper al consumidor.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Mis APIs están documentadas y versionadas de forma clara? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué pasa si un cliente usa una versión anterior? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy diseñando para cambio controlado o para improvisación constante? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. La fuente afirma que Las APIs son contratos que facilitan la integración entre sistemas.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: Las integraciones son una parte central de la arquitectura moderna. Si las APIs no están bien definidas, la evolución del sistema se vuelve costosa y frágil. Diseñar contratos claros es una capacidad esencial del arquitecto. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa métricas cuantitativas para evaluar arquitecturas en tus propias palabras y relaciónalo con esta fuente: La mayoría de sistemas modernos no existen aislados: dependen de servicios, clientes, proveedores y otras aplicaciones.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Mis APIs están documentadas y versionadas de forma clara?** Mi respuesta de partida es: Las APIs son contratos que facilitan la integración entre sistemas. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Qué pasa si un cliente usa una versión anterior?** Mi respuesta de partida es: Cambios sin versionado pueden romper dependencias. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Estoy diseñando para cambio controlado o para improvisación constante?** Mi respuesta de partida es: Debe existir claridad en formatos, validaciones, errores y semántica. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar métricas cuantitativas para evaluar arquitecturas, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia strangler fig para migraciones.

## 🤔 Para pensar antes de continuar
- ¿Mis APIs están documentadas y versionadas de forma clara?
- ¿Qué pasa si un cliente usa una versión anterior?
- ¿Estoy diseñando para cambio controlado o para improvisación constante?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 5: pruebas, operación y defensa final. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
