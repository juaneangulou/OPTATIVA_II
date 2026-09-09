# Video 10: Testing, DevOps y entrega continua

## Fuentes oficiales
- [Testing y validación de arquitectura](https://platzi.com/cursos/fundamentos-arquitectura-software/paradigmas-y-principios-solid-explicados/)
- [DevOps y automatización de entrega](https://platzi.com/cursos/fundamentos-arquitectura-software/que-hace-limpia-a-una-arquitectura-de-so/)

## 🔗 Navegación
[⬅️ Video anterior](video-09.md) | [➡️ Video siguiente](video-11.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: testing, devops y entrega continua. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Testing y validación de arquitectura**
En este video se explica que la arquitectura no debe validarse solo con la ejecución del sistema en un entorno feliz. También debe evaluarse mediante pruebas, simulaciones, revisión de calidad y validación de dependencias. La validación arquitectónica permite corroborar que el sistema cumple con expectativas de rendimiento, confiabilidad, seguridad y facilidad de evolución.

Cuando se hace testing de arquitectura, se busca detectar problemas estructurales antes de que creen deuda técnica o incidentes en producción. La calidad de una solución no siempre se ve al principio, por eso se requiere una evaluación más profunda que la simple funcionalidad básica.

**Fuente 2: DevOps y automatización de entrega**
Este video conecta arquitectura con entrega continua. La forma en que se construye, prueba, despliega y opera una aplicación influye directamente en su calidad. Si el proceso de entrega es manual y poco repetible, el sistema será más frágil incluso si su diseño inicial es bueno. Por eso DevOps y automatización son parte interesante de la arquitectura moderna.

La entrega automatizada permite reducir errores humanos, aumentar velocidad, mejorar reusabilidad y hacer más segura la evolución del sistema. El objetivo no es solo desplegar más rápido, sino hacerlo de manera controlada y confiable.

## Ideas que debes conservar
- La arquitectura debe validarse con criterios más allá del “funciona”.
- Las pruebas ayudan a detectar riesgos estructurales.
- La validación reduce la probabilidad de fallos costosos.
- La calidad del diseño se confirma con observación y pruebas.
- La entrega continua es parte de la arquitectura.
- La automatización reduce errores y acelera cambios seguros.
- Las pruebas y despliegues deben ser repetibles y controlados.
- La operación y el desarrollo deben alinearse en un mismo flujo.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: testing, devops y entrega continua. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **testing, devops y entrega continua**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: La arquitectura debe validarse con criterios más allá del “funciona”.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos testing, devops y entrega continua al flujo.
    2. **Actor prioritario de testing, devops y entrega continua:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en testing, devops y entrega continua:** escribe la condición que debe permanecer verdadera y relaciónala con la arquitectura debe validarse con criterios más allá del “funciona”..
    4. **Punto de decisión para testing, devops y entrega continua:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de testing, devops y entrega continua:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **testing, devops y entrega continua**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa testing, devops y entrega continua y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: la arquitectura debe validarse con criterios más allá del “funciona”.
3. Identifica el actor que recibe el impacto de testing, devops y entrega continua y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para testing, devops y entrega continua; compara sus costos y riesgos.
5. Elige una opción para testing, devops y entrega continua, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: testing, devops y entrega continua debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Qué tan bien validamos la estructura de mi sistema?

**Respuesta concreta:** Para testing, devops y entrega continua, el cliente necesita recibir un estado de entrega confiable. La respuesta concreta es proteger la regla 'no mostrar una entrega como completada sin evidencia válida' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué tan fácil es detectar un problema arquitectónico antes de producción?

**Respuesta concreta:** Para testing, devops y entrega continua, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué tan automatizado está mi proceso de entrega?

**Respuesta concreta:** Para testing, devops y entrega continua, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué riesgos se reducen o aumentan con el flujo actual?

**Respuesta concreta:** Para testing, devops y entrega continua, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa testing, devops y entrega continua y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de testing, devops y entrega continua:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para testing, devops y entrega continua:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de testing, devops y entrega continua:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La arquitectura debe validarse con criterios más allá del “funciona”. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a testing, devops y entrega continua: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de testing, devops y entrega continua, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Testing, DevOps y entrega continua:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
Un sistema técnico no queda validado solo por tener casos de éxito; necesita pruebas y evaluación que confirmen que su estructura soporta el presente y el crecimiento futuro.

La automatización de entrega no es solo una práctica operativa, sino una decisión arquitectónica que mejora confiabilidad, velocidad y sostenibilidad.

## Preguntas para preparar la grabación
- ¿Qué tan bien validamos la estructura de mi sistema?
- ¿Qué tan fácil es detectar un problema arquitectónico antes de producción?
- ¿Qué tan automatizado está mi proceso de entrega?
- ¿Qué riesgos se reducen o aumentan con el flujo actual?

## Evidencia para el repositorio
Guarda la explicación de testing, devops y entrega continua, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
