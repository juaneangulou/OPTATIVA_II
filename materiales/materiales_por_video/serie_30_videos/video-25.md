# Video 25: Dead Letter Queue y consumidores en tiempo real

## Fuentes oficiales
- [Diseño para cambio y evolución](https://platzi.com/cursos/software-avanzado/dead-letter-queue-en-productor-consumido/)
- [Calidad de servicio y experiencia de usuario](https://platzi.com/cursos/software-avanzado/patron-comparing-consumers-para-procesam/)

## 🔗 Navegación
[⬅️ Video anterior](video-24.md) | [➡️ Video siguiente](video-26.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: dead letter queue y consumidores en tiempo real. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Diseño para cambio y evolución**
Este video introduce una de las ideas más importantes de la arquitectura moderna: un sistema no solo debe resolver el problema actual, sino prepararse para cambiar cuando cambien las necesidades del negocio o el contexto. El diseño arquitectónico debe pensar en la evolución como una variable esperada, no como una excepción. Por eso se enfatizan principios como la modularidad, la flexibilidad, la separación de responsabilidades y la protección de las capas críticas del sistema.

Cuando el software se diseña para el cambio, se vuelve más sostenible. En cambio, si se construye como una estructura rígida y demasiado acoplada, cualquier cambio pequeño termina convirtiéndose en una tarea riesgosa. La arquitectura entonces deja de ser una estructura estática y pasa a ser una base que permite crecer y adaptarse con menos fricción.

**Fuente 2: Calidad de servicio y experiencia de usuario**
La arquitectura de software no solo se mide por qué tan bien se ejecuta internamente, sino por la experiencia que entrega a quienes la usan. Si el sistema es técnicamente sólido pero lento, poco intuitivo o inconsistente, la arquitectura termina fallando en la práctica. Este video conecta calidad técnica con calidad percibida por el usuario: tiempo de respuesta, confiabilidad, claridad, disponibilidad y consistencia.

Cuando el sistema es parte de una experiencia de negocio, la calidad de servicio se vuelve una necesidad de diseño. Un sistema puede estar bien estructurado, pero si no entrega valor de forma clara y confiable, no cumple su propósito. La arquitectura debe aportar experiencia y resultados, no solo estructura interna.

## Ideas que debes conservar
- La evolución es una característica normal del software, no un problema excepcional.
- Un buen diseño reduce el costo de cambiar.
- La modularidad permite aislar áreas del sistema y facilitar adaptaciones.
- La arquitectura debe proteger los puntos sensibles del negocio.
- La experiencia del usuario es una consecuencia del diseño arquitectónico.
- Calidad técnica y calidad de servicio no son conceptos separados.
- El tiempo de respuesta, la estabilidad y la claridad influyen en la percepción del sistema.
- Un servicio bueno no solo funciona; funciona con un nivel de calidad soportable.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: dead letter queue y consumidores en tiempo real. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **dead letter queue y consumidores en tiempo real**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: La evolución es una característica normal del software, no un problema excepcional.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos dead letter queue y consumidores en tiempo real al flujo.
    2. **Actor prioritario de dead letter queue y consumidores en tiempo real:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en dead letter queue y consumidores en tiempo real:** escribe la condición que debe permanecer verdadera y relaciónala con la evolución es una característica normal del software, no un problema excepcional..
    4. **Punto de decisión para dead letter queue y consumidores en tiempo real:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de dead letter queue y consumidores en tiempo real:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **dead letter queue y consumidores en tiempo real**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa dead letter queue y consumidores en tiempo real y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: la evolución es una característica normal del software, no un problema excepcional.
3. Identifica el actor que recibe el impacto de dead letter queue y consumidores en tiempo real y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para dead letter queue y consumidores en tiempo real; compara sus costos y riesgos.
5. Elige una opción para dead letter queue y consumidores en tiempo real, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: dead letter queue y consumidores en tiempo real debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Qué partes de mi sistema son difíciles de cambiar?

**Respuesta concreta:** Para dead letter queue y consumidores en tiempo real, el cliente necesita recibir un estado de entrega confiable. La respuesta concreta es proteger la regla 'no mostrar una entrega como completada sin evidencia válida' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Estoy diseñando para el futuro o solo para la versión actual?

**Respuesta concreta:** Si el sistema crece en el tema de dead letter queue y consumidores en tiempo real, el operador logístico seguirá necesitando reasignar una ruta sin perder el historial del pedido. No elegiría una solución distribuida automáticamente; primero mediría carga, latencia y errores. Mantendría la regla 'conservar trazabilidad de cada cambio' en un módulo claro y escalaría solo el punto que demuestre saturación. La decisión se verifica con una prueba de carga y una métrica acordada.

### ❓ ¿Qué tan buena es la experiencia de uso de mi sistema?

**Respuesta concreta:** Para dead letter queue y consumidores en tiempo real, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué factores técnicos afectan la percepción del usuario?

**Respuesta concreta:** Para dead letter queue y consumidores en tiempo real, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa dead letter queue y consumidores en tiempo real y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de dead letter queue y consumidores en tiempo real:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para dead letter queue y consumidores en tiempo real:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de dead letter queue y consumidores en tiempo real:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La evolución es una característica normal del software, no un problema excepcional. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a dead letter queue y consumidores en tiempo real: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de dead letter queue y consumidores en tiempo real, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Dead Letter Queue y consumidores en tiempo real:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La arquitectura más útil es la que acepta que el sistema cambiará. Cuando el diseño está preparado para la evolución, el software se vuelve más robusto, adaptable y sostenible.

La arquitectura debe diseñarse para entregar valor no solo dentro del equipo técnico, sino también en la experiencia real del usuario. La calidad de servicio aparece como indicador de que la solución responde bien a las necesidades del entorno.

## Preguntas para preparar la grabación
- ¿Qué partes de mi sistema son difíciles de cambiar?
- ¿Estoy diseñando para el futuro o solo para la versión actual?
- ¿Qué tan buena es la experiencia de uso de mi sistema?
- ¿Qué factores técnicos afectan la percepción del usuario?

## Evidencia para el repositorio
Guarda la explicación de dead letter queue y consumidores en tiempo real, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
