# Video 09: Observabilidad, seguridad y privacidad

## Fuentes oficiales
- [Platzi: Observabilidad y monitoreo de sistemas](https://platzi.com/cursos/fundamentos-arquitectura-software/como-funcionan-los-eventos-en-sistemas-d/)
- [Platzi: Seguridad, datos sensibles y privacidad](https://platzi.com/cursos/fundamentos-arquitectura-software/costos-ocultos-de-los-microservicios/)

## 🔗 Navegación
[⬅️ Video anterior](video-08.md) | [➡️ Video siguiente](video-10.md)

## Propósito
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

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
La observabilidad es una parte central de la arquitectura porque permite entender, prevenir y corregir problemas antes de que se vuelvan críticos.

La seguridad y la privacidad no son requisitos secundarios: son elementos fundamentales de una arquitectura responsable y confiable.

## Preguntas para preparar la grabación
- ¿Qué tan claro es el estado actual de mi sistema en producción?
- ¿Estoy monitoreando lo que realmente importa?
- ¿Qué datos sensibles maneja mi sistema?
- ¿Estoy reduciendo la exposición innecesaria de información?

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
