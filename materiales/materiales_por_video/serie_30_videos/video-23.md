# Video 23: Bounded Context e infraestructura como código

## Fuentes oficiales
- [Platzi: Cultura de arquitectura en el equipo](https://platzi.com/cursos/software-avanzado/bounded-context-y-context-maps-en-micros/)
- [Platzi: Comunicación y negociación técnica](https://platzi.com/cursos/software-avanzado/infraestructura-como-codigo-en-monorepos/)

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
Analiza cómo este tema afecta pedidos, inventario, ruteo, entregas, notificaciones, incidentes y operación. Elige un flujo concreto y explica qué responsabilidad, dependencia o atributo de calidad queda protegido.

## Actividad de construcción
1. Resume en tus palabras la idea central de cada fuente.
2. Combina esas ideas en un problema arquitectónico único.
3. Propón dos alternativas de solución.
4. Compara costo inicial, calidad, riesgo, operación y facilidad de cambio.
5. Elige una alternativa para el MVP y declara qué condición obligaría a revisarla.
6. Produce una evidencia: ADR, diagrama, contrato, código C#, prueba, métrica o plan de evolución.

## Respuesta orientadora
Una respuesta sólida conecta las fuentes con el caso. No basta decir que una tecnología es mejor: debes explicar qué problema resuelve, qué costo introduce, qué alternativa descartas y cómo comprobarás la decisión.

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
