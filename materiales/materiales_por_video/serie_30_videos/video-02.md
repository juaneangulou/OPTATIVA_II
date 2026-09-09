# Video 02: Rol del arquitecto y comunicación

## Fuentes oficiales
- [Rol del arquitecto de software](https://platzi.com/cursos/fundamentos-arquitectura-software/78360-que-hace-un-arquitecto-de-software/)
- [Comunicar la arquitectura](https://platzi.com/cursos/fundamentos-arquitectura-software/problemas-esenciales-vs-accidentales-en/)

## 🔗 Navegación
[⬅️ Video anterior](video-01.md) | [➡️ Video siguiente](video-03.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: rol del arquitecto y comunicación. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Rol del arquitecto de software**
En este video se redefine el rol del arquitecto, dejando atrás la idea de que solo dibuja diagramas. El arquitecto debe diseñar sistemas sólidos y sostenibles, simplificar la complejidad, cuestionar supuestos y negociar con distintos stakeholders. Además, tiene que entender que cada decisión técnica tiene consecuencias reales.

El trabajo del arquitecto no es imponer una solución elegante por gusto; es crear sistemas confiables, duraderos y bien pensados para el futuro. Esto implica abstraer lo esencial, priorizar la claridad, identificar riesgos y tomar decisiones con criterio técnico y de negocio.

**Fuente 2: Comunicar la arquitectura**
El video resalta un problema muy común: la falta de claridad a la hora de documentar decisiones. Cuando la arquitectura no se comunica bien, el mantenimiento, la evolución y la comprensión del sistema se vuelven mucho más difíciles. El resultado es un proyecto más frágil y más costoso de sostener.

La solución propuesta es crear un archivo ARCHITECTURE.md en la raíz del repositorio. Ese documento debe explicar el propósito del software, sus módulos, sus restricciones y los riesgos más importantes. La idea es que la arquitectura sea comprensible y que cualquiera pueda entenderla sin tener que leer todo el sistema desde cero.

## Ideas que debes conservar
- El arquitecto no es solo un dibujante de diagramas.
- Debe abstraer la complejidad y simplificar lo esencial.
- Tiene que cuestionar supuestos, tanto técnicos como de negocio.
- Debe negociar con usuarios, directivos y equipo.
- La falta de documentación dificulta mantenimiento y evolución.
- La arquitectura debe ser comunicada, no solo construida.
- Un ARCHITECTURE.md ayuda a dejar claridad documental del sistema.
- Debe incluir propósito general, módulos principales y restricciones.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: rol del arquitecto y comunicación. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **rol del arquitecto y comunicación**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: El arquitecto no es solo un dibujante de diagramas.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos rol del arquitecto y comunicación al flujo.
    2. **Actor prioritario de rol del arquitecto y comunicación:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en rol del arquitecto y comunicación:** escribe la condición que debe permanecer verdadera y relaciónala con el arquitecto no es solo un dibujante de diagramas..
    4. **Punto de decisión para rol del arquitecto y comunicación:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de rol del arquitecto y comunicación:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **rol del arquitecto y comunicación**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa rol del arquitecto y comunicación y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: el arquitecto no es solo un dibujante de diagramas.
3. Identifica el actor que recibe el impacto de rol del arquitecto y comunicación y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para rol del arquitecto y comunicación; compara sus costos y riesgos.
5. Elige una opción para rol del arquitecto y comunicación, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: rol del arquitecto y comunicación debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Qué tan claro es mi papel como arquitecto o líder técnico en el proyecto?

**Respuesta concreta:** Para rol del arquitecto y comunicación, el cliente necesita recibir un estado de entrega confiable. La respuesta concreta es proteger la regla 'no mostrar una entrega como completada sin evidencia válida' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Estoy cuestionando suposiciones o aceptando decisiones sin analizar consecuencias?

**Respuesta concreta:** La decisión sobre rol del arquitecto y comunicación afecta directamente a el operador logístico: necesita reasignar una ruta sin perder el historial del pedido. Por eso protegería esta regla: conservar trazabilidad de cada cambio. En la arquitectura cambiaría la responsabilidad para que el componente que conoce esa regla la valide antes de comunicar el resultado. Acepto el costo de agregar una validación y una prueba porque el riesgo de afectar a el operador logístico es mayor. Lo verificaría simulando el caso y comprobando el resultado observable para ese actor.

### ❓ ¿Mi proyecto está documentado lo suficiente para entender su propósito?

**Respuesta concreta:** Para rol del arquitecto y comunicación, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué tan fácil es para otra persona entender la arquitectura actual?

**Respuesta concreta:** Para rol del arquitecto y comunicación, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa rol del arquitecto y comunicación y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de rol del arquitecto y comunicación:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para rol del arquitecto y comunicación:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de rol del arquitecto y comunicación:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: El arquitecto no es solo un dibujante de diagramas. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a rol del arquitecto y comunicación: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de rol del arquitecto y comunicación, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Rol del arquitecto y comunicación:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
El papel del arquitecto es más amplio que la solución técnica: es diseñar sistemas con estrategia, criterio y responsabilidad. La arquitectura sirve para transformar complejidad en claridad.

El sistema no solo debe funcionar; también debe entenderse. Comunicar la arquitectura es una práctica que mejora la sostenibilidad del proyecto y reduce la deuda técnica.

## Preguntas para preparar la grabación
- ¿Qué tan claro es mi papel como arquitecto o líder técnico en el proyecto?
- ¿Estoy cuestionando suposiciones o aceptando decisiones sin analizar consecuencias?
- ¿Mi proyecto está documentado lo suficiente para entender su propósito?
- ¿Qué tan fácil es para otra persona entender la arquitectura actual?

## Evidencia para el repositorio
Guarda la explicación de rol del arquitecto y comunicación, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
