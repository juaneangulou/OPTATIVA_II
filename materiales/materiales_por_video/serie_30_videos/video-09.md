# Video 09: Observabilidad, seguridad y privacidad

## Fuentes oficiales
- [Observabilidad y monitoreo de sistemas](https://platzi.com/cursos/fundamentos-arquitectura-software/como-funcionan-los-eventos-en-sistemas-d/)
- [Seguridad, datos sensibles y privacidad](https://platzi.com/cursos/fundamentos-arquitectura-software/costos-ocultos-de-los-microservicios/)

## 🔗 Navegación
[⬅️ Video anterior](video-08.md) | [➡️ Video siguiente](video-10.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: observabilidad, seguridad y privacidad. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Observabilidad y monitoreo de sistemas**
La observabilidad es una capacidad esencial en sistemas modernos. Permite entender qué está sucediendo en producción, detectar fallos, identificar cuellos de botella y responder rápidamente ante anomalías. Si un sistema no es observable, el equipo trabaja a ciegas y la resolución de incidentes se vuelve más costosa.

La observabilidad no es solo activar logs; incluye métricas, trazabilidad, alertas y mecanismos para evaluar el comportamiento real del sistema. Cuando se diseña bien, ayuda a prevenir incidentes, entender la carga y tomar decisiones basadas en evidencia.

**Fuente 2: Seguridad, datos sensibles y privacidad**
Este video refuerza la idea de que la seguridad debe integrarse desde el inicio del diseño. No se trata solo de proteger la aplicación frente a intrusos, sino también de gestionar adecuadamente datos sensibles, permisos de acceso y riesgos derivados del tratamiento de información. Cualquier sistema que maneje datos valiosos debe diseñarse con principios de privacidad, control y minimización.

La arquitectura debe prestar atención a qué información guarda, cómo la protege y quién puede acceder a ella. Cuando se ignora esto, se generan riesgos reales tanto para la empresa como para las personas que usan el sistema.

## Ideas que debes conservar
- La observabilidad permite entender el comportamiento real del sistema.
- Los logs, métricas y trazas son herramientas esenciales de diagnósticos.
- Un sistema difícil de monitorear es más riesgoso en producción.
- La observabilidad es una decisión arquitectónica, no un detalle final.
- La seguridad debe estar integrada al diseño, no añadida al final.
- Los datos sensibles requieren más criterios de control y protección.
- La privacidad es parte del valor del sistema.
- Un sistema debe minimizar exposición de información innecesaria.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: observabilidad, seguridad y privacidad. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **observabilidad, seguridad y privacidad**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: La observabilidad permite entender el comportamiento real del sistema.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos observabilidad, seguridad y privacidad al flujo.
    2. **Actor prioritario de observabilidad, seguridad y privacidad:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en observabilidad, seguridad y privacidad:** escribe la condición que debe permanecer verdadera y relaciónala con la observabilidad permite entender el comportamiento real del sistema..
    4. **Punto de decisión para observabilidad, seguridad y privacidad:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de observabilidad, seguridad y privacidad:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **observabilidad, seguridad y privacidad**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa observabilidad, seguridad y privacidad y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: la observabilidad permite entender el comportamiento real del sistema.
3. Identifica el actor que recibe el impacto de observabilidad, seguridad y privacidad y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para observabilidad, seguridad y privacidad; compara sus costos y riesgos.
5. Elige una opción para observabilidad, seguridad y privacidad, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: observabilidad, seguridad y privacidad debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Qué tan claro es el estado actual de mi sistema en producción?

**Respuesta concreta:** Para observabilidad, seguridad y privacidad, el cliente necesita recibir un estado de entrega confiable. La respuesta concreta es proteger la regla 'no mostrar una entrega como completada sin evidencia válida' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Estoy monitoreando lo que realmente importa?

**Respuesta concreta:** Para observabilidad, seguridad y privacidad, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué datos sensibles maneja mi sistema?

**Respuesta concreta:** La prioridad de observabilidad, seguridad y privacidad es proteger a el repartidor, porque recibir una instrucción vigente y consistente. Aplicaría un control que impida violar la regla 'evitar dos asignaciones activas para la misma entrega', limitaría el acceso a los datos necesarios y registraría los intentos rechazados. El costo es mayor complejidad de autorización y auditoría; lo comprobaría con pruebas de acceso permitido y denegado.

### ❓ ¿Estoy reduciendo la exposición innecesaria de información?

**Respuesta concreta:** Para observabilidad, seguridad y privacidad, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa observabilidad, seguridad y privacidad y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de observabilidad, seguridad y privacidad:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para observabilidad, seguridad y privacidad:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de observabilidad, seguridad y privacidad:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La observabilidad permite entender el comportamiento real del sistema. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a observabilidad, seguridad y privacidad: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de observabilidad, seguridad y privacidad, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Observabilidad, seguridad y privacidad:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La observabilidad es una parte central de la arquitectura porque permite entender, prevenir y corregir problemas antes de que se vuelvan críticos.

La seguridad y la privacidad no son requisitos secundarios: son elementos fundamentales de una arquitectura responsable y confiable.

## Preguntas para preparar la grabación
- ¿Qué tan claro es el estado actual de mi sistema en producción?
- ¿Estoy monitoreando lo que realmente importa?
- ¿Qué datos sensibles maneja mi sistema?
- ¿Estoy reduciendo la exposición innecesaria de información?

## Evidencia para el repositorio
Guarda la explicación de observabilidad, seguridad y privacidad, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
