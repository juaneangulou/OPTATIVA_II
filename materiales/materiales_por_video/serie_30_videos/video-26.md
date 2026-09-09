# Video 26: Process Manager, Durable State y Event Sourcing

## Fuentes oficiales
- [Estrategia tecnológica y roadmap](https://platzi.com/cursos/software-avanzado/que-es-el-patron-process-manager/)
- [Evaluación de tecnologías y decisiones de stack](https://platzi.com/cursos/software-avanzado/durable-state-vs-event-sourcing-en-siste/)

## 🔗 Navegación
[⬅️ Video anterior](video-25.md) | [➡️ Video siguiente](video-27.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: process manager, durable state y event sourcing. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Estrategia tecnológica y roadmap**
El video aborda el papel de la estrategia tecnológica en la arquitectura. No basta con elegir una buena herramienta o un patrón útil; también hace falta una dirección clara para el camino del sistema. Una estrategia tecnológica define hacia dónde va la solución, qué capacidades se priorizan, qué riesgos se asumen y qué inversiones son necesarias para que la arquitectura evolucione de forma ordenada.

El roadmap se convierte en la herramienta que convierte la visión en acción. Cuando hay estrategia y planificación, el equipo evita decisiones aisladas y poco alineadas. El arquitecto tiene un rol importante en definir no solo cómo se construye el sistema, sino también qué se prioriza y en qué orden.

**Fuente 2: Evaluación de tecnologías y decisiones de stack**
La elección de tecnologías es una decisión arquitectónica y no una cuestión de moda. Cada stack tiene ventajas, costos y limitaciones. El video insiste en que seleccionar una tecnología debe hacerse con base en el problema, la capacidad del equipo, los requisitos de operación, la curva de aprendizaje y la sostenibilidad a largo plazo.

Muchas veces se adopta una tecnología por popularidad, pero eso no garantiza que se adapte bien al caso real. La evaluación del stack debe incluir mantenimiento, soporte, costos operativos, compatibilidad, seguridad y potencial de crecimiento. Así, la decisión de usar determinada herramienta o framework se vuelve más estratégica y menos impulsiva.

## Ideas que debes conservar
- La estrategia tecnológica guía la evolución del sistema.
- Un roadmap ayuda a convertir visión en decisiones secuenciales.
- Las decisiones deben priorizar capacidades que generen valor real.
- Sin estrategia, la arquitectura puede volverse reactiva y caótica.
- Las tecnologías deben elegirse por contexto, no por tendencia.
- Cada stack implica costos de operación, entrenamiento y mantenimiento.
- Un buen stack debe facilitar velocidad de entrega y sostenibilidad.
- La elección tecnológica debe estar alineada con la estrategia del sistema.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: process manager, durable state y event sourcing. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **process manager, durable state y event sourcing**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: La estrategia tecnológica guía la evolución del sistema.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos process manager, durable state y event sourcing al flujo.
    2. **Actor prioritario de process manager, durable state y event sourcing:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en process manager, durable state y event sourcing:** escribe la condición que debe permanecer verdadera y relaciónala con la estrategia tecnológica guía la evolución del sistema..
    4. **Punto de decisión para process manager, durable state y event sourcing:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de process manager, durable state y event sourcing:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **process manager, durable state y event sourcing**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa process manager, durable state y event sourcing y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: la estrategia tecnológica guía la evolución del sistema.
3. Identifica el actor que recibe el impacto de process manager, durable state y event sourcing y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para process manager, durable state y event sourcing; compara sus costos y riesgos.
5. Elige una opción para process manager, durable state y event sourcing, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: process manager, durable state y event sourcing debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Qué dirección tecnológica está tomando mi proyecto?

**Respuesta concreta:** Para process manager, durable state y event sourcing, el cliente necesita recibir un estado de entrega confiable. La respuesta concreta es proteger la regla 'no mostrar una entrega como completada sin evidencia válida' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Tengo una hoja de ruta clara o solo decisiones aisladas?

**Respuesta concreta:** Para process manager, durable state y event sourcing, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Estoy eligiendo tecnología por necesidad o por tendencia?

**Respuesta concreta:** Para process manager, durable state y event sourcing, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué tan bien se adapta mi stack a los objetivos del proyecto?

**Respuesta concreta:** Para process manager, durable state y event sourcing, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa process manager, durable state y event sourcing y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de process manager, durable state y event sourcing:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para process manager, durable state y event sourcing:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de process manager, durable state y event sourcing:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La estrategia tecnológica guía la evolución del sistema. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a process manager, durable state y event sourcing: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de process manager, durable state y event sourcing, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Process Manager, Durable State y Event Sourcing:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La estrategia y el roadmap son lo que hacen que la arquitectura deje de ser una respuesta improvisada y se convierta en una dirección clara. Un sistema necesita visión para crecer sin perder coherencia.

Elegir tecnologías es una forma de diseñar la capacidad del sistema para seguir funcionando bien en el futuro. La mejor decisión es la que resuelve el problema real con menos deuda técnica y menos riesgo.

## Preguntas para preparar la grabación
- ¿Qué dirección tecnológica está tomando mi proyecto?
- ¿Tengo una hoja de ruta clara o solo decisiones aisladas?
- ¿Estoy eligiendo tecnología por necesidad o por tendencia?
- ¿Qué tan bien se adapta mi stack a los objetivos del proyecto?

## Evidencia para el repositorio
Guarda la explicación de process manager, durable state y event sourcing, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
