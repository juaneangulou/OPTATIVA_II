# Video 31: Cómo analizar una licitación real con IA

## Título
Cómo analizar una licitación real con IA

## 🧭 Punto de partida
Vienes de trabajar intuición vs método en arquitectura de software. No vamos a repetirlo: lo usaremos como punto de partida para estudiar cómo analizar una licitación real con ia y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con monorepos con pantsbuild en proyectos reales.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Intuición vs método en arquitectura de software](video-30.md)

[➡️ Video siguiente: Monorepos con Pantsbuild en proyectos reales](video-32.md)

## 🎥 La situación que vamos a resolver
La fuente consultada para esta clase es 'Video 2: Del código funcional a la solución sostenible'. En nuestro recorrido la conectamos con el tema 'Cómo analizar una licitación real con IA' porque queremos estudiar cómo analizar una licitación real con ia desde un problema real. La fuente plantea: Este video enfatiza el cambio de mentalidad que ocurre cuando un desarrollador deja de pensar solo en entregar una funcionalidad rápida y empieza a pensar en la calidad del sistema completo. El objetivo ya no es solo que el código compile o que la funcionalidad funcione, sino que el sistema pueda evolucionar, soportar cambios y ser mantenido por más personas.

La diferencia entre un código funcional y una solución sostenible radica en la capacidad de estructurar el problema. Cuando se ignora la arquitectura, el sistema suele volverse difícil de entender, frágil ante cambios y costoso de mantener. El video presenta esta transición como un paso importante en la carrera profesional: de ser alguien que resuelve tareas puntuales a alguien que diseña soluciones con visión de producto y negocio. En la plataforma logística, esto aparece cuando un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Primero entenderemos la fuente y después construiremos la decisión.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar cómo analizar una licitación real con ia con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video enfatiza el cambio de mentalidad que ocurre cuando un desarrollador deja de pensar solo en entregar una funcionalidad rápida y empieza a pensar en la calidad del sistema completo.

Ahora voy a separar contigo tres niveles: lo que la fuente afirma, el problema esencial que debemos resolver y las decisiones técnicas que podríamos tomar después. Si confundimos esos niveles, terminaremos usando una tecnología como respuesta a un problema que todavía no hemos definido.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta cómo analizar una licitación real con ia como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. Un sistema que funciona puede seguir siendo una mala solución si no está bien diseñado.

Detente en la consecuencia de esta idea: Un sistema que funciona puede seguir siendo una mala solución si no está bien diseñado. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. La mantenibilidad es una dimensión clave del valor de una arquitectura.

Detente en la consecuencia de esta idea: La mantenibilidad es una dimensión clave del valor de una arquitectura. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. El diseño debe facilitar cambios futuros y no solo la entrega inicial.

Detente en la consecuencia de esta idea: El diseño debe facilitar cambios futuros y no solo la entrega inicial. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 4. Los problemas reales aparecen cuando el software crece en complejidad, usuarios, reglas de negocio y dependencias.

Aquí vamos a buscar la regla del negocio. Los problemas reales aparecen cuando el software crece en complejidad, usuarios, reglas de negocio y dependencias. Escribe qué objeto o módulo debería protegerla y qué error queremos impedir aunque cambie la base de datos o la interfaz.

### 5. El arquitecto debe pensar en el sistema como un conjunto de decisiones sostenibles, no solo como una colección de features.

Detente en la consecuencia de esta idea: El arquitecto debe pensar en el sistema como un conjunto de decisiones sostenibles, no solo como una colección de features. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. El código limpio no es un fin en sí mismo; es una herramienta para soportar la evolución del negocio.

Detente en la consecuencia de esta idea: El código limpio no es un fin en sí mismo; es una herramienta para soportar la evolución del negocio. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué tan sostenible es la solución que estoy construyendo hoy? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué parte del sistema es difícil de cambiar y por qué? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy optimizando para el presente o para la evolución futura? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🔀 Opciones para resolver cómo analizar una licitación real con ia

- **Opción A:** aplicar una solución sencilla dentro de la estructura actual, documentando sus límites.
- **Opción B:** introducir una separación o mecanismo especializado para proteger el riesgo principal de la fuente.

Compara ambas por costo inicial, calidad, operación, facilidad de cambio y evidencia disponible. Elige una solo después de explicar qué problema resuelve y qué costo aceptas.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. La fuente afirma que Un sistema que funciona puede seguir siendo una mala solución si no está bien diseñado.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: El salto del “código que funciona” al “sistema que sobrevive” es lo que marca la diferencia entre un desarrollador ordinario y un arquitecto de software. El valor no está solo en resolver el problema del momento, sino en construir una base que permita seguir creciendo sin perder calidad. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa cómo analizar una licitación real con ia en tus propias palabras y relaciónalo con esta fuente: Este video enfatiza el cambio de mentalidad que ocurre cuando un desarrollador deja de pensar solo en entregar una funcionalidad rápida y empieza a pensar en la calidad del sistema completo.
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

1. **¿Qué tan sostenible es la solución que estoy construyendo hoy?** Mi respuesta de partida es: Un sistema que funciona puede seguir siendo una mala solución si no está bien diseñado. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Qué parte del sistema es difícil de cambiar y por qué?** Mi respuesta de partida es: La mantenibilidad es una dimensión clave del valor de una arquitectura. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Estoy optimizando para el presente o para la evolución futura?** Mi respuesta de partida es: El diseño debe facilitar cambios futuros y no solo la entrega inicial. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar cómo analizar una licitación real con ia, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia monorepos con pantsbuild en proyectos reales.

## 🤔 Para pensar antes de continuar
- ¿Qué tan sostenible es la solución que estoy construyendo hoy?
- ¿Qué parte del sistema es difícil de cambiar y por qué?
- ¿Estoy optimizando para el presente o para la evolución futura?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 4: implementación e integración. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
