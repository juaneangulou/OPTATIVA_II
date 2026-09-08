# Playlist de Serie de Videos: Curso Completo de Arquitectura de Software (2026-2)

## Objetivo de la serie

Crear una serie audiovisual que cubra todo el contenido del curso de punta a punta: pensamiento arquitectónico, requisitos, decisiones estructurales, diseño limpio, dominio, implementación, integración, pruebas, operación y defensa técnica.

## Formato sugerido por video

- Duración recomendada: 8 a 15 minutos.
- Estructura: contexto del problema, concepto clave, ejemplo aplicado al caso logístico, cierre con decisión técnica.
- Salida mínima: una evidencia concreta (diagrama, decisión, código o prueba).

## Playlist completa (96 videos)

### Bloque 0. Apertura de la serie

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 1 | Bienvenida: cómo pensar arquitectura en este curso | Presentación de la ruta completa, metodología, caso base logístico, reglas de evaluación y cómo construir el expediente arquitectónico evolutivo. |

### Bloque 1. Pensamiento arquitectónico y contexto

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 2 | La arquitectura como conjunto de decisiones | Qué es una decisión arquitectónica, por qué impacta costo/calidad/tiempo y cómo documentarla sin burocracia excesiva. |
| 3 | El costo invisible de elegir mal | Consecuencias de decisiones tempranas deficientes: deuda, retrabajo, lentitud del equipo y riesgo operativo. |
| 4 | El arquitecto y las conversaciones difíciles | Rol del arquitecto como facilitador entre negocio, desarrollo, operaciones y seguridad. |
| 5 | Problema esencial vs detalle incidental | Cómo separar necesidades reales del negocio de preferencias tecnológicas. |
| 6 | Deuda técnica y acoplamiento: señales tempranas | Indicadores de mala salud arquitectónica y cómo priorizar mitigaciones. |
| 7 | Del problema a las fronteras del sistema | Construcción del diagrama de contexto y delimitación de responsabilidades externas/internas. |

### Bloque 2. Valor, requisitos y riesgo

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 8 | Requisitos que cambian la arquitectura | Identificación y priorización de requisitos funcionales y no funcionales con impacto estructural. |
| 9 | Calidad medible: rendimiento, seguridad y cambio | Definición de escenarios de calidad verificables y su uso para comparar alternativas. |
| 10 | Costo total de operación y costo de cambio | Modelo simple de costos (desarrollo, operación, soporte, evolución) para decidir con frugalidad. |
| 11 | Diseñar para la incertidumbre | Supuestos, decisiones reversibles/irreversibles y mecanismos para aprender rápido sin sobrediseñar. |

### Bloque 3. Formas de estructurar sistemas

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 12 | Elegir estructura sin seguir modas | Criterios para escoger estilo arquitectónico según contexto, equipo, riesgo y horizonte de producto. |
| 13 | Cliente-servidor y capas que sí protegen | Flujo completo de solicitud, responsabilidades por capa y anti-patrones frecuentes. |
| 14 | Monolito modular: empezar pequeño con futuro | Diseño de módulos con límites claros para acelerar MVP y permitir evolución. |
| 15 | Servicios y contratos evolutivos | Diseño de contratos, versionamiento y límites de servicio orientados al cambio. |
| 16 | Eventos, consistencia y fallos parciales | Patrones de integración basada en eventos, idempotencia, reintentos y compensaciones. |
| 17 | Microservicios: cuándo sí y cuándo no | Costos ocultos de operación/distribución y guía para evitar adopción prematura. |

### Bloque 4. Diseño mantenible y arquitectura limpia

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 18 | SOLID para reducir acoplamiento | Aplicación práctica de SOLID sobre código real con problemas de mantenibilidad. |
| 19 | Dirección de dependencias y límites del código | Regla de dependencias, aislamiento del dominio y control de acoplamiento accidental. |
| 20 | Patrones que resuelven problemas reales | Selección de patrones por contexto (no por moda), costo y posibilidad de retiro futuro. |
| 21 | Arquitectura MVP: primer corte útil | Cómo definir una arquitectura inicial proporcional para entregar valor rápido. |
| 22 | Evolucionar sin reescribir el producto | Estrategias evolutivas por fronteras y etapas para reducir riesgo de migración. |
| 23 | De producto personal a sistema de equipo | Cambios arquitectónicos al crecer en usuarios, datos, despliegues y coordinación de equipos. |
| 24 | Revisión de arquitectura entre pares | Técnica de revisión estructurada: preguntas, criterios y hallazgos accionables. |
| 25 | Puente hacia dominio y código | Traducción de decisiones arquitectónicas a backlog técnico y estructura implementable. |

