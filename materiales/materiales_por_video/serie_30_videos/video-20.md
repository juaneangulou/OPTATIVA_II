# Video 20: Premortem y pruebas de arquitectura

## Fuentes oficiales
- [Platzi: Microservicios y dominios](https://platzi.com/cursos/software-avanzado/tecnicas-pre-mortem-y-cinco-why-para-pre/)
- [Platzi: Datos y almacenamiento](https://platzi.com/cursos/software-avanzado/como-el-premortem-guia-tus-tests-de-arqu/)

## 🔗 Navegación
[⬅️ Video anterior](video-19.md) | [➡️ Video siguiente](video-21.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

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
Microservicios no son la respuesta universal. Su valor aparece cuando ayudan a organizar un sistema complejo en dominios manejables y equipos con responsabilidades claras. El verdadero criterio es la capacidad de crear un sistema entendible y evolutivo, no solo distribuirlo en muchos servicios.

La información es el corazón del sistema. Un diseño arquitectónico sólido toma decisiones inteligentes sobre cómo almacenar, consultar, proteger y evolucionar los datos, porque eso impacta el resto de la solución.

## Preguntas para preparar la grabación
- ¿Mi sistema necesita separación por dominio o la complejidad no justifica eso?
- ¿Estoy dividiendo el sistema por negocio o por comodidad técnica?
- ¿Qué tipo de consultas y volumen real tiene mi sistema?
- ¿Estoy priorizando velocidad de desarrollo sobre sostenibilidad de datos?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
