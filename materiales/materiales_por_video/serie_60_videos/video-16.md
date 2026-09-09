# Video 16: Infraestructura, despliegue y entorno de ejecución

## Título
Infraestructura, despliegue y entorno de ejecución

## 🧭 Punto de partida
Vienes de trabajar acoplamiento entre servicios y sistemas. No vamos a repetirlo: lo usaremos como punto de partida para estudiar infraestructura, despliegue y entorno de ejecución y añadir una decisión nueva al expediente.

Al terminar esta conversación, tendrás una decisión nueva que enlaza con observabilidad y monitoreo de sistemas.

## 🧭 Navegar por la ruta
[⬅️ Video anterior: Acoplamiento entre servicios y sistemas](video-15.md)

[➡️ Video siguiente: Observabilidad y monitoreo de sistemas](video-17.md)

## 🎥 La situación que vamos a resolver
La fuente consultada para esta clase es 'Video 14: Infraestructura, despliegue y entorno de ejecución'. En nuestro recorrido la conectamos con el tema 'Infraestructura, despliegue y entorno de ejecución' porque queremos estudiar infraestructura, despliegue y entorno de ejecución desde un problema real. La fuente plantea: Este video muestra que la arquitectura incluye también la infraestructura que ejecuta el sistema. Un diseño puede ser excelente en código, pero si el entorno de ejecución es caótico, manual o poco reproducible, la aplicación no será sostenible. La arquitectura debe considerar tanto la capa lógica como la capa operativa que la pone en marcha.

La infraestructura debe ser fácil de reproducir, detectar fallos y trasladar entre entornos. Los despliegues automatizados y los procesos de entorno ayudan a reducir errores humanos y mejorar la confianza del sistema en producción. En la plataforma logística, esto aparece cuando pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. Primero entenderemos la fuente y después construiremos la decisión.

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar infraestructura, despliegue y entorno de ejecución con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: Este video muestra que la arquitectura incluye también la infraestructura que ejecuta el sistema.

Ahora voy a separar contigo tres niveles: lo que la fuente afirma, el problema esencial que debemos resolver y las decisiones técnicas que podríamos tomar después. Si confundimos esos niveles, terminaremos usando una tecnología como respuesta a un problema que todavía no hemos definido.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta infraestructura, despliegue y entorno de ejecución como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

### 1. La infraestructura es parte del diseño arquitectónico.

Detente en la consecuencia de esta idea: La infraestructura es parte del diseño arquitectónico. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 2. El entorno debe ser reproducible y consistente.

Detente en la consecuencia de esta idea: El entorno debe ser reproducible y consistente. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 3. Un despliegue manual aumenta riesgos y errores.

Detente en la consecuencia de esta idea: Un despliegue manual aumenta riesgos y errores. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 4. La infraestructura debe soportar diferentes contextos: desarrollo, prueba y producción.

Esta idea solo queda completa cuando podemos comprobarla. La infraestructura debe soportar diferentes contextos: desarrollo, prueba y producción. Elige una prueba o métrica y explica qué resultado confirmaría o cuestionaría nuestra decisión sobre infraestructura, despliegue y entorno de ejecución.

### 5. La operación y la arquitectura están conectadas.

Detente en la consecuencia de esta idea: La operación y la arquitectura están conectadas. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

### 6. La calidad del sistema depende también de cómo se entrega.

Detente en la consecuencia de esta idea: La calidad del sistema depende también de cómo se entrega. Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué.

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
- **Te pregunto:** ¿Mi entorno es reproducible y consistente? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿Qué tan fácil es desplegar una versión nueva sin riesgos innecesarios? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.
- **Te pregunto:** ¿La infraestructura actual acompaña o complica la evolución del sistema? **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema.

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

## 🔀 Opciones para resolver infraestructura, despliegue y entorno de ejecución

- **Opción A:** aplicar una solución sencilla dentro de la estructura actual, documentando sus límites.
- **Opción B:** introducir una separación o mecanismo especializado para proteger el riesgo principal de la fuente.

Compara ambas por costo inicial, calidad, operación, facilidad de cambio y evidencia disponible. Elige una solo después de explicar qué problema resuelve y qué costo aceptas.

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna. La fuente afirma que La infraestructura es parte del diseño arquitectónico.. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: La arquitectura no termina en el código: incluye cómo se ejecuta, se despliega y se mantiene. Un sistema bien diseñado también necesita un entorno bien pensado. Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

1. Escribe qué significa infraestructura, despliegue y entorno de ejecución en tus propias palabras y relaciónalo con esta fuente: Este video muestra que la arquitectura incluye también la infraestructura que ejecuta el sistema.
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

1. **¿Mi entorno es reproducible y consistente?** Mi respuesta de partida es: La infraestructura es parte del diseño arquitectónico. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
2. **¿Qué tan fácil es desplegar una versión nueva sin riesgos innecesarios?** Mi respuesta de partida es: El entorno debe ser reproducible y consistente. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.
3. **¿La infraestructura actual acompaña o complica la evolución del sistema?** Mi respuesta de partida es: Un despliegue manual aumenta riesgos y errores. En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión.

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar infraestructura, despliegue y entorno de ejecución, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia observabilidad y monitoreo de sistemas.

## 🤔 Para pensar antes de continuar
- ¿Mi entorno es reproducible y consistente?
- ¿Qué tan fácil es desplegar una versión nueva sin riesgos innecesarios?
- ¿La infraestructura actual acompaña o complica la evolución del sistema?

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de Actividad 2: requisitos y decisión estructural. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
