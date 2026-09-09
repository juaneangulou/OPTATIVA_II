# Video 23: Bounded Context e infraestructura como código

## Fuentes oficiales
- [Cultura de arquitectura en el equipo](https://platzi.com/cursos/software-avanzado/bounded-context-y-context-maps-en-micros/)
- [Comunicación y negociación técnica](https://platzi.com/cursos/software-avanzado/infraestructura-como-codigo-en-monorepos/)

## 🔗 Navegación
[⬅️ Video anterior](video-22.md) | [➡️ Video siguiente](video-24.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: bounded context e infraestructura como código. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

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
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: bounded context e infraestructura como código. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **bounded context e infraestructura como código**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: La arquitectura se fortalece con una cultura de calidad y reflexión.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos bounded context e infraestructura como código al flujo.
    2. **Actor prioritario de bounded context e infraestructura como código:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en bounded context e infraestructura como código:** escribe la condición que debe permanecer verdadera y relaciónala con la arquitectura se fortalece con una cultura de calidad y reflexión..
    4. **Punto de decisión para bounded context e infraestructura como código:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de bounded context e infraestructura como código:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **bounded context e infraestructura como código**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa bounded context e infraestructura como código y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: la arquitectura se fortalece con una cultura de calidad y reflexión.
3. Identifica el actor que recibe el impacto de bounded context e infraestructura como código y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para bounded context e infraestructura como código; compara sus costos y riesgos.
5. Elige una opción para bounded context e infraestructura como código, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: bounded context e infraestructura como código debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Mi equipo tiene una cultura clara para discutir decisiones de arquitectura?

**Respuesta concreta:** Para bounded context e infraestructura como código, el cliente necesita recibir un estado de entrega confiable. La respuesta concreta es proteger la regla 'no mostrar una entrega como completada sin evidencia válida' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Se valora la calidad del sistema por encima de la rapidez individual?

**Respuesta concreta:** Para bounded context e infraestructura como código, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Estoy logrando comunicar claramente mis decisiones técnicas?

**Respuesta concreta:** Para bounded context e infraestructura como código, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Cómo explico los trade-offs a personas no técnicas?

**Respuesta concreta:** Para bounded context e infraestructura como código, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa bounded context e infraestructura como código y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de bounded context e infraestructura como código:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para bounded context e infraestructura como código:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de bounded context e infraestructura como código:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La arquitectura se fortalece con una cultura de calidad y reflexión. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a bounded context e infraestructura como código: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de bounded context e infraestructura como código, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Bounded Context e infraestructura como código:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La arquitectura madura no vive solo en la solución; vive en la manera en que el equipo trabaja. Si la cultura del equipo favorece la claridad, la responsabilidad y la mejora constante, la arquitectura se fortalece de manera natural.

El arquitecto no solo resuelve problemas técnicos; también ayuda a que el equipo y la organización compartan una visión común. Sin buena comunicación, incluso una arquitectura excelente puede fracasar por falta de comprensión o aceptación.

## Preguntas para preparar la grabación
- ¿Mi equipo tiene una cultura clara para discutir decisiones de arquitectura?
- ¿Se valora la calidad del sistema por encima de la rapidez individual?
- ¿Estoy logrando comunicar claramente mis decisiones técnicas?
- ¿Cómo explico los trade-offs a personas no técnicas?

## Evidencia para el repositorio
Guarda la explicación de bounded context e infraestructura como código, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
