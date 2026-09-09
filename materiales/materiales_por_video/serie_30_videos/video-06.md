# Video 06: Dominios y límites de contexto

## Fuentes oficiales
- [Modelado de dominios y límites de contexto](https://platzi.com/cursos/fundamentos-arquitectura-software/mindset-del-arquitecto-que-abraza-el-cam/)
- [Diseño para cambio y evolución](https://platzi.com/cursos/software-avanzado/dead-letter-queue-en-productor-consumido/)

## 🔗 Navegación
[⬅️ Video anterior](video-05.md) | [➡️ Video siguiente](video-07.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: dominios y límites de contexto. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Modelado de dominios y límites de contexto**
Este video habla sobre un enfoque clásico en arquitectura: modelar el dominio del negocio y definir límites claros entre contextos. El objetivo es separar áreas con responsabilidades distintas para evitar mezclar conceptos y reglas de negocio que no pertenecen al mismo problema. Cuando esto no se hace, el sistema termina con lógica mezclada, reglas contradictorias y mayor complejidad.

El modelado del dominio permite entender mejor qué es lo que realmente hace el negocio, y cómo la solución debe reflejarlo. Los límites de contexto ayudan a definir dónde termina una responsabilidad y comienza otra, reduciendo confusión en la lógica del sistema.

**Fuente 2: Diseño para cambio y evolución**
Este video introduce una de las ideas más importantes de la arquitectura moderna: un sistema no solo debe resolver el problema actual, sino prepararse para cambiar cuando cambien las necesidades del negocio o el contexto. El diseño arquitectónico debe pensar en la evolución como una variable esperada, no como una excepción. Por eso se enfatizan principios como la modularidad, la flexibilidad, la separación de responsabilidades y la protección de las capas críticas del sistema.

Cuando el software se diseña para el cambio, se vuelve más sostenible. En cambio, si se construye como una estructura rígida y demasiado acoplada, cualquier cambio pequeño termina convirtiéndose en una tarea riesgosa. La arquitectura entonces deja de ser una estructura estática y pasa a ser una base que permite crecer y adaptarse con menos fricción.

## Ideas que debes conservar
- El dominio del negocio debe reflejarse en la estructura del software.
- Los límites de contexto ayudan a ordenar responsabilidades.
- Mezclar dominios distintos genera confusión y errores.
- Un diseño basado en el dominio es más comprensible y sostenible.
- La evolución es una característica normal del software, no un problema excepcional.
- Un buen diseño reduce el costo de cambiar.
- La modularidad permite aislar áreas del sistema y facilitar adaptaciones.
- La arquitectura debe proteger los puntos sensibles del negocio.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: dominios y límites de contexto. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **dominios y límites de contexto**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: El dominio del negocio debe reflejarse en la estructura del software.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos dominios y límites de contexto al flujo.
    2. **Actor prioritario de dominios y límites de contexto:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en dominios y límites de contexto:** escribe la condición que debe permanecer verdadera y relaciónala con el dominio del negocio debe reflejarse en la estructura del software..
    4. **Punto de decisión para dominios y límites de contexto:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de dominios y límites de contexto:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **dominios y límites de contexto**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa dominios y límites de contexto y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: el dominio del negocio debe reflejarse en la estructura del software.
3. Identifica el actor que recibe el impacto de dominios y límites de contexto y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para dominios y límites de contexto; compara sus costos y riesgos.
5. Elige una opción para dominios y límites de contexto, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: dominios y límites de contexto debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Mi sistema mezcla conceptos de diferentes dominios?

**Respuesta concreta:** Para dominios y límites de contexto, el cliente necesita recibir un estado de entrega confiable. La respuesta concreta es proteger la regla 'no mostrar una entrega como completada sin evidencia válida' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Dónde está el límite claro entre áreas funcionales?

**Respuesta concreta:** Para dominios y límites de contexto, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué partes de mi sistema son difíciles de cambiar?

**Respuesta concreta:** Para dominios y límites de contexto, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Estoy diseñando para el futuro o solo para la versión actual?

**Respuesta concreta:** Si el sistema crece en el tema de dominios y límites de contexto, el equipo de soporte seguirá necesitando reconstruir qué ocurrió durante un incidente. No elegiría una solución distribuida automáticamente; primero mediría carga, latencia y errores. Mantendría la regla 'tener eventos, errores y estados observables' en un módulo claro y escalaría solo el punto que demuestre saturación. La decisión se verifica con una prueba de carga y una métrica acordada.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa dominios y límites de contexto y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de dominios y límites de contexto:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para dominios y límites de contexto:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de dominios y límites de contexto:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: El dominio del negocio debe reflejarse en la estructura del software. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a dominios y límites de contexto: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de dominios y límites de contexto, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Dominios y límites de contexto:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
Modelar correctamente el dominio y definir límites de contexto es esencial para crear sistemas más claros y coherentes con la realidad del negocio.

La arquitectura más útil es la que acepta que el sistema cambiará. Cuando el diseño está preparado para la evolución, el software se vuelve más robusto, adaptable y sostenible.

## Preguntas para preparar la grabación
- ¿Mi sistema mezcla conceptos de diferentes dominios?
- ¿Dónde está el límite claro entre áreas funcionales?
- ¿Qué partes de mi sistema son difíciles de cambiar?
- ¿Estoy diseñando para el futuro o solo para la versión actual?

## Evidencia para el repositorio
Guarda la explicación de dominios y límites de contexto, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
