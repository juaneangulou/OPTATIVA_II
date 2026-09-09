# Video 23: Bounded Context e infraestructura como código

## Fuentes oficiales
- [Cultura de arquitectura en el equipo](https://platzi.com/cursos/software-avanzado/bounded-context-y-context-maps-en-micros/)
- [Comunicación y negociación técnica](https://platzi.com/cursos/software-avanzado/infraestructura-como-codigo-en-monorepos/)

## 🔗 Navegación
[⬅️ Video anterior](video-22.md) | [➡️ Video siguiente](video-24.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Cultura de arquitectura en el equipo**
La arquitectura de software no se construye solo con diagramas o decisiones individuales; también depende de la cultura del equipo. Cuando el equipo entiende la importancia de la calidad, la comunicación, la responsabilidad y la evolución del sistema, la arquitectura tiene más posibilidades de ser sólida. Si la cultura del equipo es deficiente, incluso un buen diseño técnico puede terminar diluyéndose por falta de disciplina o consenso.

El video resalta que la arquitectura debe ser una práctica compartida, no un privilegio de unos pocos. Eso implica hablar sobre decisiones, revisar cambios, cuestionar supuestos, aceptar feedback y crear una mentalidad que valore la sostenibilidad por encima de la rapidez improvisada.

**Fuente 2: Comunicación y negociación técnica**
Una gran parte del trabajo de un arquitecto no ocurre en un editor de código, sino en conversaciones. El arquitecto debe comunicar decisiones, explicar trade-offs, escuchar necesidades del negocio y convencer a diferentes actores sobre la dirección correcta de la solución. La comunicación técnica es una competencia esencial porque la arquitectura no se implementa solo con conocimiento; se ejecuta con consenso.

El video subraya que en muchas decisiones arquitectónicas hay conflictos entre necesidades de tiempo, costo, calidad, riesgo y visión. En esos momentos, la capacidad de negociar, sintetizar y explicar la elección correcta es tan importante como el conocimiento técnico. La arquitectura también se trata de ser claro, persuasivo y empático con quienes toman decisiones o se ven afectados por ellas.

## Ideas que debes conservar
- La arquitectura se fortalece con una cultura de calidad y reflexión.
- Los equipos necesitan una manera clara de discutir y decidir cambios.
- La mejora continua es más efectiva que la improvisación aislada.
- La construcción de software no es solo técnica; es una práctica colectiva.
- La arquitectura se comunica tanto como se diseña.
- Los stakeholders no siempre hablan el mismo lenguaje técnico.
- Los trade-offs deben explicarse de forma clara y útil.
- Un arquitecto debe escuchar, explicar y alinear.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **bounded context e infraestructura como código**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: La arquitectura se fortalece con una cultura de calidad y reflexión.
2. **Actores afectados:** cliente, operador logístico, repartidor, equipo de soporte y equipo técnico. Cada uno necesita información y garantías diferentes.
3. **Punto de decisión:** el equipo debe decidir qué responsabilidad queda en el módulo de pedidos, qué cruza hacia ruteo o inventario y qué se delega a una dependencia externa.
4. **Riesgo:** si la decisión es débil, puede haber entregas tardías, datos expuestos, cambios costosos, mensajes perdidos o una operación imposible de diagnosticar.
5. **Evidencia:** la decisión se demuestra con el artefacto adecuado: diagrama, ADR, contrato, código, prueba, métrica, registro de despliegue o experimento controlado.

Para resolver el caso, empieza por el flujo “crear pedido”. Señala el componente que recibe la solicitud, la regla que debe protegerse, la dependencia que puede fallar y el resultado que espera cada actor. Después compara dos formas de construirlo: una solución sencilla para el MVP y otra con mayor separación. La elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Resume en tus palabras la idea central de cada fuente.
2. Combina esas ideas en un problema arquitectónico único.
3. Propón dos alternativas de solución.
4. Compara costo inicial, calidad, riesgo, operación y facilidad de cambio.
5. Elige una alternativa para el MVP y declara qué condición obligaría a revisarla.
6. Produce una evidencia: ADR, diagrama, contrato, código C#, prueba, métrica o plan de evolución.

## Respuestas a las preguntas
### ❓ ¿Mi equipo tiene una cultura clara para discutir decisiones de arquitectura?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la arquitectura se fortalece con una cultura de calidad y reflexión. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Se valora la calidad del sistema por encima de la rapidez individual?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con los equipos necesitan una manera clara de discutir y decidir cambios. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy logrando comunicar claramente mis decisiones técnicas?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la mejora continua es más efectiva que la improvisación aislada. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Cómo explico los trade-offs a personas no técnicas?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la construcción de software no es solo técnica; es una práctica colectiva. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa bounded context e infraestructura como código y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La arquitectura se fortalece con una cultura de calidad y reflexión. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La arquitectura madura no vive solo en la solución; vive en la manera en que el equipo trabaja. Si la cultura del equipo favorece la claridad, la responsabilidad y la mejora constante, la arquitectura se fortalece de manera natural.

El arquitecto no solo resuelve problemas técnicos; también ayuda a que el equipo y la organización compartan una visión común. Sin buena comunicación, incluso una arquitectura excelente puede fracasar por falta de comprensión o aceptación.

## Preguntas para preparar la grabación
- ¿Mi equipo tiene una cultura clara para discutir decisiones de arquitectura?
- ¿Se valora la calidad del sistema por encima de la rapidez individual?
- ¿Estoy logrando comunicar claramente mis decisiones técnicas?
- ¿Cómo explico los trade-offs a personas no técnicas?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
