# Video 21: Métricas y migración Strangler Fig

## Fuentes oficiales
- [Platzi: Observabilidad y operabilidad](https://platzi.com/cursos/software-avanzado/metricas-cuantitativas-para-evaluar-arqu/)
- [Platzi: DevOps, despliegue y automatización](https://platzi.com/cursos/software-avanzado/strangler-fig-para-migrar-arquitecturas/)

## 🔗 Navegación
[⬅️ Video anterior](video-20.md) | [➡️ Video siguiente](video-22.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
**Fuente 1: Observabilidad y operabilidad**
El video destaca que una arquitectura no termina cuando el sistema “funciona” en un entorno local. La verdadera prueba de madurez llega cuando el equipo puede entender qué está sucediendo en producción, detectar fallos y responder con rapidez. Por eso la observabilidad es una parte esencial del diseño: métricas, logs, trazas y alertas ayudan a transformar el sistema en algo operable y diagnósticable.

Cuando una solución no es observable, el equipo se mueve a ciegas y las correcciones se vuelven reactivas. La operabilidad mejora cuando se diseña para monitoreo, diagnóstico y recuperación. El video deja claro que observar el sistema es una decisión arquitectónica, no un extra de operaciones.

**Fuente 2: DevOps, despliegue y automatización**
Este video conecta arquitectura con entrega continua y operación real. La forma en que se despliega una aplicación afecta directamente la estabilidad, velocidad y capacidad de innovación del equipo. Cuando el despliegue es manual, propenso a errores o difícil de repetir, la arquitectura se vuelve frágil incluso si el diseño técnico es bueno.

La automatización del despliegue, la integración continua, la orquestación y la infraestructura como código permiten que el sistema evolucione con menos riesgos. El video muestra que la arquitectura moderna no se limita a la aplicación, sino al flujo completo de entrega: código, integración, pruebas, despliegue, observabilidad y rollback. Esto hace que la calidad del sistema dependa también del proceso que lo lleva a producción.

## Ideas que debes conservar
- La observabilidad permite entender el comportamiento real del sistema.
- Logs, métricas y trazas ayudan a detectar fallas y cuellos de botella.
- Un sistema difícil de diagnosticar termina costando más en producción.
- La operación debe estar integrada en el diseño desde el principio.
- El despliegue es parte de la arquitectura, no una etapa separada.
- La automatización reduce errores humanos y acelera la entrega.
- La infraestructura debe ser reproducible y controlada.
- La calidad del proceso impacta la calidad del sistema.

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
Un sistema bien diseñado no solo responde a requerimientos, sino que también puede ser comprendido y mantenido en producción. La observabilidad es uno de los pilares para convertir una solución técnica en una solución operable.

La arquitectura moderna integra desarrollo, operación y entrega. Un sistema no se considera bien diseñado si no puede entregarse, operar y evolucionar de manera segura y repetible.

## Preguntas para preparar la grabación
- ¿Qué tanto sabemos realmente qué está pasando en producción?
- ¿Mi sistema me alerta antes de que el usuario lo note?
- ¿Mi despliegue es repetible y automatizado?
- ¿Qué tan rápido puedo revertir un cambio problemático?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