### Bloque 5. Dominio y modelos de referencia limpia

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 26 | Qué protege una arquitectura limpia | Motivación de Clean Architecture: proteger reglas de negocio de detalles externos. |
| 27 | Límites de MVC y tres capas tradicionales | Cuándo colapsan estas aproximaciones y cómo detectar señales de fatiga estructural. |
| 28 | Clean, Hexagonal y Onion: una intención común | Comparación conceptual y guía para elegir variante proporcional al proyecto. |
| 29 | Adoptar arquitectura limpia sin dogma | Criterios para aplicar solo la complejidad necesaria según tamaño y riesgo. |
| 30 | Encapsulamiento e invariantes de dominio | Diseño de entidades y objetos de valor que hagan cumplir reglas críticas del negocio. |

### Bloque 6. Casos de uso y capa de aplicación

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 31 | Transaction Script vs dominio rico | Comparación de enfoques para implementar reglas según complejidad del problema. |
| 32 | Inyección de dependencias desde el borde | Composición de dependencias sin contaminar núcleo de negocio con framework. |
| 33 | Servicios de aplicación sin convertirse en God Object | Diseño de contratos de aplicación claros, cohesivos y orientados a casos de uso. |
| 34 | Casos de uso como intención de negocio | Modelado de entradas/salidas/errores y orquestación de reglas y puertos. |
| 35 | CQRS proporcional: separar cuando agrega valor | Cuándo separar comandos y consultas, riesgos de consistencia y trade-offs de operación. |

### Bloque 7. Infraestructura, persistencia e integración

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 36 | Persistencia detrás de un puerto | Contratos de persistencia, desacople del dominio y flexibilidad para cambiar tecnología. |
| 37 | Repository útil, no abstracción vacía | Diseño de repositorios orientados al caso de uso, evitando interfaces genéricas inútiles. |
| 38 | API REST como adaptador de entrada | Construcción de endpoints conectados a casos de uso con validación y manejo de errores. |
| 39 | Integraciones externas con Adapter | Encapsulamiento de proveedores externos, traducción de errores y resiliencia básica. |

### Bloque 8. Calidad, pruebas y operación

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 40 | Probar reglas, no detalles accidentales | Estrategia de pruebas sobre dominio y casos de uso para proteger decisiones clave. |
| 41 | Mocks, stubs y pruebas de integración | Selección correcta de dobles de prueba y definición de pirámide de pruebas realista. |
| 42 | Contratos, errores y observabilidad mínima | Qué observar en producción y cómo definir señales de salud arquitectónica. |
| 43 | Seguridad como responsabilidad distribuida | Controles de seguridad por capas, amenazas principales y decisiones mínimas obligatorias. |

### Bloque 9. Evolución arquitectónica y defensa

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 44 | Migrar por fronteras, no por carpetas | Plan incremental de modernización con bajo riesgo y alto aprendizaje. |
| 45 | Datos, transacciones y consistencia | Decisiones de consistencia, atomicidad y compensaciones en escenarios distribuidos. |
| 46 | Revisar costo, calidad y mantenibilidad | Uso de un scorecard arquitectónico para evaluar estado actual y próximos pasos. |
| 47 | Contar la historia de una decisión | Cómo estructurar una sustentación técnica persuasiva basada en evidencia. |
| 48 | Defender trade-offs ante escenarios nuevos | Simulación de comité técnico: preguntas difíciles y respuestas argumentadas. |
| 49 | Cierre técnico: arquitectura como práctica continua | Síntesis de aprendizajes, mapa de errores comunes y plan de mejora continua. |

### Bloque 10. Producción académica y entregables

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 50 | Cómo grabar y evaluar tus sustentaciones (Actividades 1-5) | Guía de formato para videos de entrega, estructura recomendada, rúbrica práctica y checklist final de calidad académica. |

