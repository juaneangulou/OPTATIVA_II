# Video 13: Liderazgo, negociación e impacto social

## Fuentes oficiales
- [Comunicación, liderazgo y negociación técnica](https://platzi.com/cursos/fundamentos-arquitectura-software/evolucion-del-software-personal-hacia-el/)
- [Arquitectura con impacto social y valor real](https://platzi.com/cursos/fundamentos-arquitectura-software/preguntas-clave-que-todo-arquitecto-de-s/)

## 🔗 Navegación
[⬅️ Video anterior](video-12.md) | [➡️ Video siguiente](video-14.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: liderazgo, negociación e impacto social. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Comunicación, liderazgo y negociación técnica**
Este video destaca que una gran parte del trabajo del arquitecto no está en el código, sino en la conversación. Cuando se diseña un sistema, se necesita comunicar decisiones, negociar prioridades y hacer que diferentes actores comprendan por qué se elige una solución y no otra. La arquitectura se fortalece cuando hay claridad, diálogo y liderazgo.

El arquitecto debe ser capaz de escuchar, explicar trade-offs, escuchar preocupaciones y alinear decisiones entre negocio, equipo y usuarios. La negociación técnica no es improvisación; es la capacidad de construir consenso con criterio y equilibrio.

**Fuente 2: Arquitectura con impacto social y valor real**
Este video cierra la dimensión ética y social de la arquitectura. Un sistema no solo debe cumplir con requisitos técnicos; también debe generar valor real para las personas, mejorar procesos y no causar daño. La arquitectura industrial y de software termina teniendo un impacto humano y social, incluso cuando no se nota a simple vista.

La idea es que el valor de una solución no se mide solo por su complejidad o performance, sino por el beneficio real que produce, la confianza que genera y la responsabilidad con quienes la usan. La arquitectura más valiosa es la que crea impacto positivo sin ignorar el contexto social.

## Ideas que debes conservar
- La comunicación es una habilidad arquitectónica central.
- Las decisiones de arquitectura implican balancear intereses distintos.
- El liderazgo técnico ayuda a alinear equipo y visión.
- La negociación permite tomar decisiones sin improvisación.
- La tecnología tiene impacto sobre personas y comunidades.
- El valor real no se mide solo por complejidad o volumen.
- La arquitectura debe generar utilidad y confianza.
- La responsabilidad técnica incluye consecuencias sociales.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: liderazgo, negociación e impacto social. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **liderazgo, negociación e impacto social**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: La comunicación es una habilidad arquitectónica central.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos liderazgo, negociación e impacto social al flujo.
    2. **Actor prioritario de liderazgo, negociación e impacto social:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en liderazgo, negociación e impacto social:** escribe la condición que debe permanecer verdadera y relaciónala con la comunicación es una habilidad arquitectónica central..
    4. **Punto de decisión para liderazgo, negociación e impacto social:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de liderazgo, negociación e impacto social:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **liderazgo, negociación e impacto social**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa liderazgo, negociación e impacto social y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: la comunicación es una habilidad arquitectónica central.
3. Identifica el actor que recibe el impacto de liderazgo, negociación e impacto social y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para liderazgo, negociación e impacto social; compara sus costos y riesgos.
5. Elige una opción para liderazgo, negociación e impacto social, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: liderazgo, negociación e impacto social debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Estoy logrando explicar bien mis decisiones técnicas?

**Respuesta concreta:** Para liderazgo, negociación e impacto social, el cliente necesita recibir un estado de entrega confiable. La respuesta concreta es proteger la regla 'no mostrar una entrega como completada sin evidencia válida' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué conflictos de prioridad están bloqueando el proyecto?

**Respuesta concreta:** Para liderazgo, negociación e impacto social, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué impacto social tiene mi solución?

**Respuesta concreta:** La decisión sobre liderazgo, negociación e impacto social afecta directamente a el repartidor: necesita recibir una instrucción vigente y consistente. Por eso protegería esta regla: evitar dos asignaciones activas para la misma entrega. En la arquitectura cambiaría la responsabilidad para que el componente que conoce esa regla la valide antes de comunicar el resultado. Acepto el costo de agregar una validación y una prueba porque el riesgo de afectar a el repartidor es mayor. Lo verificaría simulando el caso y comprobando el resultado observable para ese actor.

### ❓ ¿Está generando valor real o solo cumpliendo un requisito técnico?

**Respuesta concreta:** Para liderazgo, negociación e impacto social, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa liderazgo, negociación e impacto social y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de liderazgo, negociación e impacto social:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para liderazgo, negociación e impacto social:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de liderazgo, negociación e impacto social:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La comunicación es una habilidad arquitectónica central. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a liderazgo, negociación e impacto social: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de liderazgo, negociación e impacto social, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Liderazgo, negociación e impacto social:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La arquitectura no solo se diseña; también se comunica y se negocia. Un buen arquitecto no solo toma decisiones, sino que logra que el equipo y la organización las entienda y las apoye.

Una buena arquitectura no solo es eficiente técnicamente; también genera valor real para la sociedad y para quienes interactúan con el sistema.

## Preguntas para preparar la grabación
- ¿Estoy logrando explicar bien mis decisiones técnicas?
- ¿Qué conflictos de prioridad están bloqueando el proyecto?
- ¿Qué impacto social tiene mi solución?
- ¿Está generando valor real o solo cumpliendo un requisito técnico?

## Evidencia para el repositorio
Guarda la explicación de liderazgo, negociación e impacto social, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
