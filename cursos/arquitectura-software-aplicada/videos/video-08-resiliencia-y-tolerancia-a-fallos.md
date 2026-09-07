# Video 8: Resiliencia y tolerancia a fallos

## Título
Resiliencia y tolerancia a fallos

## Resumen
Este video introduce la idea de que ningún sistema es completamente estable ni inmune a fallos. Internet, servicios externos, bases de datos, dependencias y cambios de carga pueden afectar el funcionamiento normal. Por eso, una arquitectura robusta no se define por la ausencia de errores, sino por la capacidad de responder a ellos sin colapsar el servicio completo.

La resiliencia consiste en diseñar sistemas que puedan degradar con elegancia, recuperar automáticamente y continuar ofreciendo valor incluso cuando una parte falle. El video enfatiza que la tolerancia a fallos no es una característica extra; es un criterio de diseño funcional en sistemas reales. Esto incluye reintentos, timeouts, circuit breakers, replicas, backups y una estrategia clara de recuperación.

## Ideas principales
- Los fallos son inevitables en sistemas distribuidos y complejos.
- La resiliencia es la capacidad de recuperarse sin perder el servicio completo.
- La degradación controlada es mejor que un colapso total.
- La arquitectura debe anticipar errores en dependencias y en infraestructura.
- Los sistemas robustos incorporan mecanismos para continuar funcionando bajo presión.
- La disponibilidad y la confiabilidad tienen costos, pero también protegen la experiencia del usuario.

## Conclusión
Un sistema no se vuelve bueno solo porque “anda en el momento”, sino porque puede resistir fallos y seguir entregando valor. La resiliencia es una de las habilidades más importantes de una arquitectura moderna.

## Preguntas para reflexión
- ¿Qué pasa si uno de mis servicios falla hoy?
- ¿Mi sistema degrada de forma controlada o colapsa por completo?
- ¿Estoy monitoreando y preparando la recuperación de fallos antes de que pasen?
