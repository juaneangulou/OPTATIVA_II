# Video 1: Decisiones de arquitectura y consecuencias reales

## Título
Decisiones de arquitectura y consecuencias reales

## 🧭 Punto de partida
Esta es la primera conversación del recorrido. Vamos a construir el punto de partida: mirar el sistema como una decisión que afecta a personas, negocio y operación.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con problema esencial y decisiones técnicas.

## 🧭 Navegar por la ruta
[➡️ Video siguiente: Problema esencial y decisiones técnicas](video-02.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 1: Decisiones de arquitectura de software y sus consecuencias reales'. Este video abre con una historia impactante: la tragedia del Boeing 737 MAX. La idea principal es que un fallo grave no siempre es un simple bug aislado, sino una mala decisión arquitectónica. Cuando se prioriza velocidad o costo por encima de seguridad, las consecuencias pueden ser humanas y devastadoras.

A partir de ese ejemplo, el curso presenta la arquitectura de software como una decisión con impacto real. No se trata solo de elegir tecnologías o dibujar diagramas; se trata de diseñar sistemas que sean seguros, confiables, sostenibles y responsables. Cada decisión técnica puede influir en escalabilidad, seguridad, privacidad, accesibilidad y ética. En la plataforma logística, esto aparece cuando la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar decisiones de arquitectura y consecuencias reales con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video abre con una historia impactante: la tragedia del Boeing 737 MAX.

La fuente desarrolla esta situación con más detalle en el bloque anterior. Ahora quiero que hagamos algo distinto: separar el problema esencial de los detalles técnicos que podríamos elegir después.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta decisiones de arquitectura y consecuencias reales como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. Las decisiones de software tienen consecuencias reales y humanas.

Detente en la consecuencia de esta idea: Las decisiones de software tienen consecuencias reales y humanas. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. No todo fallo es un bug aislado; a veces es un problema de diseño.

Detente en la consecuencia de esta idea: No todo fallo es un bug aislado; a veces es un problema de diseño. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. La arquitectura afecta seguridad, escalabilidad, privacidad y confiabilidad.

Aquí quiero que mires el riesgo humano de esta idea. La arquitectura afecta seguridad, escalabilidad, privacidad y confiabilidad. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

### 4. Priorizar costos o velocidad sin analizar el impacto puede ser peligroso.

Aquí quiero que mires el riesgo humano de esta idea. Priorizar costos o velocidad sin analizar el impacto puede ser peligroso. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

### 5. El arquitecto debe pensar más allá del código y en el contexto real del sistema.

Detente en la consecuencia de esta idea: El arquitecto debe pensar más allá del código y en el contexto real del sistema. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. La responsabilidad técnica es parte esencial del diseño.

Aquí quiero que mires el riesgo humano de esta idea. La responsabilidad técnica es parte esencial del diseño. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué decisiones técnicas están afectando la seguridad o confiabilidad de mis sistemas? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy priorizando velocidad por encima de calidad y sostenibilidad? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué consecuencias reales puede tener un diseño débil en producción? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. La fuente afirma que Las decisiones de software tienen consecuencias reales y humanas.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La arquitectura de software no es solo una disciplina técnica; es una responsabilidad. Cada decisión define no solo cómo funciona el sistema, sino también su impacto en personas, negocios y sociedad. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa decisiones de arquitectura y consecuencias reales en tus propias palabras y relaciónalo con esta fuente: Este video abre con una historia impactante: la tragedia del Boeing 737 MAX.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué decisiones técnicas están afectando la seguridad o confiabilidad de mis sistemas?** Mi respuesta de partida es: Las decisiones de software tienen consecuencias reales y humanas. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Estoy priorizando velocidad por encima de calidad y sostenibilidad?** Mi respuesta de partida es: No todo fallo es un bug aislado; a veces es un problema de diseño. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Qué consecuencias reales puede tener un diseño débil en producción?** Mi respuesta de partida es: La arquitectura afecta seguridad, escalabilidad, privacidad y confiabilidad. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar decisiones de arquitectura y consecuencias reales, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia problema esencial y decisiones técnicas.

## 🤔 Para pensar antes de continuar
- ¿Qué decisiones técnicas están afectando la seguridad o confiabilidad de mis sistemas?
- ¿Estoy priorizando velocidad por encima de calidad y sostenibilidad?
- ¿Qué consecuencias reales puede tener un diseño débil en producción?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 1: diagnóstico y contexto arquitectónico. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
