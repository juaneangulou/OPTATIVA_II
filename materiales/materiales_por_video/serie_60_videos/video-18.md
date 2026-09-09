# Video 18: Seguridad, datos sensibles y privacidad

## Título
Seguridad, datos sensibles y privacidad

## 🧭 Punto de partida
Vienes de trabajar observabilidad y monitoreo de sistemas. No vamos a repetirlo: lo usaremos como punto de partida para estudiar seguridad, datos sensibles y privacidad y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con testing y validación de arquitectura.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Observabilidad y monitoreo de sistemas](video-17.md)

[➡️ Video siguiente: Testing y validación de arquitectura](video-19.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 16: Seguridad, datos sensibles y privacidad'. Este video refuerza la idea de que la seguridad debe integrarse desde el inicio del diseño. No se trata solo de proteger la aplicación frente a intrusos, sino también de gestionar adecuadamente datos sensibles, permisos de acceso y riesgos derivados del tratamiento de información. Cualquier sistema que maneje datos valiosos debe diseñarse con principios de privacidad, control y minimización.

La arquitectura debe prestar atención a qué información guarda, cómo la protege y quién puede acceder a ella. Cuando se ignora esto, se generan riesgos reales tanto para la empresa como para las personas que usan el sistema. En la plataforma logística, esto aparece cuando una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar seguridad, datos sensibles y privacidad con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video refuerza la idea de que la seguridad debe integrarse desde el inicio del diseño. No se trata solo de proteger la aplicación frente a intrusos, sino también de gestionar adecuadamente datos sensibles, permisos de acceso y riesgos derivados del tratamiento de información. Cualquier sistema que maneje datos valiosos debe diseñarse con principios de privacidad, control y minimización.

La arquitectura debe prestar atención a qué información guarda, cómo la protege y quién puede acceder a ella. Cuando se ignora esto, se generan riesgos reales tanto para la empresa como para las personas que usan el sistema.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciona esa situación con el proyecto: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. Aquí aparece el verdadero trabajo arquitectónico. No basta con saber que existe un patrón, una tecnología o una práctica. Necesitamos saber qué problema resuelve en este contexto, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta seguridad, datos sensibles y privacidad como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La seguridad debe estar integrada al diseño, no añadida al final.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 2. Los datos sensibles requieren más criterios de control y protección.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 3. La privacidad es parte del valor del sistema.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 4. Un sistema debe minimizar exposición de información innecesaria.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 5. El diseño debe recordar quién tiene acceso y bajo qué condiciones.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 6. La confianza del usuario depende del manejo responsable de datos.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué datos sensibles maneja mi sistema? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy reduciendo la exposición innecesaria de información? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Mis controles de acceso y seguridad están alineados con el riesgo real? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. La fuente afirma que La seguridad debe estar integrada al diseño, no añadida al final.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La seguridad y la privacidad no son requisitos secundarios: son elementos fundamentales de una arquitectura responsable y confiable. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa seguridad, datos sensibles y privacidad en tus propias palabras y relaciónalo con esta fuente: Este video refuerza la idea de que la seguridad debe integrarse desde el inicio del diseño.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué datos sensibles maneja mi sistema?** Mi respuesta de partida es: La seguridad debe estar integrada al diseño, no añadida al final. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Estoy reduciendo la exposición innecesaria de información?** Mi respuesta de partida es: Los datos sensibles requieren más criterios de control y protección. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Mis controles de acceso y seguridad están alineados con el riesgo real?** Mi respuesta de partida es: La privacidad es parte del valor del sistema. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar seguridad, datos sensibles y privacidad, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia testing y validación de arquitectura.

## 🤔 Para pensar antes de continuar
- ¿Qué datos sensibles maneja mi sistema?
- ¿Estoy reduciendo la exposición innecesaria de información?
- ¿Mis controles de acceso y seguridad están alineados con el riesgo real?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 3: diseño y dominio. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
