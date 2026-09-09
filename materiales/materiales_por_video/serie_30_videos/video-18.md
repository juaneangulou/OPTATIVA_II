# Video 18: Documentación viva y revisión con IA

## Fuentes oficiales
- [Escalabilidad y rendimiento](https://platzi.com/cursos/software-avanzado/quarto-como-sitio-de-documentacion-viva/)
- [Resiliencia y tolerancia a fallos](https://platzi.com/cursos/software-avanzado/agentes-de-ia-que-revisan-tu-codigo-en-g/)

## 🔗 Navegación
[⬅️ Video anterior](video-17.md) | [➡️ Video siguiente](video-19.md)

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: documentación viva y revisión con ia. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
**Fuente 1: Escalabilidad y rendimiento**
El video aborda la diferencia entre un sistema que funciona con pocos usuarios y un sistema que mantiene calidad cuando la carga aumenta. La escalabilidad no es un concepto abstracto: se refiere a la capacidad del sistema para crecer sin perder rendimiento, estabilidad o calidad de servicio. También se menciona que no siempre la solución correcta es “hacerlo más grande”, sino diseñarlo para adaptarse a la demanda con una estrategia clara.

El rendimiento no depende solo de servidores o hardware; también influye la estructura del sistema, la forma en que se comunican componentes, el uso de caché, la distribución de responsabilidades y la calidad del diseño. Aquí aparece la idea de que la escalabilidad debe planearse desde el inicio, pero no siempre con una arquitectura más compleja que el problema justifique.

**Fuente 2: Resiliencia y tolerancia a fallos**
Este video introduce la idea de que ningún sistema es completamente estable ni inmune a fallos. Internet, servicios externos, bases de datos, dependencias y cambios de carga pueden afectar el funcionamiento normal. Por eso, una arquitectura robusta no se define por la ausencia de errores, sino por la capacidad de responder a ellos sin colapsar el servicio completo.

La resiliencia consiste en diseñar sistemas que puedan degradar con elegancia, recuperar automáticamente y continuar ofreciendo valor incluso cuando una parte falle. El video enfatiza que la tolerancia a fallos no es una característica extra; es un criterio de diseño funcional en sistemas reales. Esto incluye reintentos, timeouts, circuit breakers, replicas, backups y una estrategia clara de recuperación.

## Ideas que debes conservar
- Escalabilidad significa crecer sin romper el sistema.
- El rendimiento es un problema de diseño, no solo de infraestructura.
- Un sistema puede ser lento por mala arquitectura, no solo por falta de recursos.
- Aumentar capacidad no siempre es la mejor solución; a veces hay que mejorar diseño.
- Los fallos son inevitables en sistemas distribuidos y complejos.
- La resiliencia es la capacidad de recuperarse sin perder el servicio completo.
- La degradación controlada es mejor que un colapso total.
- La arquitectura debe anticipar errores en dependencias y en infraestructura.

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: documentación viva y revisión con ia. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
Para estudiar **documentación viva y revisión con ia**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: Escalabilidad significa crecer sin romper el sistema.

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos documentación viva y revisión con ia al flujo.
    2. **Actor prioritario de documentación viva y revisión con ia:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en documentación viva y revisión con ia:** escribe la condición que debe permanecer verdadera y relaciónala con escalabilidad significa crecer sin romper el sistema..
    4. **Punto de decisión para documentación viva y revisión con ia:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de documentación viva y revisión con ia:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **documentación viva y revisión con ia**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Explica con tus palabras qué significa documentación viva y revisión con ia y qué fuente respalda esa interpretación.
2. Describe una situación de la plataforma logística donde aparezca: escalabilidad significa crecer sin romper el sistema.
3. Identifica el actor que recibe el impacto de documentación viva y revisión con ia y la regla que no puede romperse.
4. Propón una solución mínima y otra más robusta para documentación viva y revisión con ia; compara sus costos y riesgos.
5. Elige una opción para documentación viva y revisión con ia, declara qué sacrificas y define la condición que obligaría a revisarla.
6. Produce la evidencia propia de este tema: documentación viva y revisión con ia debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.

## Respuestas a las preguntas
### ❓ ¿Mi sistema está preparado para crecer en usuarios, tráfico o complejidad?

**Respuesta concreta:** Si el sistema crece en el tema de documentación viva y revisión con ia, el cliente seguirá necesitando recibir un estado de entrega confiable. No elegiría una solución distribuida automáticamente; primero mediría carga, latencia y errores. Mantendría la regla 'no mostrar una entrega como completada sin evidencia válida' en un módulo claro y escalaría solo el punto que demuestre saturación. La decisión se verifica con una prueba de carga y una métrica acordada.

### ❓ ¿Qué cuellos de botella reales existen hoy?

**Respuesta concreta:** Para documentación viva y revisión con ia, el operador logístico necesita reasignar una ruta sin perder el historial del pedido. La respuesta concreta es proteger la regla 'conservar trazabilidad de cada cambio' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Qué pasa si uno de mis servicios falla hoy?

**Respuesta concreta:** Para documentación viva y revisión con ia, el repartidor necesita recibir una instrucción vigente y consistente. La respuesta concreta es proteger la regla 'evitar dos asignaciones activas para la misma entrega' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

### ❓ ¿Mi sistema degrada de forma controlada o colapsa por completo?

**Respuesta concreta:** Para documentación viva y revisión con ia, el equipo de soporte necesita reconstruir qué ocurrió durante un incidente. La respuesta concreta es proteger la regla 'tener eventos, errores y estados observables' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa documentación viva y revisión con ia y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de documentación viva y revisión con ia:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para documentación viva y revisión con ia:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de documentación viva y revisión con ia:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: Escalabilidad significa crecer sin romper el sistema. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a documentación viva y revisión con ia: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de documentación viva y revisión con ia, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para Documentación viva y revisión con IA:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
La escalabilidad y el rendimiento son indicadores de madurez arquitectónica. Un sistema que puede crecer sin perder calidad no solo sirve mejor, sino que también reduce riesgos operativos y costos de corrección a largo plazo.

Un sistema no se vuelve bueno solo porque “anda en el momento”, sino porque puede resistir fallos y seguir entregando valor. La resiliencia es una de las habilidades más importantes de una arquitectura moderna.

## Preguntas para preparar la grabación
- ¿Mi sistema está preparado para crecer en usuarios, tráfico o complejidad?
- ¿Qué cuellos de botella reales existen hoy?
- ¿Qué pasa si uno de mis servicios falla hoy?
- ¿Mi sistema degrada de forma controlada o colapsa por completo?

## Evidencia para el repositorio
Guarda la explicación de documentación viva y revisión con ia, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística.
