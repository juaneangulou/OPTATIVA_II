# Video 20: Premortem y pruebas de arquitectura

## Fuentes oficiales
- [Microservicios y dominios](https://platzi.com/cursos/software-avanzado/tecnicas-pre-mortem-y-cinco-why-para-pre/)
- [Datos y almacenamiento](https://platzi.com/cursos/software-avanzado/como-el-premortem-guia-tus-tests-de-arqu/)

## 🔗 Navegación
[⬅️ Video anterior](video-19.md) | [➡️ Video siguiente](video-21.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: premortem y pruebas de arquitectura. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Microservicios y dominios**
Este video analiza una de las decisiones arquitectónicas más debatidas del desarrollo actual: la adopción de microservicios. La idea central no es que los microservicios sean automáticamente mejores que una arquitectura monolítica, sino que pueden encajar muy bien cuando el sistema necesita evolución separada por dominios, equipos y responsabilidades. El problema es que muchos equipos los adoptan por moda sin analizar si el problema real los justifica.

También se introduce la relación entre arquitectura y dominio. Un buen diseño de software debe reflejar el dominio del negocio. Cuando los servicios corresponden a límites de negocio claros, la solución se vuelve más entendible, escalable y mantenible. La clave está en separar responsabilidades con sentido, no en dividir por tecnología por el solo hecho de hacerlo.

**Fuente 2: Datos y almacenamiento**
El video presenta la importancia decisiva de la estrategia de datos dentro de la arquitectura. Una aplicación no es solo lógica de negocio; también es un sistema de lectura, escritura, consulta y persistencia. La forma en que se almacenan los datos afecta directamente rendimiento, consistencia, recuperación, costos, y capacidad de evolución. Elegir una base de datos o un patrón de almacenamiento equivale a definir parte del comportamiento del sistema.

Se enfatiza que no existe una base de datos “mejor” en abstracto, sino una opción más adecuada para cada problema. La arquitectura debe evaluar volumen, tipos de consulta, consistencia requerida, latencia, integridad y costo operativo. A partir de ahí, se pueden elegir modelos relacionales, NoSQL, colas, caché o arquitecturas híbridas.

## Ideas que debes conservar
- Los microservicios son una opción, no una obligación.
- La arquitectura debe reflejar el dominio del negocio y no solo la tecnología.
- La división por componentes debe hacerse con criterios claros de responsabilidad.
- La complejidad operativa aumenta al adoptar múltiples servicios.
- La estrategia de datos influye directamente en la arquitectura.
- No todas las bases de datos resuelven el mismo tipo de problema.
- El almacenamiento debe obedecer al comportamiento real del negocio.
- Rendimiento, consistencia y costos son variables que se deben balancear.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: premortem y pruebas de arquitectura. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **premortem y pruebas de arquitectura**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: Los microservicios son una opción, no una obligación.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos premortem y pruebas de arquitectura al flujo.
    2. **Actor prioritario de premortem y pruebas de arquitectura:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en premortem y pruebas de arquitectura:** escribe la condición que debe permanecer verdadera y relaciónala con los microservicios son una opción, no una obligación..
    4. **Punto de decisión para premortem y pruebas de arquitectura:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de premortem y pruebas de arquitectura:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **premortem y pruebas de arquitectura**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa premortem y pruebas de arquitectura y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: los microservicios son una opción, no una obligación.
3. Identifica el actor que recibe el impacto de premortem y pruebas de arquitectura y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para premortem y pruebas de arquitectura; compara sus costos y riesgos.
5. Elige una opción para premortem y pruebas de arquitectura, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: premortem y pruebas de arquitectura debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Mi sistema necesita separación por dominio o la complejidad no justifica eso?

**Respuesta concreta:** Para premortem y pruebas de arquitectura, el cliente necesita recibir un estado de entrega confiable. La respuesta concreta es proteger la regla 'no mostrar una entrega como completada sin evidencia válida' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Estoy dividiendo el sistema por negocio o por comodidad técnica?

**Respuesta concreta:** Para premortem y pruebas de arquitectura, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué tipo de consultas y volumen real tiene mi sistema?

**Respuesta concreta:** Para premortem y pruebas de arquitectura, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Estoy priorizando velocidad de desarrollo sobre sostenibilidad de datos?

**Respuesta concreta:** La prioridad de premortem y pruebas de arquitectura es proteger a el equipo de soporte, porque reconstruir qué ocurrió durante un incidente. Aplicaría un control que impida violar la regla 'tener eventos, errores y estados observables', limitaría el acceso a los datos necesarios y registraría los intentos rechazados. El costo es mayor complejidad de autorización y auditoría; lo comprobaría con pruebas de acceso permitido y denegado.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa premortem y pruebas de arquitectura y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de premortem y pruebas de arquitectura:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para premortem y pruebas de arquitectura:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de premortem y pruebas de arquitectura:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: Los microservicios son una opción, no una obligación. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a premortem y pruebas de arquitectura: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de premortem y pruebas de arquitectura, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Premortem y pruebas de arquitectura:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
Microservicios no son la respuesta universal. Su valor aparece cuando ayudan a organizar un sistema complejo en dominios manejables y equipos con responsabilidades claras. El verdadero criterio es la capacidad de crear un sistema entendible y evolutivo, no solo distribuirlo en muchos servicios.

La información es el corazón del sistema. Un diseño arquitectónico sólido toma decisiones inteligentes sobre cómo almacenar, consultar, proteger y evolucionar los datos, porque eso impacta el resto de la solución.

## Preguntas para preparar la grabación
- ¿Mi sistema necesita separación por dominio o la complejidad no justifica eso?
- ¿Estoy dividiendo el sistema por negocio o por comodidad técnica?
- ¿Qué tipo de consultas y volumen real tiene mi sistema?
- ¿Estoy priorizando velocidad de desarrollo sobre sostenibilidad de datos?

## Evidencia para el repositorio
Guarda la explicación de premortem y pruebas de arquitectura, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
