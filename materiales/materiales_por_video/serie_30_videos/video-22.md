# Video 22: Bases de datos y API Gateway

## Fuentes oficiales
- [Platzi: Arquitectura moderna y liderazgo](https://platzi.com/cursos/software-avanzado/migraciones-de-base-de-datos-con-flyway/)
- [Platzi: Documentación y decisiones explícitas](https://platzi.com/cursos/software-avanzado/api-gateway-como-capa-de-abstraccion-en/)

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
Analiza cómo este tema afecta pedidos, inventario, ruteo, entregas, notificaciones, incidentes y operación. Elige un flujo concreto y explica qué responsabilidad, dependencia o atributo de calidad queda protegido.

## Actividad de construcción
1. Resume en tus palabras la idea central de cada fuente.
2. Combina esas ideas en un problema arquitectónico único.
3. Propón dos alternativas de solución.
4. Compara costo inicial, calidad, riesgo, operación y facilidad de cambio.
5. Elige una alternativa para el MVP y declara qué condición obligaría a revisarla.
6. Produce una evidencia: ADR, diagrama, contrato, código C#, prueba, métrica o plan de evolución.

## Respuesta orientadora
Una respuesta sólida conecta las fuentes con el caso. No basta decir que una tecnología es mejor: debes explicar qué problema resuelve, qué costo introduce, qué alternativa descartas y cómo comprobarás la decisión.

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
