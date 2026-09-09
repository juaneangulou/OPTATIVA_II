# Video 16: Monorepos, trunk-based development y calidad

## Fuentes oficiales
- [Contexto, negocio y decisiones arquitectónicas](https://platzi.com/cursos/software-avanzado/monorepos-con-pantsbuild-en-proyectos-re/)
- [Principios, calidad y trade-offs](https://platzi.com/cursos/software-avanzado/trunk-based-development-con-rulesets-en/)

## 🔗 Navegación
[⬅️ Video anterior](video-15.md) | [➡️ Video siguiente](video-17.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: monorepos, trunk-based development y calidad. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Contexto, negocio y decisiones arquitectónicas**
El video muestra que la arquitectura de software no se construye en un vacío técnico. Cada decisión depende del contexto del negocio, los objetivos del cliente, las personas involucradas, las restricciones de tiempo, costo, seguridad y operación. Un sistema excelente para un caso puede ser inútil para otro si no se toma en cuenta el entorno.

Por eso, el arquitecto debe interpretar no solo requisitos funcionales, sino también necesidades de negocio, riesgos, evolución esperada, experiencia del usuario y capacidad operativa del equipo. La arquitectura deja de ser una actividad puramente técnica y se convierte en una actividad de análisis, negociación y toma de decisiones. En otras palabras, no se diseña solo para resolver un problema lógico; se diseña para resolver un problema real dentro de un contexto real.

**Fuente 2: Principios, calidad y trade-offs**
Este video habla de una realidad central en arquitectura de software: no existe una solución perfecta para todos los casos, sino decisiones que equilibran objetivos en conflicto. A menudo el equipo quiere velocidad, el negocio quiere menor costo, la operación quiere estabilidad y el usuario quiere experiencia rápida. La arquitectura de software consiste en resolver esas tensiones con criterio técnico y estratégico.

La idea principal es que la calidad del diseño no se mide solo por cuán elegante es, sino por cuán bien se adapta al problema real. Un sistema puede ser técnicamente sofisticado y aun así ser un mal diseño si no considera costo, complejidad, operatividad y capacidad de evolución. El video enfatiza la importancia de principios, ya que los principios ayudan a tomar decisiones cuando no hay una respuesta única.

## Ideas que debes conservar
- Los requisitos técnicos no son suficientes; el negocio da la forma de la solución.
- El contexto define qué es una buena decisión y qué no lo es.
- Un gran diseño debe equilibrar funcionalidad, costos, tiempo y complejidad.
- El arquitecto actúa como traductor entre negocio y tecnología.
- No todo en arquitectura es absoluto; muchas decisiones implican trade-offs.
- La calidad del diseño depende del contexto, no de una fórmula universal.
- Un sistema debe balancear velocidad, claridad, costo, rendimiento y sostenibilidad.
- Los principios técnicos ayudan a evitar decisiones impulsivas o improvisadas.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: monorepos, trunk-based development y calidad. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **monorepos, trunk-based development y calidad**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: Los requisitos técnicos no son suficientes; el negocio da la forma de la solución.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos monorepos, trunk-based development y calidad al flujo.
    2. **Actor prioritario de monorepos, trunk-based development y calidad:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en monorepos, trunk-based development y calidad:** escribe la condición que debe permanecer verdadera y relaciónala con los requisitos técnicos no son suficientes; el negocio da la forma de la solución..
    4. **Punto de decisión para monorepos, trunk-based development y calidad:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de monorepos, trunk-based development y calidad:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **monorepos, trunk-based development y calidad**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa monorepos, trunk-based development y calidad y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: los requisitos técnicos no son suficientes; el negocio da la forma de la solución.
3. Identifica el actor que recibe el impacto de monorepos, trunk-based development y calidad y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para monorepos, trunk-based development y calidad; compara sus costos y riesgos.
5. Elige una opción para monorepos, trunk-based development y calidad, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: monorepos, trunk-based development y calidad debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Qué restricciones del negocio están impactando mi diseño actual?

**Respuesta concreta:** La parte frágil de monorepos, trunk-based development y calidad es la que permite que el cliente reciba un resultado incorrecto: recibir un estado de entrega confiable. La corregiría colocando la regla 'no mostrar una entrega como completada sin evidencia válida' en un límite explícito, en lugar de dejarla repartida entre la interfaz y la infraestructura. El costo será reorganizar el flujo y agregar pruebas; la evidencia será un cambio aislado que no rompa los demás módulos.

### ❓ ¿Estoy resolviendo el problema real o solo la versión técnica de ese problema?

**Respuesta concreta:** Para monorepos, trunk-based development y calidad, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué trade-off estoy asumiendo sin darme cuenta en mi proyecto?

**Respuesta concreta:** Para monorepos, trunk-based development y calidad, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Estoy priorizando la solución más elegante o la más adecuada?

**Respuesta concreta:** Para monorepos, trunk-based development y calidad, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa monorepos, trunk-based development y calidad y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de monorepos, trunk-based development y calidad:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para monorepos, trunk-based development y calidad:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de monorepos, trunk-based development y calidad:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: Los requisitos técnicos no son suficientes; el negocio da la forma de la solución. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a monorepos, trunk-based development y calidad: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de monorepos, trunk-based development y calidad, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Monorepos, trunk-based development y calidad:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
Una buena arquitectura no se mide solo por su elegancia técnica, sino por su capacidad de responder a un problema auténtico con sentido de negocio. El mejor diseño es aquel que sirve al contexto y no el que solo parece bonito desde el punto de vista teórico.

La arquitectura no es una búsqueda de perfección abstracta, sino de equilibrio. El arquitecto debe aprender a elegir entre alternativas con sentido, entendiendo que cada decisión tiene consecuencias en costo, mantenimiento y evolución del sistema.

## Preguntas para preparar la grabación
- ¿Qué restricciones del negocio están impactando mi diseño actual?
- ¿Estoy resolviendo el problema real o solo la versión técnica de ese problema?
- ¿Qué trade-off estoy asumiendo sin darme cuenta en mi proyecto?
- ¿Estoy priorizando la solución más elegante o la más adecuada?

## Evidencia para el repositorio
Guarda la explicación de monorepos, trunk-based development y calidad, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
