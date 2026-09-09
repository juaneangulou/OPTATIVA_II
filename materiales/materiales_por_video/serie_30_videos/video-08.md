# Video 08: APIs, contratos e infraestructura

## Fuentes oficiales
- [APIs y contratos de integración](https://platzi.com/cursos/fundamentos-arquitectura-software/que-son-las-arquitecturas-monoliticas-y/)
- [Infraestructura, despliegue y entorno de ejecución](https://platzi.com/cursos/fundamentos-arquitectura-software/arquitecturas-orientadas-a-servicios-con/)

## 🔗 Navegación
[⬅️ Video anterior](video-07.md) | [➡️ Video siguiente](video-09.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: apis, contratos e infraestructura. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: APIs y contratos de integración**
Este video centra la atención en la forma en que los sistemas se integran entre sí. Las APIs son contratos entre partes: representan cómo se comunica un servicio con otro y cómo se comparte información. Cuando esos contratos son claros, la integración es más productiva y menos frágil. Cuando no lo son, se vuelven fuentes de errores, incompatibilidades y cambios difíciles de gestionar.

El diseño de APIs incluye no solo endpoints o rutas, sino también formato, validaciones, errores, versionado y políticas de evolución. Una buena API debe ser clara, estable y fácil de consumirse por el equipo o por sistemas externos.

**Fuente 2: Infraestructura, despliegue y entorno de ejecución**
Este video muestra que la arquitectura incluye también la infraestructura que ejecuta el sistema. Un diseño puede ser excelente en código, pero si el entorno de ejecución es caótico, manual o poco reproducible, la aplicación no será sostenible. La arquitectura debe considerar tanto la capa lógica como la capa operativa que la pone en marcha.

La infraestructura debe ser fácil de reproducir, detectar fallos y trasladar entre entornos. Los despliegues automatizados y los procesos de entorno ayudan a reducir errores humanos y mejorar la confianza del sistema en producción.

## Ideas que debes conservar
- Las APIs son acuerdos de comunicación entre sistemas.
- Los contratos deben ser claros y bien documentados.
- El versionado reduce riesgos de romper dependencias.
- Una mala API genera fragilidad en la integración.
- La infraestructura es parte del diseño arquitectónico.
- El entorno debe ser reproducible y consistente.
- Un despliegue manual aumenta riesgos y errores.
- La infraestructura debe soportar diferentes contextos: desarrollo, prueba y producción.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: apis, contratos e infraestructura. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **apis, contratos e infraestructura**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: Las APIs son acuerdos de comunicación entre sistemas.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos apis, contratos e infraestructura al flujo.
    2. **Actor prioritario de apis, contratos e infraestructura:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en apis, contratos e infraestructura:** escribe la condición que debe permanecer verdadera y relaciónala con las apis son acuerdos de comunicación entre sistemas..
    4. **Punto de decisión para apis, contratos e infraestructura:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de apis, contratos e infraestructura:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **apis, contratos e infraestructura**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa apis, contratos e infraestructura y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: las apis son acuerdos de comunicación entre sistemas.
3. Identifica el actor que recibe el impacto de apis, contratos e infraestructura y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para apis, contratos e infraestructura; compara sus costos y riesgos.
5. Elige una opción para apis, contratos e infraestructura, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: apis, contratos e infraestructura debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Mis interfaces están bien definidas y documentadas?

**Respuesta concreta:** Para apis, contratos e infraestructura, el cliente necesita recibir un estado de entrega confiable. La respuesta concreta es proteger la regla 'no mostrar una entrega como completada sin evidencia válida' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué pasa si un cliente usa una versión anterior?

**Respuesta concreta:** Para apis, contratos e infraestructura, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Mi entorno es reproducible y consistente?

**Respuesta concreta:** Para apis, contratos e infraestructura, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué tan fácil es desplegar una versión nueva sin riesgos innecesarios?

**Respuesta concreta:** Para apis, contratos e infraestructura, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa apis, contratos e infraestructura y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de apis, contratos e infraestructura:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para apis, contratos e infraestructura:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de apis, contratos e infraestructura:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: Las APIs son acuerdos de comunicación entre sistemas. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a apis, contratos e infraestructura: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de apis, contratos e infraestructura, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para APIs, contratos e infraestructura:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
El diseño de APIs es una parte central de la arquitectura. Un buen contrato de integración mejora la evolución del sistema y reduce errores de colaboración entre equipos.

La arquitectura no termina en el código: incluye cómo se ejecuta, se despliega y se mantiene. Un sistema bien diseñado también necesita un entorno bien pensado.

## Preguntas para preparar la grabación
- ¿Mis interfaces están bien definidas y documentadas?
- ¿Qué pasa si un cliente usa una versión anterior?
- ¿Mi entorno es reproducible y consistente?
- ¿Qué tan fácil es desplegar una versión nueva sin riesgos innecesarios?

## Evidencia para el repositorio
Guarda la explicación de apis, contratos e infraestructura, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
