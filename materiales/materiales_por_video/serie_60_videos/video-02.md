# Video 2: Problema esencial y decisiones técnicas

## Título
Problema esencial y decisiones técnicas

## 🧭 Punto de partida
Vienes de trabajar decisiones de arquitectura y consecuencias reales. No vamos a repetirlo: lo usaremos como punto de partida para estudiar problema esencial y decisiones técnicas y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con el arquitecto y la responsabilidad técnica.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Decisiones de arquitectura y consecuencias reales](video-01.md)

[➡️ Video siguiente: El arquitecto y la responsabilidad técnica](video-03.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 2: ¿Por qué importa la arquitectura?'. Este video responde una pregunta central: ¿por qué la arquitectura de software es importante si al final un sistema solo necesita funcionar? La respuesta es que un sistema no se mide solo por su funcionamiento inmediato, sino por su capacidad de crecer, proteger datos, ser usable y responder a nuevas necesidades sin romperse.

La arquitectura influye en varios aspectos del software: escalabilidad, seguridad, accesibilidad, privacidad y ética. Si un sistema está mal diseñado, puede funcionar al inicio y luego volverse difícil de mantener, poco seguro y muy costoso de evolucionar. La arquitectura es la diferencia entre un producto resistente y uno frágil. En la plataforma logística, esto aparece cuando la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar problema esencial y decisiones técnicas con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video responde una pregunta central: ¿por qué la arquitectura de software es importante si al final un sistema solo necesita funcionar? La respuesta es que un sistema no se mide solo por su funcionamiento inmediato, sino por su capacidad de crecer, proteger datos, ser usable y responder a nuevas necesidades sin romperse.

La arquitectura influye en varios aspectos del software: escalabilidad, seguridad, accesibilidad, privacidad y ética. Si un sistema está mal diseñado, puede funcionar al inicio y luego volverse difícil de mantener, poco seguro y muy costoso de evolucionar. La arquitectura es la diferencia entre un producto resistente y uno frágil.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciona esa situación con el proyecto: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. Aquí aparece el verdadero trabajo arquitectónico. No basta con saber que existe un patrón, una tecnología o una práctica. Necesitamos saber qué problema resuelve en este contexto, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta problema esencial y decisiones técnicas como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La arquitectura determina el futuro del sistema.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 2. Un sistema puede trabajar hoy y fallar mañana si no está bien diseñado.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 3. La escalabilidad implica crecer sin perder rendimiento ni estabilidad.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 4. La seguridad y la privacidad son decisiones de diseño, no de última hora.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 5. La accesibilidad y la ética forman parte del valor del software.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

### 6. Lo que se decide al diseñar un sistema afecta su éxito y su impacto social.

Te propongo que no la leas como una frase para memorizar. Llévala al caso: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. Pregúntate qué parte del sistema se ve afectada, quién debe tomar la decisión y qué evidencia necesitaríamos para saber si esta idea está funcionando.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué impacto tiene la arquitectura sobre la calidad general del sistema? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué parte de mi proyecto es frágil por falta de diseño? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy pensando solo en la solución inmediata o también en el crecimiento futuro? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. La fuente afirma que La arquitectura determina el futuro del sistema.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La arquitectura importa porque define la calidad, la sostenibilidad y la responsabilidad del sistema. Un diseño bien pensado protege el negocio, al equipo y a las personas que usan la solución. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa problema esencial y decisiones técnicas en tus propias palabras y relaciónalo con esta fuente: Este video responde una pregunta central: ¿por qué la arquitectura de software es importante si al final un sistema solo necesita funcionar? La respuesta es que un sistema no se mide solo por su funcionamiento inmediato, sino por su capacidad de crecer, proteger datos, ser usable y responder a nuevas necesidades sin romperse.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué impacto tiene la arquitectura sobre la calidad general del sistema?** Mi respuesta de partida es: La arquitectura determina el futuro del sistema. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Qué parte de mi proyecto es frágil por falta de diseño?** Mi respuesta de partida es: Un sistema puede trabajar hoy y fallar mañana si no está bien diseñado. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Estoy pensando solo en la solución inmediata o también en el crecimiento futuro?** Mi respuesta de partida es: La escalabilidad implica crecer sin perder rendimiento ni estabilidad. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar problema esencial y decisiones técnicas, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia el arquitecto y la responsabilidad técnica.

## 🤔 Para pensar antes de continuar
- ¿Qué impacto tiene la arquitectura sobre la calidad general del sistema?
- ¿Qué parte de mi proyecto es frágil por falta de diseño?
- ¿Estoy pensando solo en la solución inmediata o también en el crecimiento futuro?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 1: diagnóstico y contexto arquitectónico. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
