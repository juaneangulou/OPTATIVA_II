# Video 03: Documentación y decisiones explícitas

## Fuentes oficiales
- [Documentar decisiones y mantener claridad](https://platzi.com/cursos/fundamentos-arquitectura-software/malas-practicas-de-arquitectura-y-como-e/)
- [Documentación y decisiones explícitas](https://platzi.com/cursos/software-avanzado/api-gateway-como-capa-de-abstraccion-en/)

## 🔗 Navegación
[⬅️ Video anterior](video-02.md) | [➡️ Video siguiente](video-04.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: documentación y decisiones explícitas. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Documentar decisiones y mantener claridad**
Este video profundiza en la importancia de dejar explícitas las decisiones de arquitectura. Muchas veces el problema no es solo que el sistema funcione, sino que se vuelva difícil de entender por quien lo revisa después. Cuando las decisiones no se documentan, cada persona asume una interpretación distinta y eso termina generando inconsistencias.

La idea es documentar el contexto, la intención, los riesgos, las restricciones y las alternativas descartadas. Esa práctica no solo ayuda al mantenimiento, sino también a que el equipo pueda evaluar si una solución sigue siendo apropiada con el tiempo. La documentación debe ser clara, viva y útil.

**Fuente 2: Documentación y decisiones explícitas**
La documentación de arquitectura no es un lujo ni una actividad burocrática superficial; es una herramienta clave para que el sistema pueda entenderse, evolucionar y sostenerse en el tiempo. Cuando las decisiones se documentan de forma clara, el equipo puede reducir ambigüedad, evitar errores de interpretación y mantener continuidad incluso con cambios de personal. El video hace hincapié en que la arquitectura debe dejarse escrita, no solo en la cabeza de unos pocos.

Esto incluye explicar trade-offs, restricciones, decisiones tomadas y alternativas descartadas. Cuando un proyecto se basa en decisiones implícitas, cada integrante empieza a hacer su propia “lectura” del sistema. La documentación ayuda a que el diseño sea compartido, revisado y mejorado con base en evidencia.

## Ideas que debes conservar
- Las decisiones de arquitectura deben dejarse escritas.
- La documentación ayuda a preservar conocimiento y continuidad.
- Debe aclarar intención, restricciones, riesgos y alternativas.
- La arquitectura viva reduce la ambigüedad y mejora la evolución.
- La documentación reduce ambigüedad y ayuda a la continuidad del proyecto.
- Las decisiones arquitectónicas deben ser explícitas, no solo inferidas.
- Documentar no significa escribir mucho por escrito; significa registrar lo relevante.
- Se deben reflejar restricciones, decisiones, alternativas y razones.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: documentación y decisiones explícitas. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **documentación y decisiones explícitas**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: Las decisiones de arquitectura deben dejarse escritas.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos documentación y decisiones explícitas al flujo.
    2. **Actor prioritario de documentación y decisiones explícitas:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en documentación y decisiones explícitas:** escribe la condición que debe permanecer verdadera y relaciónala con las decisiones de arquitectura deben dejarse escritas..
    4. **Punto de decisión para documentación y decisiones explícitas:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de documentación y decisiones explícitas:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **documentación y decisiones explícitas**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa documentación y decisiones explícitas y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: las decisiones de arquitectura deben dejarse escritas.
3. Identifica el actor que recibe el impacto de documentación y decisiones explícitas y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para documentación y decisiones explícitas; compara sus costos y riesgos.
5. Elige una opción para documentación y decisiones explícitas, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: documentación y decisiones explícitas debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Estoy escribiendo solo el resultado o también el razonamiento detrás de la solución?

**Respuesta concreta:** Para documentación y decisiones explícitas, el cliente necesita recibir un estado de entrega confiable. La respuesta concreta es proteger la regla 'no mostrar una entrega como completada sin evidencia válida' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué decisiones clave del proyecto podrían perderse si se cambia de equipo?

**Respuesta concreta:** Para documentación y decisiones explícitas, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué decisiones importantes de mi proyecto están aún en la cabeza de una sola persona?

**Respuesta concreta:** Para documentación y decisiones explícitas, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Estoy documentando solo la solución final o también el porqué?

**Respuesta concreta:** Para documentación y decisiones explícitas, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa documentación y decisiones explícitas y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de documentación y decisiones explícitas:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para documentación y decisiones explícitas:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de documentación y decisiones explícitas:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: Las decisiones de arquitectura deben dejarse escritas. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a documentación y decisiones explícitas: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de documentación y decisiones explícitas, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Documentación y decisiones explícitas:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La documentación no es burocracia: es una forma de mantener la claridad del sistema y evitar que el conocimiento se pierda. La arquitectura se vuelve más sólida cuando está documentada y compartida.

La documentación arquitectónica es una forma de preservar el conocimiento y de evitar que el sistema se vuelva incomprensible con el tiempo. Un buen diseño debe ser enseñable, comprensible y defendible.

## Preguntas para preparar la grabación
- ¿Estoy escribiendo solo el resultado o también el razonamiento detrás de la solución?
- ¿Qué decisiones clave del proyecto podrían perderse si se cambia de equipo?
- ¿Qué decisiones importantes de mi proyecto están aún en la cabeza de una sola persona?
- ¿Estoy documentando solo la solución final o también el porqué?

## Evidencia para el repositorio
Guarda la explicación de documentación y decisiones explícitas, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
