# Video 07: Monolitos, sistemas distribuidos y microservicios

## Fuentes oficiales
- [Monolito vs arquitectura distribuida](https://platzi.com/cursos/fundamentos-arquitectura-software/como-elegir-un-estilo-arquitectonico-sin/)
- [Microservicios y organización por dominios](https://platzi.com/cursos/fundamentos-arquitectura-software/arquitectura-cliente-servidor-fundamento/)

## 🔗 Navegación
[⬅️ Video anterior](video-06.md) | [➡️ Video siguiente](video-08.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: monolitos, sistemas distribuidos y microservicios. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Monolito vs arquitectura distribuida**
Este video compara dos enfoques arquitectónicos muy comunes: el monolito y la arquitectura distribuida. El monolito puede ser una buena opción cuando el sistema es relativamente pequeño o cuando se desea velocidad de desarrollo y menor complejidad operativa. Sin embargo, cuando el proyecto crece y la organización requiere mayor desacople y evolución independiente, la arquitectura distribuida puede ser más apropiada.

La clave no es elegir una opción “mejor” en abstracto, sino seleccionar la que mejor se adapte a la complejidad real del sistema, el tamaño del equipo, la carga de trabajo y los objetivos de negocio. El problema aparece cuando se adopta una solución distribuida solo por moda, sin analizar su costo operativo.

**Fuente 2: Microservicios y organización por dominios**
La arquitectura basada en microservicios suele asociarse con escalabilidad y flexibilidad, pero también con mayor complejidad distribuidas. Este video explica que los microservicios no son una solución mágica: tienen sentido cuando la organización y el dominio del negocio lo justifican. Una buena división por servicios debe surgir del dominio, de las responsabilidades y de la capacidad de evolución del negocio.

La organización por dominios ayuda a definir límites claros y a separar áreas con objetivos diferentes. Cuando esto se hace bien, el sistema gana claridad. Cuando se hace mal, se vuelve difícil de operar, depurar y mantener.

## Ideas que debes conservar
- El monolito y la arquitectura distribuida tienen ventajas y costos distintos.
- La elección depende del problema real, no de la tendencia.
- El monolito reduce complejidad de operación, pero puede limitar evolución.
- La arquitectura distribuida mejora desacople y escalabilidad, pero aumenta complejidad.
- Los microservicios solo tienen valor si se justifican por el problema real.
- La división debe ser por dominio y responsabilidad, no por moda.
- El diseño por dominios ayuda a clarificar la estructura del sistema.
- Una arquitectura distribuida exige más coordinación y observabilidad.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: monolitos, sistemas distribuidos y microservicios. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **monolitos, sistemas distribuidos y microservicios**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: El monolito y la arquitectura distribuida tienen ventajas y costos distintos.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos monolitos, sistemas distribuidos y microservicios al flujo.
    2. **Actor prioritario de monolitos, sistemas distribuidos y microservicios:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en monolitos, sistemas distribuidos y microservicios:** escribe la condición que debe permanecer verdadera y relaciónala con el monolito y la arquitectura distribuida tienen ventajas y costos distintos..
    4. **Punto de decisión para monolitos, sistemas distribuidos y microservicios:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de monolitos, sistemas distribuidos y microservicios:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **monolitos, sistemas distribuidos y microservicios**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa monolitos, sistemas distribuidos y microservicios y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: el monolito y la arquitectura distribuida tienen ventajas y costos distintos.
3. Identifica el actor que recibe el impacto de monolitos, sistemas distribuidos y microservicios y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para monolitos, sistemas distribuidos y microservicios; compara sus costos y riesgos.
5. Elige una opción para monolitos, sistemas distribuidos y microservicios, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: monolitos, sistemas distribuidos y microservicios debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Mi sistema necesita más desacople o más simplicidad?

**Respuesta concreta:** Para monolitos, sistemas distribuidos y microservicios, el cliente necesita recibir un estado de entrega confiable. La respuesta concreta es proteger la regla 'no mostrar una entrega como completada sin evidencia válida' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Estoy adoptando una arquitectura por moda o por necesidad real?

**Respuesta concreta:** Para monolitos, sistemas distribuidos y microservicios, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿La separación de servicios refleja bien el dominio del negocio?

**Respuesta concreta:** Para monolitos, sistemas distribuidos y microservicios, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Estoy aumentando complejidad operativa por una decisión no justificada?

**Respuesta concreta:** Para monolitos, sistemas distribuidos y microservicios, elegiría la alternativa que garantice que el equipo de soporte pueda reconstruir qué ocurrió durante un incidente. La opción sencilla reduce el costo inicial, pero puede dejar débil la regla 'tener eventos, errores y estados observables'; la opción más estructurada cuesta más, pero facilita probarla y cambiarla. Para el MVP escogería la segunda solo si el riesgo es crítico y documentaría la condición de revisión.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa monolitos, sistemas distribuidos y microservicios y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de monolitos, sistemas distribuidos y microservicios:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para monolitos, sistemas distribuidos y microservicios:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de monolitos, sistemas distribuidos y microservicios:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: El monolito y la arquitectura distribuida tienen ventajas y costos distintos. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a monolitos, sistemas distribuidos y microservicios: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de monolitos, sistemas distribuidos y microservicios, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Monolitos, sistemas distribuidos y microservicios:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
No existe una arquitectura universalmente superior; la mejor opción es la que responde mejor al problema real, a la organización y a la capacidad de evolución del sistema.

Microservicios pueden ser útiles, pero solo cuando resuelven un problema real de organización, evolución y complejidad. La arquitectura debe simplificar, no complicar inútilmente.

## Preguntas para preparar la grabación
- ¿Mi sistema necesita más desacople o más simplicidad?
- ¿Estoy adoptando una arquitectura por moda o por necesidad real?
- ¿La separación de servicios refleja bien el dominio del negocio?
- ¿Estoy aumentando complejidad operativa por una decisión no justificada?

## Evidencia para el repositorio
Guarda la explicación de monolitos, sistemas distribuidos y microservicios, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
