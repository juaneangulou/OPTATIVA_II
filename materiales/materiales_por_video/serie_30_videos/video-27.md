# Video 27: Máquinas de estado y seguridad de aplicaciones

## Fuentes oficiales
- [Riesgos, costos y sostenibilidad financiera](https://platzi.com/cursos/software-avanzado/maquinas-de-estado-finito-en-el-front-en/)
- [Arquitectura para equipos distribuidos](https://platzi.com/cursos/software-avanzado/tecnicas-sast-dast-y-pen-testing-para-se/)

## 🔗 Navegación
[⬅️ Video anterior](video-26.md) | [➡️ Video siguiente](video-28.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: máquinas de estado y seguridad de aplicaciones. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Riesgos, costos y sostenibilidad financiera**
La arquitectura de software también tiene implicaciones económicas. Un sistema no solo debe funcionar desde el punto de vista técnico; también debe ser viable desde el punto de vista financiero, operativo y de mantenimiento. Este video muestra que las decisiones de arquitectura implican costos directos e indirectos: infraestructura, equipos, tiempo, soporte, seguridad, correcciones y capacidad de adaptación.

La sostenibilidad financiera no es solo una preocupación del negocio; también afecta la arquitectura. Si el sistema es demasiado costoso de operar o difícil de mantener, su valor real disminuye. Por ello, el arquitecto debe ser capaz de medir el costo total de una solución y no solo el costo inicial de desarrollo.

**Fuente 2: Arquitectura para equipos distribuidos**
Cuando los equipos trabajan de forma distribuida, la arquitectura necesita ser más clara y más explícita. La comunicación, la coordinación y la documentación se vuelven críticos, porque el sistema no puede depender exclusivamente de la familiaridad entre personas. Un diseño bien estructurado permite que diferentes miembros del equipo trabajen en paralelo sin generar fricción o conflictos por responsabilidades ambiguas.

El video enfatiza que una arquitectura fuerte es también una herramienta de colaboración. Si el sistema está bien dividido, la documentación es clara y las interfaces están bien definidas, el equipo puede avanzar con menos fricción. Esto reduce errores de integración, soporta trabajo distribuido y mejora el flujo global del proyecto.

## Ideas que debes conservar
- La arquitectura tiene un costo real en infraestructura, operación y mantenimiento.
- Los riesgos técnicos y financieros deben evaluarse en conjunto.
- Un diseño barato al principio puede volverse muy costoso después.
- La sostenibilidad financiera depende del equilibrio entre valor y costo.
- La arquitectura facilita o complica el trabajo en equipo.
- Equipos distribuidos necesitan más claridad en interfaces y responsabilidades.
- La documentación y la comunicación son parte de la arquitectura efectiva.
- El diseño debe facilitar coordinación, no solo funcionalidad.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: máquinas de estado y seguridad de aplicaciones. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **máquinas de estado y seguridad de aplicaciones**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: La arquitectura tiene un costo real en infraestructura, operación y mantenimiento.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos máquinas de estado y seguridad de aplicaciones al flujo.
    2. **Actor prioritario de máquinas de estado y seguridad de aplicaciones:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en máquinas de estado y seguridad de aplicaciones:** escribe la condición que debe permanecer verdadera y relaciónala con la arquitectura tiene un costo real en infraestructura, operación y mantenimiento..
    4. **Punto de decisión para máquinas de estado y seguridad de aplicaciones:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de máquinas de estado y seguridad de aplicaciones:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **máquinas de estado y seguridad de aplicaciones**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa máquinas de estado y seguridad de aplicaciones y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: la arquitectura tiene un costo real en infraestructura, operación y mantenimiento.
3. Identifica el actor que recibe el impacto de máquinas de estado y seguridad de aplicaciones y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para máquinas de estado y seguridad de aplicaciones; compara sus costos y riesgos.
5. Elige una opción para máquinas de estado y seguridad de aplicaciones, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: máquinas de estado y seguridad de aplicaciones debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Qué costo total real tiene mi solución?

**Respuesta concreta:** Para máquinas de estado y seguridad de aplicaciones, elegiría la alternativa que garantice que el cliente pueda recibir un estado de entrega confiable. La opción sencilla reduce el costo inicial, pero puede dejar débil la regla 'no mostrar una entrega como completada sin evidencia válida'; la opción más estructurada cuesta más, pero facilita probarla y cambiarla. Para el MVP escogería la segunda solo si el riesgo es crítico y documentaría la condición de revisión.

### ❓ ¿Estoy optimizando solo el desarrollo inicial o la sostenibilidad del sistema?

**Respuesta concreta:** Para máquinas de estado y seguridad de aplicaciones, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué tan claro está el sistema para otros miembros del equipo?

**Respuesta concreta:** Para máquinas de estado y seguridad de aplicaciones, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Hay dependencias ocultas que bloquean el trabajo colaborativo?

**Respuesta concreta:** Para máquinas de estado y seguridad de aplicaciones, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa máquinas de estado y seguridad de aplicaciones y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de máquinas de estado y seguridad de aplicaciones:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para máquinas de estado y seguridad de aplicaciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de máquinas de estado y seguridad de aplicaciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La arquitectura tiene un costo real en infraestructura, operación y mantenimiento. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a máquinas de estado y seguridad de aplicaciones: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de máquinas de estado y seguridad de aplicaciones, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Máquinas de estado y seguridad de aplicaciones:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
El software no es solo una decisión técnica: es también una decisión financiera y estratégica. Una arquitectura sostenible es la que crea valor sin generar costos ocultos que la vuelvan inviable con el tiempo.

La arquitectura no solo sirve para resolver un problema técnico; también permite que múltiples personas trabajen de manera coordinada y sostenida. En un equipo distribuido, la claridad arquitectónica es una ventaja de productividad y calidad.

## Preguntas para preparar la grabación
- ¿Qué costo total real tiene mi solución?
- ¿Estoy optimizando solo el desarrollo inicial o la sostenibilidad del sistema?
- ¿Qué tan claro está el sistema para otros miembros del equipo?
- ¿Hay dependencias ocultas que bloquean el trabajo colaborativo?

## Evidencia para el repositorio
Guarda la explicación de máquinas de estado y seguridad de aplicaciones, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