### Bloque 11. Laboratorio de modelado del caso logístico

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 51 | Modelar el flujo end-to-end de un pedido | Recorrido completo desde creación de pedido hasta entrega y cierre, identificando eventos y estados críticos. |
| 52 | Delimitar bounded contexts iniciales | Separación inicial de dominios: pedidos, inventario, ruteo, repartidores, incidencias y soporte. |
| 53 | Mapa de eventos del negocio | Identificación de eventos de negocio, productores, consumidores y dependencias temporales. |
| 54 | Priorización de invariantes de dominio | Reglas que nunca deben romperse y su impacto en consistencia, disponibilidad y experiencia de usuario. |
| 55 | Taller de lenguaje ubicuo | Construcción del vocabulario común entre negocio y desarrollo para reducir ambigüedad. |
| 56 | Del modelo conceptual al modelo implementable | Conversión de conceptos de negocio a entidades, objetos de valor y contratos técnicos. |

### Bloque 12. ADR y gobierno de decisiones

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 57 | Cómo escribir un ADR útil | Estructura mínima de ADR: contexto, decisión, alternativas, consecuencias y revisión futura. |
| 58 | Matriz de decisión con criterios ponderados | Método cuantitativo ligero para comparar alternativas de arquitectura sin caer en falsa precisión. |
| 59 | Decisiones reversibles vs irreversibles | Clasificación práctica de decisiones y diseño de experimentos para reducir incertidumbre. |
| 60 | Riesgo técnico y riesgo de negocio | Diferencias, cruces y forma de priorizar mitigaciones en roadmap arquitectónico. |
| 61 | Comité técnico simulado I | Revisión de decisiones estructurales con preguntas de costo, tiempo, seguridad y operación. |
| 62 | Comité técnico simulado II | Defensa de cambios bajo escenarios de crisis, escalamiento y restricciones presupuestales. |

### Bloque 13. Diseño de API y contratos

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 63 | Diseño de contratos orientados a casos de uso | Cómo definir contratos útiles que expresen intención del negocio y eviten sobreexposición de datos. |
| 64 | Versionamiento de API sin romper clientes | Estrategias de compatibilidad hacia atrás y deprecación controlada. |
| 65 | Validación de entrada y errores consistentes | Estándar de validaciones, códigos de error y mensajes para clientes internos/externos. |
| 66 | Idempotencia en operaciones críticas | Técnicas para evitar duplicación de efectos en pagos, pedidos y asignaciones. |
| 67 | Contratos asíncronos en mensajería | Definición de esquemas de eventos, evolución de payloads y manejo de consumidores mixtos. |
| 68 | Documentación viva de interfaces | OpenAPI/AsyncAPI como contrato verificable y mecanismo de alineación entre equipos. |

### Bloque 14. Datos, persistencia y consistencia

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 69 | Elegir estrategia de persistencia por subdominio | Cuándo centralizar, cuándo separar y cómo justificar decisiones de almacenamiento. |
| 70 | Modelado de transacciones en procesos logísticos | Diseño de límites transaccionales para operaciones que cruzan inventario, pedido y despacho. |
| 71 | Patrones de consistencia eventual | Outbox, reintentos, deduplicación y compensaciones para flujos distribuidos. |
| 72 | Diseño de consultas de alto volumen | Estrategias de lectura optimizada, proyecciones y cache para paneles operativos. |
| 73 | Integridad de datos y reglas cruzadas | Mecanismos para mantener coherencia entre servicios sin acoplamiento rígido. |
| 74 | Migraciones seguras en producción | Estrategias expand-contract, dual write controlado y retrocompatibilidad de esquema. |

### Bloque 15. Observabilidad y operación

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 75 | Métricas que importan para arquitectura | Señales de latencia, errores, throughput y saturación para decisiones evolutivas. |
| 76 | Logs estructurados para diagnóstico rápido | Diseño de trazas de negocio y correlación de eventos entre componentes. |
| 77 | Trazabilidad distribuida en flujos críticos | Uso de trace-id/correlation-id para seguir un pedido entre servicios. |
| 78 | Alertas accionables y fatiga operativa | Definición de umbrales útiles y reducción de ruido en monitoreo. |
| 79 | Runbooks técnicos para incidentes frecuentes | Estandarización de respuesta operativa con pasos verificables y responsables claros. |
| 80 | Postmortem sin culpables | Método para aprender de incidentes y convertir hallazgos en mejoras concretas. |

