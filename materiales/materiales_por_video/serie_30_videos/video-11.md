# Video 11: Evolución, riesgos y costos

## Fuentes oficiales
- [Estructura de software y evolución del sistema](https://platzi.com/cursos/fundamentos-arquitectura-software/patrones-de-software-para-arquitectos/)
- [Riesgos, costos y decisiones bajo incertidumbre](https://platzi.com/cursos/fundamentos-arquitectura-software/arquitectura-mvp-de-telegram-a-remarkabl/)

## 🔗 Navegación
[⬅️ Video anterior](video-10.md) | [➡️ Video siguiente](video-12.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: evolución, riesgos y costos. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Estructura de software y evolución del sistema**
Este video resalta la relación entre la estructura del software y su capacidad de evolución. Los sistemas no son estáticos; cambian con el tiempo, según la carga, el negocio, las reglas y las necesidades del usuario. Por eso, la arquitectura debe permitir cambios sin provocar caos. La estructura del software debe facilitar adaptaciones, no volverlas costosas o riesgosas.

Cuando la estructura del sistema es clara, modular y bien diseñada, el cambio no rompe todo. Cuando está mal organizada, cada ajuste requiere correcciones complejas y difíciles de prever. La evolución del software depende directamente de la calidad de su arquitectura.

**Fuente 2: Riesgos, costos y decisiones bajo incertidumbre**
Este video habla de los riesgos y costos que subyacen a cada decisión arquitectónica. No siempre se tiene toda la información antes de elegir una solución. En ese contexto, el arquitecto debe evaluar qué tan reversible es la decisión, cuál es su costo real y qué riesgos conlleva. La incertidumbre es normal, pero la mala gestión de la misma puede generar decisiones impulsivas o demasiado rígidas.

La toma de decisiones bajo incertidumbre exige criterio: priorizar opciones que permitan aprender, adaptarse y cambiar sin grandes pérdidas. Así, el sistema se vuelve más resiliente frente a cambios de negocio o de contexto.

## Ideas que debes conservar
- El sistema evolucionará; la arquitectura debe anticiparlo.
- La estructura define cuán costoso es cambiar el software.
- Un diseño claro Reduce impacto de cambios y nuevos requerimientos.
- La evolución del sistema requiere capacidad de adaptación.
- La incertidumbre es parte del trabajo arquitectónico.
- Cada decisión tiene costos y riesgos que no siempre son visibles de inmediato.
- La reversibilidad ayuda a decisión bajo cambios.
- La arquitectura debe permitir aprender y ajustar.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: evolución, riesgos y costos. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **evolución, riesgos y costos**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: El sistema evolucionará; la arquitectura debe anticiparlo.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos evolución, riesgos y costos al flujo.
    2. **Actor prioritario de evolución, riesgos y costos:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en evolución, riesgos y costos:** escribe la condición que debe permanecer verdadera y relaciónala con el sistema evolucionará; la arquitectura debe anticiparlo..
    4. **Punto de decisión para evolución, riesgos y costos:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de evolución, riesgos y costos:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **evolución, riesgos y costos**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa evolución, riesgos y costos y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: el sistema evolucionará; la arquitectura debe anticiparlo.
3. Identifica el actor que recibe el impacto de evolución, riesgos y costos y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para evolución, riesgos y costos; compara sus costos y riesgos.
5. Elige una opción para evolución, riesgos y costos, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: evolución, riesgos y costos debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Qué tan costoso es cambiar una parte del sistema hoy?

**Respuesta concreta:** Para evolución, riesgos y costos, elegiría la alternativa que garantice que el cliente pueda recibir un estado de entrega confiable. La opción sencilla reduce el costo inicial, pero puede dejar débil la regla 'no mostrar una entrega como completada sin evidencia válida'; la opción más estructurada cuesta más, pero facilita probarla y cambiarla. Para el MVP escogería la segunda solo si el riesgo es crítico y documentaría la condición de revisión.

### ❓ ¿Qué piezas del software están más rígidas o frágiles?

**Respuesta concreta:** La parte frágil de evolución, riesgos y costos es la que permite que el operador logístico reciba un resultado incorrecto: reasignar una ruta sin perder el historial del pedido. La corregiría colocando la regla 'conservar trazabilidad de cada cambio' en un límite explícito, en lugar de dejarla repartida entre la interfaz y la infraestructura. El costo será reorganizar el flujo y agregar pruebas; la evidencia será un cambio aislado que no rompa los demás módulos.

### ❓ ¿Qué decisiones de mi proyecto se están tomando con mucha incertidumbre?

**Respuesta concreta:** Para evolución, riesgos y costos, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué tan reversible es esta decisión si cambian las condiciones?

**Respuesta concreta:** Para evolución, riesgos y costos, elegiría la alternativa que garantice que el equipo de soporte pueda reconstruir qué ocurrió durante un incidente. La opción sencilla reduce el costo inicial, pero puede dejar débil la regla 'tener eventos, errores y estados observables'; la opción más estructurada cuesta más, pero facilita probarla y cambiarla. Para el MVP escogería la segunda solo si el riesgo es crítico y documentaría la condición de revisión.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa evolución, riesgos y costos y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de evolución, riesgos y costos:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para evolución, riesgos y costos:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de evolución, riesgos y costos:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: El sistema evolucionará; la arquitectura debe anticiparlo. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a evolución, riesgos y costos: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de evolución, riesgos y costos, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Evolución, riesgos y costos:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La capacidad de evolución es una medida de calidad arquitectónica. Los sistemas más sólidos son aquellos que soportan cambios sin destruir su lógica ni su estabilidad.

Bajo incertidumbre, la mejor decisión no siempre es la más ambiciosa, sino la que permite aprender, adaptarse y sostener el sistema con menos riesgo.

## Preguntas para preparar la grabación
- ¿Qué tan costoso es cambiar una parte del sistema hoy?
- ¿Qué piezas del software están más rígidas o frágiles?
- ¿Qué decisiones de mi proyecto se están tomando con mucha incertidumbre?
- ¿Qué tan reversible es esta decisión si cambian las condiciones?

## Evidencia para el repositorio
Guarda la explicación de evolución, riesgos y costos, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
