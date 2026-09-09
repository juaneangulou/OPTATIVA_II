# Video 10: Estructura del sistema y estilos arquitectónicos

## Título
Estructura del sistema y estilos arquitectónicos

## 🧭 Punto de partida
Vienes de trabajar diagnóstico de contexto arquitectónico. No vamos a repetirlo: lo usaremos como punto de partida para estudiar estructura del sistema y estilos arquitectónicos y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con monolito modular: empezar bien sin cerrarse.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Diagnóstico de contexto arquitectónico](video-09.md)

[➡️ Video siguiente: Monolito modular: empezar bien sin cerrarse](video-11.md)

## 🎥 La situación que vamos a resolver
La fuente de esta clase es 'Video 19: Estructura de software y evolución del sistema'. Este video resalta la relación entre la estructura del software y su capacidad de evolución. Los sistemas no son estáticos; cambian con el tiempo, según la carga, el negocio, las reglas y las necesidades del usuario. Por eso, la arquitectura debe permitir cambios sin provocar caos. La estructura del software debe facilitar adaptaciones, no volverlas costosas o riesgosas.

Cuando la estructura del sistema es clara, modular y bien diseñada, el cambio no rompe todo. Cuando está mal organizada, cada ajuste requiere correcciones complejas y difíciles de prever. La evolución del software depende directamente de la calidad de su arquitectura. En la plataforma logística, esto aparece cuando pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. No voy a darte una respuesta prefabricada: vamos a descubrir qué decisión exige esta situación.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar estructura del sistema y estilos arquitectónicos con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video resalta la relación entre la estructura del software y su capacidad de evolución.

La fuente desarrolla esta situación con más detalle en el bloque anterior. Ahora quiero que hagamos algo distinto: separar el problema esencial de los detalles técnicos que podríamos elegir después.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta estructura del sistema y estilos arquitectónicos como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. El sistema evolucionará; la arquitectura debe anticiparlo.

Detente en la consecuencia de esta idea: El sistema evolucionará; la arquitectura debe anticiparlo. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. La estructura define cuán costoso es cambiar el software.

Detente en la consecuencia de esta idea: La estructura define cuán costoso es cambiar el software. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. Un diseño claro Reduce impacto de cambios y nuevos requerimientos.

Aquí quiero que mires el riesgo humano de esta idea. Un diseño claro Reduce impacto de cambios y nuevos requerimientos. Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en la plataforma logística.

### 4. La evolución del sistema requiere capacidad de adaptación.

Detente en la consecuencia de esta idea: La evolución del sistema requiere capacidad de adaptación. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 5. Los sistemas mal estructurados se vuelven frágiles con el tiempo.

Detente en la consecuencia de esta idea: Los sistemas mal estructurados se vuelven frágiles con el tiempo. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. La arquitectura debe ser pensada para el futuro, no solo para el presente.

Detente en la consecuencia de esta idea: La arquitectura debe ser pensada para el futuro, no solo para el presente. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Qué tan costoso es cambiar una parte del sistema hoy? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué piezas del software están más rígidas o frágiles? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Estoy diseñando para crecer o para sobrevivir solo un tiempo corto? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. La fuente afirma que El sistema evolucionará; la arquitectura debe anticiparlo.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La capacidad de evolución es una medida de calidad arquitectónica. Los sistemas más sólidos son aquellos que soportan cambios sin destruir su lógica ni su estabilidad. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa estructura del sistema y estilos arquitectónicos en tus propias palabras y relaciónalo con esta fuente: Este video resalta la relación entre la estructura del software y su capacidad de evolución.
2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.
3. Elige una decisión concreta; no escribas todavía una solución completa.
4. Explica qué alternativa descartas y qué costo aceptas al elegir.
5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.
6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

1. **¿Qué tan costoso es cambiar una parte del sistema hoy?** Mi respuesta de partida es: El sistema evolucionará; la arquitectura debe anticiparlo. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Qué piezas del software están más rígidas o frágiles?** Mi respuesta de partida es: La estructura define cuán costoso es cambiar el software. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿Estoy diseñando para crecer o para sobrevivir solo un tiempo corto?** Mi respuesta de partida es: Un diseño claro Reduce impacto de cambios y nuevos requerimientos. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar estructura del sistema y estilos arquitectónicos, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia monolito modular: empezar bien sin cerrarse.

## 🤔 Para pensar antes de continuar
- ¿Qué tan costoso es cambiar una parte del sistema hoy?
- ¿Qué piezas del software están más rígidas o frágiles?
- ¿Estoy diseñando para crecer o para sobrevivir solo un tiempo corto?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 2: requisitos y decisión estructural. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
