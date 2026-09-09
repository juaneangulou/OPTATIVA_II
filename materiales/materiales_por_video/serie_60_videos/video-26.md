# Video 26: Principios de diseño y fundamentos de estructura

## Título
Principios de diseño y fundamentos de estructura

## 🧭 Punto de partida
Vienes de trabajar escalabilidad, seguridad y ética. No vamos a repetirlo: lo usaremos como punto de partida para estudiar principios de diseño y fundamentos de estructura y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con acoplamiento, cohesión y calidad estructural.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Escalabilidad, seguridad y ética](video-25.md)

[➡️ Video siguiente: Acoplamiento, cohesión y calidad estructural](video-27.md)

## 🎥 La situación que vamos a resolver
La fuente consultada para esta clase es 'Video 8: Fundamentos de diseño y principios de arquitectura'. En nuestro recorrido la conectamos con el tema 'Principios de diseño y fundamentos de estructura' porque queremos estudiar principios de diseño y fundamentos de estructura desde un problema real. La fuente plantea: Este video presenta los fundamentos del diseño arquitectónico: cómo una solución técnica debe estructurarse para ser clara, sostenible y adaptable. La arquitectura no se basa solo en elegir herramientas, sino en aplicar principios que guíen la organización del sistema. Entre esos principios están la modularidad, la separación de responsabilidades, la reutilización con sentido y la reducción del acoplamiento.

La idea central es que un sistema bien diseñado no solo funciona, sino que es más fácil de entender, mantener y evolucionar. Los principios de arquitectura sirven como brújula para tomar decisiones con criterio, especialmente cuando el proyecto crece en complejidad. En la plataforma logística, esto aparece cuando pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. Primero entenderemos la fuente y después construiremos la decisión.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar principios de diseño y fundamentos de estructura con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video presenta los fundamentos del diseño arquitectónico: cómo una solución técnica debe estructurarse para ser clara, sostenible y adaptable.

Ahora voy a separar contigo tres niveles: lo que la fuente afirma, el problema esencial que debemos resolver y las decisiones técnicas que podríamos tomar después. Si confundimos esos niveles, terminaremos usando una tecnología como respuesta a un problema que todavía no hemos definido.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta principios de diseño y fundamentos de estructura como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. El diseño arquitectónico no es un detalle opcional.

Detente en la consecuencia de esta idea: El diseño arquitectónico no es un detalle opcional. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. Los principios ayudan a sostener decisiones de largo plazo.

Detente en la consecuencia de esta idea: Los principios ayudan a sostener decisiones de largo plazo. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. La modularidad mejora la claridad y la evolución del sistema.

Detente en la consecuencia de esta idea: La modularidad mejora la claridad y la evolución del sistema. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 4. La separación de responsabilidades reduce complejidad.

Aquí quiero que mires el riesgo humano de esta idea. La separación de responsabilidades reduce complejidad. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

### 5. Un buen diseño facilita cambios sin romper el sistema completo.

Detente en la consecuencia de esta idea: Un buen diseño facilita cambios sin romper el sistema completo. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. La arquitectura debe crear orden en medio de la complejidad.

Detente en la consecuencia de esta idea: La arquitectura debe crear orden en medio de la complejidad. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué parte de mi sistema tiene responsabilidades mezcladas? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué principio arquitectónico me está faltando aplicar? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy diseñando para la claridad o para la improvisación? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🔀 Opciones para resolver principios de diseño y fundamentos de estructura

- **Opción A:** aplicar una solución sencilla dentro de la estructura actual, documentando sus límites.
- **Opción B:** introducir una separación o mecanismo especializado para proteger el riesgo principal de la fuente.

Compara ambas por costo inicial, calidad, operación, facilidad de cambio y evidencia disponible. Elige una solo después de explicar qué problema resuelve y qué costo aceptas.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. La fuente afirma que El diseño arquitectónico no es un detalle opcional.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: Los principios de diseño son la base para crear sistemas más claros, más sostenibles y más fáciles de hacer crecer con seguridad. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa principios de diseño y fundamentos de estructura en tus propias palabras y relaciónalo con esta fuente: Este video presenta los fundamentos del diseño arquitectónico: cómo una solución técnica debe estructurarse para ser clara, sostenible y adaptable.
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

1. **¿Qué parte de mi sistema tiene responsabilidades mezcladas?** Mi respuesta de partida es: El diseño arquitectónico no es un detalle opcional. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Qué principio arquitectónico me está faltando aplicar?** Mi respuesta de partida es: Los principios ayudan a sostener decisiones de largo plazo. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Estoy diseñando para la claridad o para la improvisación?** Mi respuesta de partida es: La modularidad mejora la claridad y la evolución del sistema. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar principios de diseño y fundamentos de estructura, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia acoplamiento, cohesión y calidad estructural.

## 🤔 Para pensar antes de continuar
- ¿Qué parte de mi sistema tiene responsabilidades mezcladas?
- ¿Qué principio arquitectónico me está faltando aplicar?
- ¿Estoy diseñando para la claridad o para la improvisación?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 3: diseño y dominio. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
