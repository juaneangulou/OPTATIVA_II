# Video 27: Acoplamiento, cohesión y calidad estructural

## Título
Acoplamiento, cohesión y calidad estructural

## 🧭 Punto de partida
Vienes de trabajar principios de diseño y fundamentos de estructura. No vamos a repetirlo: lo usaremos como punto de partida para estudiar acoplamiento, cohesión y calidad estructural y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con modelado de dominios y límites de contexto.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Principios de diseño y fundamentos de estructura](video-26.md)

[➡️ Video siguiente: Modelado de dominios y límites de contexto](video-28.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 9: Acoplamiento, cohesión y calidad estructural'. Este video explica dos conceptos centrales en arquitectura: acoplamiento y cohesión. El acoplamiento mide cuán dependientes son componentes entre sí; la cohesión mide qué tan relacionadas están las responsabilidades dentro de un mismo módulo o servicio. La mejor arquitectura busca baja dependencia entre partes y alta claridad dentro de cada parte.

Cuando el acoplamiento es alto, hacer cambios implica romper varias piezas del sistema. Cuando la cohesión es baja, una entidad se vuelve confusa y difícil de mantener. La calidad estructural del software se mejora cuando se reducen dependencias innecesarias y se ordenan bien las responsabilidades. En la plataforma logística, esto aparece cuando pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar acoplamiento, cohesión y calidad estructural con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video explica dos conceptos centrales en arquitectura: acoplamiento y cohesión. El acoplamiento mide cuán dependientes son componentes entre sí; la cohesión mide qué tan relacionadas están las responsabilidades dentro de un mismo módulo o servicio. La mejor arquitectura busca baja dependencia entre partes y alta claridad dentro de cada parte.

Cuando el acoplamiento es alto, hacer cambios implica romper varias piezas del sistema. Cuando la cohesión es baja, una entidad se vuelve confusa y difícil de mantener. La calidad estructural del software se mejora cuando se reducen dependencias innecesarias y se ordenan bien las responsabilidades.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciona esa situación con el proyecto: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. Aquí aparece el verdadero trabajo arquitectónico. No basta con saber que existe un patrón, una tecnología o una práctica. Necesitamos saber qué problema resuelve en este contexto, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta acoplamiento, cohesión y calidad estructural como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. El acoplamiento alto genera fragilidad.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 2. La cohesión alta mejora claridad y mantenibilidad.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 3. La arquitectura debe disminuir dependencias innecesarias.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 4. Un sistema con responsabilidades bien definidas es más fácil de evolucionar.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 5. La calidad estructural se refleja en cómo se organizan los componentes.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 6. Un buen diseño minimiza efectos colaterales de un cambio.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué tan acoplado está mi sistema en este momento? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué modulos tienen demasiadas responsabilidades mezcladas? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué cambio actual rompe más de lo necesario por dependencias internas? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. La fuente afirma que El acoplamiento alto genera fragilidad.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La calidad estructural de un sistema está marcada por la forma en que se separan sus responsabilidades y cómo se gestionan sus dependencias. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa acoplamiento, cohesión y calidad estructural en tus propias palabras y relaciónalo con esta fuente: Este video explica dos conceptos centrales en arquitectura: acoplamiento y cohesión.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué tan acoplado está mi sistema en este momento?** Mi respuesta de partida es: El acoplamiento alto genera fragilidad. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Qué modulos tienen demasiadas responsabilidades mezcladas?** Mi respuesta de partida es: La cohesión alta mejora claridad y mantenibilidad. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Qué cambio actual rompe más de lo necesario por dependencias internas?** Mi respuesta de partida es: La arquitectura debe disminuir dependencias innecesarias. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar acoplamiento, cohesión y calidad estructural, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia modelado de dominios y límites de contexto.

## 🤔 Para pensar antes de continuar
- ¿Qué tan acoplado está mi sistema en este momento?
- ¿Qué modulos tienen demasiadas responsabilidades mezcladas?
- ¿Qué cambio actual rompe más de lo necesario por dependencias internas?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 3: diseño y dominio. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
