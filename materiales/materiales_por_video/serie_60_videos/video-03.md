# Video 3: El arquitecto y la responsabilidad técnica

## Título
El arquitecto y la responsabilidad técnica

## 🧭 Punto de partida
Vienes de trabajar problema esencial y decisiones técnicas. No vamos a repetirlo: lo usaremos como punto de partida para estudiar el arquitecto y la responsabilidad técnica y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con negocio, usuarios y contexto.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Problema esencial y decisiones técnicas](video-02.md)

[➡️ Video siguiente: Negocio, usuarios y contexto](video-04.md)

## 🎥 La situación que vamos a resolver
La fuente consultada para esta clase es 'Video 3: Rol del arquitecto de software'. En nuestro recorrido la conectamos con el tema 'El arquitecto y la responsabilidad técnica' porque queremos estudiar el arquitecto y la responsabilidad técnica desde un problema real. La fuente plantea: En este video se redefine el rol del arquitecto, dejando atrás la idea de que solo dibuja diagramas. El arquitecto debe diseñar sistemas sólidos y sostenibles, simplificar la complejidad, cuestionar supuestos y negociar con distintos stakeholders. Además, tiene que entender que cada decisión técnica tiene consecuencias reales.

El trabajo del arquitecto no es imponer una solución elegante por gusto; es crear sistemas confiables, duraderos y bien pensados para el futuro. Esto implica abstraer lo esencial, priorizar la claridad, identificar riesgos y tomar decisiones con criterio técnico y de negocio. En la plataforma logística, esto aparece cuando la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. Primero entenderemos la fuente y después construiremos la decisión.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar el arquitecto y la responsabilidad técnica con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: En este video se redefine el rol del arquitecto, dejando atrás la idea de que solo dibuja diagramas.

Ahora voy a separar contigo tres niveles: lo que la fuente afirma, el problema esencial que debemos resolver y las decisiones técnicas que podríamos tomar después. Si confundimos esos niveles, terminaremos usando una tecnología como respuesta a un problema que todavía no hemos definido.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta el arquitecto y la responsabilidad técnica como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. El arquitecto no es solo un dibujante de diagramas.

Detente en la consecuencia de esta idea: El arquitecto no es solo un dibujante de diagramas. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. Debe abstraer la complejidad y simplificar lo esencial.

Detente en la consecuencia de esta idea: Debe abstraer la complejidad y simplificar lo esencial. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. Tiene que cuestionar supuestos, tanto técnicos como de negocio.

Detente en la consecuencia de esta idea: Tiene que cuestionar supuestos, tanto técnicos como de negocio. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 4. Debe negociar con usuarios, directivos y equipo.

Detente en la consecuencia de esta idea: Debe negociar con usuarios, directivos y equipo. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 5. Su objetivo es construir sistemas confiables, sostenibles y con visión de futuro.

Detente en la consecuencia de esta idea: Su objetivo es construir sistemas confiables, sostenibles y con visión de futuro. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. El arquitecto conecta negocio, tecnología y equipos.

Detente en la consecuencia de esta idea: El arquitecto conecta negocio, tecnología y equipos. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué tan claro es mi papel como arquitecto o líder técnico en el proyecto? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy cuestionando suposiciones o aceptando decisiones sin analizar consecuencias? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Cómo puedo comunicar mejor la arquitectura a los diferentes actores del proyecto? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🔀 Opciones para resolver el arquitecto y la responsabilidad técnica

- **Opción A:** aplicar una solución sencilla dentro de la estructura actual, documentando sus límites.
- **Opción B:** introducir una separación o mecanismo especializado para proteger el riesgo principal de la fuente.

Compara ambas por costo inicial, calidad, operación, facilidad de cambio y evidencia disponible. Elige una solo después de explicar qué problema resuelve y qué costo aceptas.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. La fuente afirma que El arquitecto no es solo un dibujante de diagramas.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: El papel del arquitecto es más amplio que la solución técnica: es diseñar sistemas con estrategia, criterio y responsabilidad. La arquitectura sirve para transformar complejidad en claridad. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa el arquitecto y la responsabilidad técnica en tus propias palabras y relaciónalo con esta fuente: En este video se redefine el rol del arquitecto, dejando atrás la idea de que solo dibuja diagramas.
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

1. **¿Qué tan claro es mi papel como arquitecto o líder técnico en el proyecto?** Mi respuesta de partida es: El arquitecto no es solo un dibujante de diagramas. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Estoy cuestionando suposiciones o aceptando decisiones sin analizar consecuencias?** Mi respuesta de partida es: Debe abstraer la complejidad y simplificar lo esencial. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Cómo puedo comunicar mejor la arquitectura a los diferentes actores del proyecto?** Mi respuesta de partida es: Tiene que cuestionar supuestos, tanto técnicos como de negocio. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar el arquitecto y la responsabilidad técnica, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia negocio, usuarios y contexto.

## 🤔 Para pensar antes de continuar
- ¿Qué tan claro es mi papel como arquitecto o líder técnico en el proyecto?
- ¿Estoy cuestionando suposiciones o aceptando decisiones sin analizar consecuencias?
- ¿Cómo puedo comunicar mejor la arquitectura a los diferentes actores del proyecto?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 1: diagnóstico y contexto arquitectónico. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
