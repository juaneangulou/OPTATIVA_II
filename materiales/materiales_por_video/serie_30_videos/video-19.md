# Video 19: Architecture.md y Domain Driven Design

## Fuentes oficiales
- [Seguridad y privacidad](https://platzi.com/cursos/software-avanzado/estructura-del-archivo-architecture-md-p/)
- [Integración y contratos de API](https://platzi.com/cursos/software-avanzado/domain-driven-design-para-arquitectura-l/)

## 🔗 Navegación
[⬅️ Video anterior](video-18.md) | [➡️ Video siguiente](video-20.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: architecture.md y domain driven design. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Seguridad y privacidad**
La seguridad es una parte esencial de la arquitectura, no un tema opcional que se resuelve al final. Un sistema puede ser rápido y funcional, pero si no maneja bien autenticación, autorización, cifrado, validación de datos y control de acceso, puede poner en riesgo información crítica y la confianza del usuario. El video llama la atención sobre el hecho de que los problemas de seguridad no siempre aparecen como fallas técnicas evidentes: muchas veces son decisiones de diseño que dejan brechas invisibles.

También se habla de privacidad como un principio arquitectónico, no solo como cumplimiento. Diseñar con privacidad implica limitar datos, controlar acceso, definir responsabilidades y evitar recopilar más información de la necesaria. La arquitectura debe pensar en la seguridad desde las capas más básicas hasta el comportamiento del sistema en producción.

**Fuente 2: Integración y contratos de API**
La mayoría de sistemas modernos no existen aislados: dependen de servicios, clientes, proveedores y otras aplicaciones. Por eso, la capacidad de integrar componentes de forma clara y segura es crucial. Este video habla de las APIs como contratos entre sistemas: si esos contratos son ambiguos o cambian sin control, el sistema entera se vuelve frágil y difícil de mantener.

Se enfatiza la idea de que una API no es solo una ruta o un endpoint; es una interfaz formal de comunicación entre partes. Cuando se diseña bien, facilita la colaboración, reduce errores y mejora la evolución del sistema. Cuando se diseña mal, genera compatibilidad, dependencia y cambios difíciles de gestionar.

## Ideas que debes conservar
- La seguridad debe ser un eje arquitectónico, no un detalle a último momento.
- La confianza del usuario depende del manejo responsable de datos.
- Hay que proteger no solo la aplicación, sino sus flujos de datos y sus dependencias.
- La privacidad implica principio de mínimo privilegio y minimización de datos.
- Las APIs son contratos que facilitan la integración entre sistemas.
- Cambios sin versionado pueden romper dependencias.
- Debe existir claridad en formatos, validaciones, errores y semántica.
- La integración eficiente reduce riesgos de acoplamiento y mejora la escalabilidad.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: architecture.md y domain driven design. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **architecture.md y domain driven design**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: La seguridad debe ser un eje arquitectónico, no un detalle a último momento.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos architecture.md y domain driven design al flujo.
    2. **Actor prioritario de architecture.md y domain driven design:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en architecture.md y domain driven design:** escribe la condición que debe permanecer verdadera y relaciónala con la seguridad debe ser un eje arquitectónico, no un detalle a último momento..
    4. **Punto de decisión para architecture.md y domain driven design:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de architecture.md y domain driven design:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **architecture.md y domain driven design**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa architecture.md y domain driven design y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: la seguridad debe ser un eje arquitectónico, no un detalle a último momento.
3. Identifica el actor que recibe el impacto de architecture.md y domain driven design y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para architecture.md y domain driven design; compara sus costos y riesgos.
5. Elige una opción para architecture.md y domain driven design, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: architecture.md y domain driven design debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Qué datos sensibles maneja mi sistema?

**Respuesta concreta:** La prioridad de architecture.md y domain driven design es proteger a el cliente, porque recibir un estado de entrega confiable. Aplicaría un control que impida violar la regla 'no mostrar una entrega como completada sin evidencia válida', limitaría el acceso a los datos necesarios y registraría los intentos rechazados. El costo es mayor complejidad de autorización y auditoría; lo comprobaría con pruebas de acceso permitido y denegado.

### ❓ ¿Estoy limitando el acceso y la exposición de información de forma consciente?

**Respuesta concreta:** Para architecture.md y domain driven design, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Mis APIs están documentadas y versionadas de forma clara?

**Respuesta concreta:** Para architecture.md y domain driven design, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué pasa si un cliente usa una versión anterior?

**Respuesta concreta:** Para architecture.md y domain driven design, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa architecture.md y domain driven design y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de architecture.md y domain driven design:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para architecture.md y domain driven design:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de architecture.md y domain driven design:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La seguridad debe ser un eje arquitectónico, no un detalle a último momento. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a architecture.md y domain driven design: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de architecture.md y domain driven design, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Architecture.md y Domain Driven Design:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
Un sistema con buena arquitectura no solo resuelve necesidades funcionales, sino que protege la información, reduce riesgos y genera confianza. La seguridad y la privacidad no se agregan al final: se diseñan desde el principio.

Las integraciones son una parte central de la arquitectura moderna. Si las APIs no están bien definidas, la evolución del sistema se vuelve costosa y frágil. Diseñar contratos claros es una capacidad esencial del arquitecto.

## Preguntas para preparar la grabación
- ¿Qué datos sensibles maneja mi sistema?
- ¿Estoy limitando el acceso y la exposición de información de forma consciente?
- ¿Mis APIs están documentadas y versionadas de forma clara?
- ¿Qué pasa si un cliente usa una versión anterior?

## Evidencia para el repositorio
Guarda la explicación de architecture.md y domain driven design, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
