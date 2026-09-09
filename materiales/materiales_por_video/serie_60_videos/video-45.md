# Video 45: API Gateway como capa de abstracción

## Título
API Gateway como capa de abstracción

## 🧭 Punto de partida
Vienes de trabajar migraciones de base de datos con flyway. No vamos a repetirlo: lo usaremos como punto de partida para estudiar api gateway como capa de abstracción y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con bounded context y context maps.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Migraciones de base de datos con Flyway](video-44.md)

[➡️ Video siguiente: Bounded context y context maps](video-46.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 14: DevOps, despliegue y automatización'. Este video conecta arquitectura con entrega continua y operación real. La forma en que se despliega una aplicación afecta directamente la estabilidad, velocidad y capacidad de innovación del equipo. Cuando el despliegue es manual, propenso a errores o difícil de repetir, la arquitectura se vuelve frágil incluso si el diseño técnico es bueno.

La automatización del despliegue, la integración continua, la orquestación y la infraestructura como código permiten que el sistema evolucione con menos riesgos. El video muestra que la arquitectura moderna no se limita a la aplicación, sino al flujo completo de entrega: código, integración, pruebas, despliegue, observabilidad y rollback. Esto hace que la calidad del sistema dependa también del proceso que lo lleva a producción. En la plataforma logística, esto aparece cuando un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar api gateway como capa de abstracción con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video conecta arquitectura con entrega continua y operación real. La forma en que se despliega una aplicación afecta directamente la estabilidad, velocidad y capacidad de innovación del equipo. Cuando el despliegue es manual, propenso a errores o difícil de repetir, la arquitectura se vuelve frágil incluso si el diseño técnico es bueno.

La automatización del despliegue, la integración continua, la orquestación y la infraestructura como código permiten que el sistema evolucione con menos riesgos. El video muestra que la arquitectura moderna no se limita a la aplicación, sino al flujo completo de entrega: código, integración, pruebas, despliegue, observabilidad y rollback. Esto hace que la calidad del sistema dependa también del proceso que lo lleva a producción.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciona esa situación con el proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Aquí aparece el verdadero trabajo arquitectónico. No basta con saber que existe un patrón, una tecnología o una práctica. Necesitamos saber qué problema resuelve en este contexto, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta api gateway como capa de abstracción como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. El despliegue es parte de la arquitectura, no una etapa separada.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 2. La automatización reduce errores humanos y acelera la entrega.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 3. La infraestructura debe ser reproducible y controlada.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 4. La calidad del proceso impacta la calidad del sistema.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 5. Un pipeline bien diseñado permite cambios más seguros y más frecuentes.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 6. La capacidad de rollback y recuperación es clave en entornos reales.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Mi despliegue es repetible y automatizado? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué tan rápido puedo revertir un cambio problemático? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy diseñando para entrega continua o para “una vez al mes” con riesgo mayor? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. La fuente afirma que El despliegue es parte de la arquitectura, no una etapa separada.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La arquitectura moderna integra desarrollo, operación y entrega. Un sistema no se considera bien diseñado si no puede entregarse, operar y evolucionar de manera segura y repetible. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa api gateway como capa de abstracción en tus propias palabras y relaciónalo con esta fuente: Este video conecta arquitectura con entrega continua y operación real.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Mi despliegue es repetible y automatizado?** Mi respuesta de partida es: El despliegue es parte de la arquitectura, no una etapa separada. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Qué tan rápido puedo revertir un cambio problemático?** Mi respuesta de partida es: La automatización reduce errores humanos y acelera la entrega. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Estoy diseñando para entrega continua o para “una vez al mes” con riesgo mayor?** Mi respuesta de partida es: La infraestructura debe ser reproducible y controlada. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar api gateway como capa de abstracción, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia bounded context y context maps.

## 🤔 Para pensar antes de continuar
- ¿Mi despliegue es repetible y automatizado?
- ¿Qué tan rápido puedo revertir un cambio problemático?
- ¿Estoy diseñando para entrega continua o para “una vez al mes” con riesgo mayor?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 4: implementación e integración. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
