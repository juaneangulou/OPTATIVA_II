# Video 21: Métricas y migración Strangler Fig

## Fuentes oficiales
- [Observabilidad y operabilidad](https://platzi.com/cursos/software-avanzado/metricas-cuantitativas-para-evaluar-arqu/)
- [DevOps, despliegue y automatización](https://platzi.com/cursos/software-avanzado/strangler-fig-para-migrar-arquitecturas/)

## 🔗 Navegación
[⬅️ Video anterior](video-20.md) | [➡️ Video siguiente](video-22.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: métricas y migración strangler fig. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Observabilidad y operabilidad**
El video destaca que una arquitectura no termina cuando el sistema “funciona” en un entorno local. La verdadera prueba de madurez llega cuando el equipo puede entender qué está sucediendo en producción, detectar fallos y responder con rapidez. Por eso la observabilidad es una parte esencial del diseño: métricas, logs, trazas y alertas ayudan a transformar el sistema en algo operable y diagnósticable.

Cuando una solución no es observable, el equipo se mueve a ciegas y las correcciones se vuelven reactivas. La operabilidad mejora cuando se diseña para monitoreo, diagnóstico y recuperación. El video deja claro que observar el sistema es una decisión arquitectónica, no un extra de operaciones.

**Fuente 2: DevOps, despliegue y automatización**
Este video conecta arquitectura con entrega continua y operación real. La forma en que se despliega una aplicación afecta directamente la estabilidad, velocidad y capacidad de innovación del equipo. Cuando el despliegue es manual, propenso a errores o difícil de repetir, la arquitectura se vuelve frágil incluso si el diseño técnico es bueno.

La automatización del despliegue, la integración continua, la orquestación y la infraestructura como código permiten que el sistema evolucione con menos riesgos. El video muestra que la arquitectura moderna no se limita a la aplicación, sino al flujo completo de entrega: código, integración, pruebas, despliegue, observabilidad y rollback. Esto hace que la calidad del sistema dependa también del proceso que lo lleva a producción.

## Ideas que debes conservar
- La observabilidad permite entender el comportamiento real del sistema.
- Logs, métricas y trazas ayudan a detectar fallas y cuellos de botella.
- Un sistema difícil de diagnosticar termina costando más en producción.
- La operación debe estar integrada en el diseño desde el principio.
- El despliegue es parte de la arquitectura, no una etapa separada.
- La automatización reduce errores humanos y acelera la entrega.
- La infraestructura debe ser reproducible y controlada.
- La calidad del proceso impacta la calidad del sistema.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: métricas y migración strangler fig. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **métricas y migración strangler fig**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: La observabilidad permite entender el comportamiento real del sistema.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos métricas y migración strangler fig al flujo.
    2. **Actor prioritario de métricas y migración strangler fig:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en métricas y migración strangler fig:** escribe la condición que debe permanecer verdadera y relaciónala con la observabilidad permite entender el comportamiento real del sistema..
    4. **Punto de decisión para métricas y migración strangler fig:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de métricas y migración strangler fig:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **métricas y migración strangler fig**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa métricas y migración strangler fig y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: la observabilidad permite entender el comportamiento real del sistema.
3. Identifica el actor que recibe el impacto de métricas y migración strangler fig y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para métricas y migración strangler fig; compara sus costos y riesgos.
5. Elige una opción para métricas y migración strangler fig, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: métricas y migración strangler fig debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Qué tanto sabemos realmente qué está pasando en producción?

**Respuesta concreta:** Para métricas y migración strangler fig, el cliente necesita recibir un estado de entrega confiable. La respuesta concreta es proteger la regla 'no mostrar una entrega como completada sin evidencia válida' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Mi sistema me alerta antes de que el usuario lo note?

**Respuesta concreta:** Para métricas y migración strangler fig, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Mi despliegue es repetible y automatizado?

**Respuesta concreta:** Para métricas y migración strangler fig, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué tan rápido puedo revertir un cambio problemático?

**Respuesta concreta:** Para métricas y migración strangler fig, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa métricas y migración strangler fig y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de métricas y migración strangler fig:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para métricas y migración strangler fig:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de métricas y migración strangler fig:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La observabilidad permite entender el comportamiento real del sistema. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a métricas y migración strangler fig: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de métricas y migración strangler fig, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Métricas y migración Strangler Fig:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
Un sistema bien diseñado no solo responde a requerimientos, sino que también puede ser comprendido y mantenido en producción. La observabilidad es uno de los pilares para convertir una solución técnica en una solución operable.

La arquitectura moderna integra desarrollo, operación y entrega. Un sistema no se considera bien diseñado si no puede entregarse, operar y evolucionar de manera segura y repetible.

## Preguntas para preparar la grabación
- ¿Qué tanto sabemos realmente qué está pasando en producción?
- ¿Mi sistema me alerta antes de que el usuario lo note?
- ¿Mi despliegue es repetible y automatizado?
- ¿Qué tan rápido puedo revertir un cambio problemático?

## Evidencia para el repositorio
Guarda la explicación de métricas y migración strangler fig, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