### Bloque 16. Seguridad aplicada a arquitectura

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 81 | Threat modeling del caso logístico | Identificación de activos críticos, superficies de ataque y amenazas prioritarias. |
| 82 | Autenticación y autorización por contexto | Patrones para controlar acceso de clientes, operadores, repartidores y sistemas externos. |
| 83 | Gestión segura de secretos y credenciales | Prácticas de almacenamiento, rotación y uso seguro de credenciales en entornos múltiples. |
| 84 | Seguridad en APIs y eventos | Controles de validación, firma, cifrado y protección ante replay/fraude. |
| 85 | Privacidad y trazabilidad de datos sensibles | Clasificación de datos, minimización y auditoría alineada con cumplimiento. |
| 86 | Resiliencia ante abuso y disponibilidad maliciosa | Rate limiting, circuit breakers y controles de protección operacional. |

### Bloque 17. Calidad de código y evolución técnica

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 87 | Refactor arquitectónico guiado por riesgos | Cómo priorizar refactors de mayor retorno en mantenibilidad y estabilidad. |
| 88 | Modularización incremental sin detener entregas | Estrategias de extracción de módulos con continuidad de negocio. |
| 89 | Política de deuda técnica del equipo | Definición de criterios, presupuesto de deuda y seguimiento de acciones. |
| 90 | Fitness functions para arquitectura | Reglas automáticas para vigilar dependencias, complejidad y convenciones. |
| 91 | Pruebas de arquitectura y contratos internos | Validación automatizada de límites entre capas y módulos. |
| 92 | Roadmap de evolución a 12 meses | Plan de capacidad técnica, riesgos y hitos de arquitectura por trimestre. |

### Bloque 18. Sustentación avanzada y cierre integral

| # | Título del video | Qué trataría el video |
|---:|---|---|
| 93 | Estructura narrativa de defensa técnica | Cómo presentar decisiones para públicos mixtos: negocio, técnica y operación. |
| 94 | Simulación de jurado: preguntas de alto impacto | Banco de preguntas exigentes y forma de responder con evidencia y trade-offs. |
| 95 | Errores frecuentes al defender arquitectura | Fallos comunes en sustentación y cómo corregirlos antes de entrega final. |
| 96 | Cierre de la serie: checklist final del expediente | Revisión integral de artefactos, consistencia argumental y preparación de entrega definitiva. |

## Recomendación de publicación

- Publicar 2 videos por semana para cubrir la serie en 48 semanas.
- Alternar videos conceptuales y videos de demostración para mantener ritmo pedagógico.
- Cerrar cada video con una microtarea que alimente el expediente arquitectónico del proyecto.

## Rango de videos por actividad evaluativa

Sí: para organizar mejor el curso, conviene asociar cada actividad a un bloque de videos. La siguiente distribución mantiene coherencia con los objetivos de evaluación del semestre.

| Actividad | Rango de videos | Enfoque principal |
|---|---|---|
| Actividad 1. Diagnóstico y contexto | 1-20 | Comprensión del problema, actores, riesgos, requisitos iniciales y primera propuesta arquitectónica. |
| Actividad 2. Requisitos y decisión estructural | 21-40 | Trade-offs, elección de estilo, diseño de límites, dominio inicial y primeras decisiones de implementación. |
| Actividad 3. Diseño y dominio | 41-60 | Calidad interna del diseño, modelado del dominio, lenguaje ubicuo, ADR y gobierno de decisiones. |
| Actividad 4. Implementación e integración | 61-80 | Contratos API/eventos, persistencia, consistencia, integración externa, observabilidad y operación. |
| Actividad 5. Pruebas, operación y defensa final | 81-96 | Seguridad, evolución técnica, pruebas arquitectónicas, roadmap y sustentación final. |

### Cómo usar estos rangos

- Cada actividad debe cerrar con un entregable en GitHub y un video de sustentación.
- El video de sustentación de cada actividad debe resumir decisiones tomadas dentro de su rango.
- Si un equipo avanza más rápido, puede consumir videos del siguiente rango sin cambiar la fecha de entrega.

## Resultado esperado de la serie

Al finalizar los 96 videos, el estudiante tendrá un expediente completo y defendible: contexto, requisitos, decisiones estructurales, diseño limpio, modelado de dominio, implementación de vertical slices, pruebas, seguridad, operación, observabilidad y plan de evolución arquitectónica.
