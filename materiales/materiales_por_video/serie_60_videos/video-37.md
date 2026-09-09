# Video 37: Agentes de IA revisando código en GitHub

## Título
Agentes de IA revisando código en GitHub

## 🧭 Punto de partida
Vienes de trabajar quarto como documentación viva. No vamos a repetirlo: lo usaremos como punto de partida para estudiar agentes de ia revisando código en github y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con estructura del archivo architecture.md.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Quarto como documentación viva](video-36.md)

[➡️ Video siguiente: Estructura del archivo Architecture.md](video-38.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 6: Arquitectura y decisiones de diseño'. En este video se enfoca en la idea de que la arquitectura no es solo un conjunto de componentes, sino una serie de decisiones que ordenan cómo funciona un sistema. Cada elección de diseño tiene consecuencias sobre mantenibilidad, complejidad, acoplamiento, tiempo de entrega y calidad general. El arquitecto no solo define una estructura; define un conjunto de reglas que guían el crecimiento del sistema.

La clave es entender que las decisiones arquitectónicas no se toman solo por gustos técnicos. Se basan en restricciones del negocio, capacidades del equipo, objetivos de evolución, riesgos y costos. El video muestra que una arquitectura sana toma decisiones con intención y no por accidente. Cuando el diseño está guiado por principios claros, el sistema avanza sin convertirse en una estructura caótica. En la plataforma logística, esto aparece cuando un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar agentes de ia revisando código en github con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: En este video se enfoca en la idea de que la arquitectura no es solo un conjunto de componentes, sino una serie de decisiones que ordenan cómo funciona un sistema. Cada elección de diseño tiene consecuencias sobre mantenibilidad, complejidad, acoplamiento, tiempo de entrega y calidad general. El arquitecto no solo define una estructura; define un conjunto de reglas que guían el crecimiento del sistema.

La clave es entender que las decisiones arquitectónicas no se toman solo por gustos técnicos. Se basan en restricciones del negocio, capacidades del equipo, objetivos de evolución, riesgos y costos. El video muestra que una arquitectura sana toma decisiones con intención y no por accidente. Cuando el diseño está guiado por principios claros, el sistema avanza sin convertirse en una estructura caótica.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciona esa situación con el proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Aquí aparece el verdadero trabajo arquitectónico. No basta con saber que existe un patrón, una tecnología o una práctica. Necesitamos saber qué problema resuelve en este contexto, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta agentes de ia revisando código en github como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La arquitectura es un conjunto de decisiones con impacto a largo plazo.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 2. Cada diseño tiene beneficios y costos asociados.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 3. El acoplamiento y la cohesión son criterios clave para evaluar un diseño.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 4. Un sistema bien diseñado reduce la fricción para cambiar y escalar.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 5. La arquitectura debe ser explícita, no improvisada.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 6. Las decisiones deben estar alineadas con objetivos de negocio y capacidad del equipo.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué decisiones de diseño están guiando mi sistema hoy? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy tomando decisiones por intuición o por un criterio explícito? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué parte del sistema está empezando a volverse rígida o difícil de modificar? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. La fuente afirma que La arquitectura es un conjunto de decisiones con impacto a largo plazo.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: Una buena arquitectura no aparece por azar; se construye deliberadamente. El valor de la arquitectura radica en la claridad con la que guía el crecimiento del sistema y en la capacidad de soportar decisiones futuras sin destruir la base actual. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa agentes de ia revisando código en github en tus propias palabras y relaciónalo con esta fuente: En este video se enfoca en la idea de que la arquitectura no es solo un conjunto de componentes, sino una serie de decisiones que ordenan cómo funciona un sistema.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué decisiones de diseño están guiando mi sistema hoy?** Mi respuesta de partida es: La arquitectura es un conjunto de decisiones con impacto a largo plazo. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Estoy tomando decisiones por intuición o por un criterio explícito?** Mi respuesta de partida es: Cada diseño tiene beneficios y costos asociados. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Qué parte del sistema está empezando a volverse rígida o difícil de modificar?** Mi respuesta de partida es: El acoplamiento y la cohesión son criterios clave para evaluar un diseño. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar agentes de ia revisando código en github, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia estructura del archivo architecture.md.

## 🤔 Para pensar antes de continuar
- ¿Qué decisiones de diseño están guiando mi sistema hoy?
- ¿Estoy tomando decisiones por intuición o por un criterio explícito?
- ¿Qué parte del sistema está empezando a volverse rígida o difícil de modificar?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 4: implementación e integración. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
