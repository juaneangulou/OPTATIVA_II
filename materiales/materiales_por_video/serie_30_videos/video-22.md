# Video 22: Bases de datos y API Gateway

## Fuentes oficiales
- [Arquitectura moderna y liderazgo](https://platzi.com/cursos/software-avanzado/migraciones-de-base-de-datos-con-flyway/)
- [Documentación y decisiones explícitas](https://platzi.com/cursos/software-avanzado/api-gateway-como-capa-de-abstraccion-en/)

## 🔗 Navegación
[⬅️ Video anterior](video-21.md) | [➡️ Video siguiente](video-23.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Arquitectura moderna y liderazgo**
El video final reúne los principales temas del curso: la arquitectura de software ya no es solo una disciplina técnica de diagramas y patrones, sino una práctica estratégica que conecta negocio, tecnología, personas y evolución. El arquitecto moderno debe pensar en sistemas sostenibles, seguros, escalables, observables y alineados con el contexto real donde operan.

Además, se resalta que la tecnología cambia rápido, pero la esencia del liderazgo arquitectónico no: la clave es tomar decisiones con criterio, comunicar claramente, resolver conflictos, y guiar a equipos a construir soluciones con sentido. La arquitectura moderna requiere una mezcla de técnica, visión de negocio, capacidad de análisis, juicio ético y habilidades de liderazgo. Es más que construir software: es diseñar el camino para que ese software pueda sobrevivir y aportar valor con el tiempo.

**Fuente 2: Documentación y decisiones explícitas**
La documentación de arquitectura no es un lujo ni una actividad burocrática superficial; es una herramienta clave para que el sistema pueda entenderse, evolucionar y sostenerse en el tiempo. Cuando las decisiones se documentan de forma clara, el equipo puede reducir ambigüedad, evitar errores de interpretación y mantener continuidad incluso con cambios de personal. El video hace hincapié en que la arquitectura debe dejarse escrita, no solo en la cabeza de unos pocos.

Esto incluye explicar trade-offs, restricciones, decisiones tomadas y alternativas descartadas. Cuando un proyecto se basa en decisiones implícitas, cada integrante empieza a hacer su propia “lectura” del sistema. La documentación ayuda a que el diseño sea compartido, revisado y mejorado con base en evidencia.

## Ideas que debes conservar
- La arquitectura moderna combina tecnología, negocio y estrategia.
- El arquitecto actúa como guía, decisor y comunicador.
- La calidad del sistema depende de decisiones y procesos, no solo de ideas técnicas.
- La evolución continua exige adaptación constante y aprendizaje.
- La documentación reduce ambigüedad y ayuda a la continuidad del proyecto.
- Las decisiones arquitectónicas deben ser explícitas, no solo inferidas.
- Documentar no significa escribir mucho por escrito; significa registrar lo relevante.
- Se deben reflejar restricciones, decisiones, alternativas y razones.

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
La plataforma logística recibe un pedido, reserva inventario, calcula una ruta, asigna un repartidor y comunica el estado. En esta clase no vamos a mencionar esos pasos como una lista: vamos a observar dónde aparece **bases de datos y api gateway**.

1. **Situación:** el sistema debe resolver un pedido sin perder la calidad relacionada con este tema: La arquitectura moderna combina tecnología, negocio y estrategia.
2. **Actores afectados:** cliente, operador logístico, repartidor, equipo de soporte y equipo técnico. Cada uno necesita información y garantías diferentes.
3. **Punto de decisión:** el equipo debe decidir qué responsabilidad queda en el módulo de pedidos, qué cruza hacia ruteo o inventario y qué se delega a una dependencia externa.
4. **Riesgo:** si la decisión es débil, puede haber entregas tardías, datos expuestos, cambios costosos, mensajes perdidos o una operación imposible de diagnosticar.
5. **Evidencia:** la decisión se demuestra con el artefacto adecuado: diagrama, ADR, contrato, código, prueba, métrica, registro de despliegue o experimento controlado.

Para resolver el caso, empieza por el flujo “crear pedido”. Señala el componente que recibe la solicitud, la regla que debe protegerse, la dependencia que puede fallar y el resultado que espera cada actor. Después compara dos formas de construirlo: una solución sencilla para el MVP y otra con mayor separación. La elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.


## Actividad de construcción
1. Resume en tus palabras la idea central de cada fuente.
2. Combina esas ideas en un problema arquitectónico único.
3. Propón dos alternativas de solución.
4. Compara costo inicial, calidad, riesgo, operación y facilidad de cambio.
5. Elige una alternativa para el MVP y declara qué condición obligaría a revisarla.
6. Produce una evidencia: ADR, diagrama, contrato, código C#, prueba, métrica o plan de evolución.

## Respuestas a las preguntas
### ❓ ¿Qué tipo de arquitecto quiero ser: técnico, estratégico o de liderazgo?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la arquitectura moderna combina tecnología, negocio y estrategia. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy construyendo soluciones solo para hoy o para el crecimiento futuro?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con el arquitecto actúa como guía, decisor y comunicador. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Qué decisiones importantes de mi proyecto están aún en la cabeza de una sola persona?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la calidad del sistema depende de decisiones y procesos, no solo de ideas técnicas. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

### ❓ ¿Estoy documentando solo la solución final o también el porqué?

**Respuesta orientadora:** En la plataforma logística, esta pregunta se responde relacionándola con la evolución continua exige adaptación constante y aprendizaje. Primero identifica el actor afectado y la regla que quieres proteger; después elige una evidencia que permita comprobarlo. Una respuesta completa debe decir qué cambiarías, qué costo aceptarías y cómo sabrías si la decisión funcionó.

## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa bases de datos y api gateway y qué idea principal de las fuentes lo justifica.
2. **Delimita el caso:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
3. **Formula dos opciones:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
4. **Compara las opciones:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: La arquitectura moderna combina tecnología, negocio y estrategia. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda al tema: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión definida, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.


## Conclusiones de las fuentes
El curso cierra con una visión clara: la mejor arquitectura no es la más compleja ni la más innovadora, sino la que resuelve el problema real con criterio, sostenibilidad y capacidad de evolución. El arquitecto de software es quien convierte la complejidad en claridad y guía a la organización para crear soluciones con valor duradero.

La documentación arquitectónica es una forma de preservar el conocimiento y de evitar que el sistema se vuelva incomprensible con el tiempo. Un buen diseño debe ser enseñable, comprensible y defendible.

## Preguntas para preparar la grabación
- ¿Qué tipo de arquitecto quiero ser: técnico, estratégico o de liderazgo?
- ¿Estoy construyendo soluciones solo para hoy o para el crecimiento futuro?
- ¿Qué decisiones importantes de mi proyecto están aún en la cabeza de una sola persona?
- ¿Estoy documentando solo la solución final o también el porqué?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
