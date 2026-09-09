# Video 18: Documentación viva y revisión con IA

## Fuentes oficiales
- [Platzi: Escalabilidad y rendimiento](https://platzi.com/cursos/software-avanzado/quarto-como-sitio-de-documentacion-viva/)
- [Platzi: Resiliencia y tolerancia a fallos](https://platzi.com/cursos/software-avanzado/agentes-de-ia-que-revisan-tu-codigo-en-g/)

## 🔗 Navegación
[⬅️ Video anterior](video-17.md) | [➡️ Video siguiente](video-19.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

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
La escalabilidad y el rendimiento son indicadores de madurez arquitectónica. Un sistema que puede crecer sin perder calidad no solo sirve mejor, sino que también reduce riesgos operativos y costos de corrección a largo plazo.

Un sistema no se vuelve bueno solo porque “anda en el momento”, sino porque puede resistir fallos y seguir entregando valor. La resiliencia es una de las habilidades más importantes de una arquitectura moderna.

## Preguntas para preparar la grabación
- ¿Mi sistema está preparado para crecer en usuarios, tráfico o complejidad?
- ¿Qué cuellos de botella reales existen hoy?
- ¿Qué pasa si uno de mis servicios falla hoy?
- ¿Mi sistema degrada de forma controlada o colapsa por completo?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
