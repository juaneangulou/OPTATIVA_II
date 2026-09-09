# Video 22: Bases de datos y API Gateway

## Fuentes oficiales
- [Arquitectura moderna y liderazgo](https://platzi.com/cursos/software-avanzado/migraciones-de-base-de-datos-con-flyway/)
- [Documentación y decisiones explícitas](https://platzi.com/cursos/software-avanzado/api-gateway-como-capa-de-abstraccion-en/)

## 🔗 Navegación
[⬅️ Video anterior](video-21.md) | [➡️ Video siguiente](video-23.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: bases de datos y api gateway. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Arquitectura moderna y liderazgo**
El video final reúne los principales temas del curso: la arquitectura de software ya no es solo una disciplina técnica de diagramas y patrones, sino una práctica estratégica que conecta negocio, tecnología, personas y evolución. El arquitecto moderno debe pensar en sistemas sostenibles, seguros, escalables, observables y alineados con el contexto real donde operan.

Además, se resalta que la tecnología cambia rápido, pero la esencia del liderazgo arquitectónico no: la clave es tomar decisiones con criterio, comunicar claramente, resolver conflictos, y guiar a equipos a construir soluciones con sentido. La arquitectura moderna requiere una mezcla de técnica, visión de negocio, capacidad de análisis, juicio ético y habilidades de liderazgo. Es más que construir software: es diseñar el camino para que ese software pueda sobrevivir y aportar valor con el tiempo.

**Fuente 2: Documentación y decisiones explícitas**
La documentación de arquitectura no es un lujo ni una actividad burocrática superficial; es una herramienta clave para que el sistema pueda entenderse, evolucionar y sostenerse en el tiempo. Cuando las decisiones se documentan de forma clara, el equipo puede reducir ambigüedad, evitar errores de interpretación y mantener continuidad incluso con cambios de personal. El video hace hincapié en que la arquitectura debe dejarse escrita, no solo en la cabeza de unos pocos.

Esto incluye explicar trade-offs, restricciones, decisiones tomadas y alternativas descartadas. Cuando un proyecto se basa en decisiones implícitas, cada integrante empieza a hacer su propia “lectura” del sistema. La documentación ayuda a que el diseño sea compartido, revisado y mejorado con base en evidencia.

## Ideas que debes conservar
- La arquitectura moderna combina tecnología, negocio y estrategia.
- El arquitecto actúa como guía, decisor y comunicador.
- La calidad del sistema depende de decisiones y procesos, no solo de ideas técnicas.
- La evolución continua exige adaptación constante y aprendizaje.
- La documentación reduce ambigüedad y ayuda a la continuidad del proyecto.
- Las decisiones arquitectónicas deben ser explícitas, no solo inferidas.
- Documentar no significa escribir mucho por escrito; significa registrar lo relevante.
- Se deben reflejar restricciones, decisiones, alternativas y razones.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: bases de datos y api gateway. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **bases de datos y api gateway**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: La arquitectura moderna combina tecnología, negocio y estrategia.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos bases de datos y api gateway al flujo.
    2. **Actor prioritario de bases de datos y api gateway:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en bases de datos y api gateway:** escribe la condición que debe permanecer verdadera y relaciónala con la arquitectura moderna combina tecnología, negocio y estrategia..
    4. **Punto de decisión para bases de datos y api gateway:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de bases de datos y api gateway:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **bases de datos y api gateway**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa bases de datos y api gateway y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: la arquitectura moderna combina tecnología, negocio y estrategia.
3. Identifica el actor que recibe el impacto de bases de datos y api gateway y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para bases de datos y api gateway; compara sus costos y riesgos.
5. Elige una opción para bases de datos y api gateway, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: bases de datos y api gateway debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Qué tipo de arquitecto quiero ser: técnico, estratégico o de liderazgo?

**Respuesta concreta:** Para bases de datos y api gateway, el cliente necesita recibir un estado de entrega confiable. La respuesta concreta es proteger la regla 'no mostrar una entrega como completada sin evidencia válida' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Estoy construyendo soluciones solo para hoy o para el crecimiento futuro?

**Respuesta concreta:** Si el sistema crece en el tema de bases de datos y api gateway, el operador logístico seguirá necesitando reasignar una ruta sin perder el historial del pedido. No elegiría una solución distribuida automáticamente; primero mediría carga, latencia y errores. Mantendría la regla 'conservar trazabilidad de cada cambio' en un módulo claro y escalaría solo el punto que demuestre saturación. La decisión se verifica con una prueba de carga y una métrica acordada.

### ❓ ¿Qué decisiones importantes de mi proyecto están aún en la cabeza de una sola persona?

**Respuesta concreta:** Para bases de datos y api gateway, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Estoy documentando solo la solución final o también el porqué?

**Respuesta concreta:** Para bases de datos y api gateway, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa bases de datos y api gateway y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de bases de datos y api gateway:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para bases de datos y api gateway:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de bases de datos y api gateway:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La arquitectura moderna combina tecnología, negocio y estrategia. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a bases de datos y api gateway: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de bases de datos y api gateway, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Bases de datos y API Gateway:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
El curso cierra con una visión clara: la mejor arquitectura no es la más compleja ni la más innovadora, sino la que resuelve el problema real con criterio, sostenibilidad y capacidad de evolución. El arquitecto de software es quien convierte la complejidad en claridad y guía a la organización para crear soluciones con valor duradero.

La documentación arquitectónica es una forma de preservar el conocimiento y de evitar que el sistema se vuelva incomprensible con el tiempo. Un buen diseño debe ser enseñable, comprensible y defendible.

## Preguntas para preparar la grabación
- ¿Qué tipo de arquitecto quiero ser: técnico, estratégico o de liderazgo?
- ¿Estoy construyendo soluciones solo para hoy o para el crecimiento futuro?
- ¿Qué decisiones importantes de mi proyecto están aún en la cabeza de una sola persona?
- ¿Estoy documentando solo la solución final o también el porqué?

## Evidencia para el repositorio
Guarda la explicación de bases de datos y api gateway, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
