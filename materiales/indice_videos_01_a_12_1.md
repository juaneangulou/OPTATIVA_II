# Índice de videos grabados: 01 a 12.1

| Orden | Video | Título | Enlace |
|---:|---|---|---|
| 1 | Video 01 | Qué es la arquitectura y por qué importa | [Abrir video 01](materiales/materiales_por_video/serie_30_videos/video-01.md) |
| 2 | Video 02 | Rol del arquitecto y comunicación | [Abrir video 02](materiales/materiales_por_video/serie_30_videos/video-02.md) |
| 3 | Video 03 | Documentación y decisiones explícitas | [Abrir video 03](materiales/materiales_por_video/serie_30_videos/video-03.md) |
| 4 | Video 04 | Responsabilidad, escalabilidad, seguridad y ética | [Abrir video 04](materiales/materiales_por_video/serie_30_videos/video-04.md) |
| 5 | Video 04.1 | Actividad 1: Diagnóstico y contexto arquitectónico | [Abrir actividad 1](materiales/materiales_por_video/serie_30_videos/video-04-1.md) |
| 6 | Video 05 | Principios de diseño, acoplamiento y cohesión | [Abrir video 05](materiales/materiales_por_video/serie_30_videos/video-05.md) |
| 7 | Video 06 | Dominios y límites de contexto | [Abrir video 06](materiales/materiales_por_video/serie_30_videos/video-06.md) |
| 8 | Video 07 | Monolitos, sistemas distribuidos y microservicios | [Abrir video 07](materiales/materiales_por_video/serie_30_videos/video-07.md) |
| 9 | Video 08 | APIs, contratos e infraestructura | [Abrir video 08](materiales/materiales_por_video/serie_30_videos/video-08.md) |
| 10 | Video 08.1 | Actividad 2: Requisitos y decisión estructural | [Abrir actividad 2](materiales/materiales_por_video/serie_30_videos/video-08-1.md) |
| 11 | Video 09 | Observabilidad, seguridad y privacidad | [Abrir video 09](materiales/materiales_por_video/serie_30_videos/video-09.md) |
| 12 | Video 10 | Testing, DevOps y entrega continua | [Abrir video 10](materiales/materiales_por_video/serie_30_videos/video-10.md) |
| 13 | Video 11 | Evolución, riesgos y costos | [Abrir video 11](materiales/materiales_por_video/serie_30_videos/video-11.md) |
| 14 | Video 12 | Estrategia tecnológica y roadmap | [Abrir video 12](materiales/materiales_por_video/serie_30_videos/video-12.md) |
| 15 | Video 12.1 | Actividad 3: Diseño y dominio | [Abrir actividad 3](materiales/materiales_por_video/serie_30_videos/video-12-1.md) |

## Actividades cubiertas

| Video | Título | Descripción |
|---|---|---|
| 01 | Qué es la arquitectura y por qué importa | Explica que la arquitectura no consiste solo en elegir tecnologías o dibujar diagramas, sino en tomar decisiones que afectan la seguridad, la evolución, la calidad y el impacto real de un sistema. |
| 02 | Rol del arquitecto y comunicación | Presenta al arquitecto como la persona que conecta negocio, tecnología y equipos, transforma complejidad en decisiones comprensibles y comunica trade-offs a los distintos actores del proyecto. |
| 03 | Documentación y decisiones explícitas | Enseña a registrar contexto, alternativas, riesgos, restricciones y razones mediante decisiones arquitectónicas que permitan conservar el conocimiento y mantener claridad cuando el equipo o el sistema cambien. |
| 04 | Responsabilidad, escalabilidad, seguridad y ética | Analiza el uso responsable de datos de ubicación en una plataforma logística, comparando rapidez operativa con privacidad, seguridad, auditoría y protección de las personas involucradas. |
| 04.1 | Actividad 1: Diagnóstico y contexto arquitectónico | Resuelve el diagnóstico inicial de la plataforma logística mediante la definición del problema, identificación de actores, alcance, restricciones, riesgos, diagrama de contexto y decisiones iniciales documentadas. |
| 05 | Principios de diseño, acoplamiento y cohesión | Explica cómo identificar una clase con responsabilidades mezcladas y refactorizarla en componentes más cohesionados y menos acoplados mediante interfaces, casos de uso y adaptadores en C#. |
| 06 | Dominios y límites de contexto | Diferencia los contextos de Pedidos, Inventario, Ruteo y Entregas, mostrando que conceptos como “disponible” pueden tener significados distintos y deben protegerse mediante modelos y reglas separadas. |
| 07 | Monolitos, sistemas distribuidos y microservicios | Compara un monolito modular con la extracción gradual de un servicio de Ruteo, utilizando métricas de carga, latencia, autonomía y costo operativo para decidir cuándo una arquitectura distribuida está justificada. |
| 08 | APIs, contratos e infraestructura | Construye el borde de una aplicación con un contrato HTTP versionado, DTOs, controlador ASP.NET Core, caso de uso, adaptadores y configuración reproducible para evitar romper clientes existentes. |
| 08.1 | Actividad 2: Requisitos y decisión estructural | Convierte las necesidades de la aplicación móvil en requisitos priorizados, escenarios de calidad, alternativas estructurales, ADR, contrato API, trade-offs y criterios de revisión verificables. |
| 09 | Observabilidad, seguridad y privacidad | Investiga un pedido bloqueado usando logs estructurados, métricas, trazas y auditoría, explicando cómo utilizar `ILogger` y `traceId` sin registrar tokens, direcciones o información personal innecesaria. |
| 10 | Testing, DevOps y entrega continua | Protege una regla de negocio mediante pruebas xUnit, falsos controlados y un pipeline de GitHub Actions que restaura, compila y prueba el sistema antes de integrar cambios. |
| 11 | Evolución, riesgos y costos | Evalúa si conviene reescribir el motor de rutas o introducir una política intercambiable, usando riesgos, reversibilidad, experimentos, métricas y condiciones explícitas para continuar o retirar una decisión. |
| 12 | Estrategia tecnológica y roadmap | Construye un roadmap de tres meses que conecta objetivos de negocio con iniciativas, dependencias, capacidad del equipo, métricas de salida y decisiones que deben quedar fuera del alcance. |
| 12.1 | Actividad 3: Diseño y dominio | Diseña el núcleo del dominio con entidades, objetos de valor, invariantes, casos de uso, puertos, adaptadores y dirección de dependencias, implementando un ejemplo C# de asignación de repartidor. |
