# Video 13: Liderazgo, negociación e impacto social

## Fuentes de este video
- [Comunicación, liderazgo y negociación técnica](https://platzi.com/cursos/fundamentos-arquitectura-software/evolucion-del-software-personal-hacia-el/)
- [Arquitectura con impacto social y valor real](https://platzi.com/cursos/fundamentos-arquitectura-software/preguntas-clave-que-todo-arquitecto-de-s/)

## Navegación
[⬅️ Video anterior: estrategia tecnológica y roadmap](video-12.md) | [📚 Índice de la serie](README.md) | [➡️ Video siguiente: transición a la arquitectura aplicada](video-14.md)

## Para estudiar por tu cuenta
Una decisión de arquitectura afecta a personas distintas, aunque solo una parte del equipo escriba el código. En este capítulo no volverás a priorizar un roadmap: practicarás cómo convertir desacuerdos concretos en una decisión negociada, con límites de privacidad y una prueba que permita revisarla.

El caso será el seguimiento de repartidores. La empresa quiere ofrecer al cliente una experiencia más clara; el repartidor también necesita privacidad y seguridad. Tu objetivo es comparar opciones y justificar una decisión equilibrada.

## 1. Qué aporta cada fuente
La primera fuente trata la comunicación, el liderazgo y la negociación técnica. Su idea central es que una decisión no se implementa solo porque alguien la diseñó: otras personas deben comprender su propósito, sus límites y el trabajo que implica.

La segunda fuente conecta arquitectura con impacto social y valor real. El sistema afecta tiempo, datos, confianza y condiciones de trabajo; por eso una solución técnicamente posible no siempre es responsable para todas las personas involucradas.

Las dos fuentes se conectan así: comunicar bien permite descubrir a quién afecta una decisión; comprender ese impacto permite negociar una solución mejor que imponer la primera opción.

## 2. Conceptos en palabras sencillas
- **Liderazgo técnico:** ayudar al equipo a entender el problema y avanzar con una decisión explicable. No significa decidir por todos.
- **Negociación:** buscar un acuerdo entre necesidades diferentes, sin esconder costos ni riesgos.
- **Impacto social:** consecuencias que la solución tiene para personas y grupos, como privacidad, accesibilidad, seguridad o carga de trabajo.
- **Trade-off:** beneficio que se obtiene a cambio de aceptar un costo o una limitación.

## 3. El caso: mostrar la ubicación de un repartidor
Atención al cliente recibe muchas preguntas porque el estado del pedido tarda en actualizarse. Alguien propone mostrar en un mapa la ubicación exacta del repartidor durante toda su jornada.

Antes de aceptar esa propuesta, define el problema con precisión: el cliente necesita saber si la entrega se acerca; soporte necesita explicar retrasos. La ubicación exacta todo el día es una solución posible, no la necesidad original.

Identifica a quienes reciben el impacto:

| Actor | Necesidad | Riesgo posible |
|---|---|---|
| Cliente | Saber si su paquete está próximo | Recibir una posición desactualizada como si fuera actual |
| Repartidor | Completar entregas de forma segura | Exponer su ubicación fuera del trabajo de una entrega |
| Soporte | Resolver preguntas sobre retrasos | No poder reconstruir qué estado se comunicó |
| Operación | Coordinar rutas | Recopilar más información personal de la necesaria |

## 4. Distingue posiciones e intereses
Una **posición** es una petición concreta: “quiero ubicación en vivo” o “no compartamos ninguna ubicación”. El **interés** es la necesidad detrás: reducir incertidumbre, proteger privacidad o resolver una entrega tardía.

Al buscar intereses puedes proponer alternativas que las posiciones iniciales no mostraban. El cliente quizá solo necesite una hora estimada; soporte quizá necesite un historial de estados; el repartidor puede aceptar que la ubicación se muestre solo durante una entrega activa.

## 5. Comparación de opciones

| Opción | Qué recibe el cliente | Beneficio | Costo o riesgo |
|---|---|---|---|
| A. Estado del pedido y hora estimada | “En camino; llega entre 14:00 y 14:30” | Menos datos de ubicación expuestos | La estimación puede cambiar |
| B. Ubicación aproximada durante la entrega activa | Una zona aproximada y su hora de actualización | Puede reducir la incertidumbre en tiempo real | Requiere permisos y limitar cuándo se consulta |
| C. Ubicación exacta durante toda la jornada | Movimiento continuo del repartidor | Mucho detalle para la operación | Exposición de ubicación más amplia de la necesaria |

No hay una alternativa universal. La elección depende del valor para el cliente, las condiciones de trabajo, las reglas de privacidad y la capacidad de proteger la información.

## 6. Una decisión argumentada
Para una primera versión, podrías mostrar estado y hora estimada. Si después la evidencia muestra que hace falta ubicación, prueba la opción B durante una entrega activa, con acceso limitado y una hora visible para identificar datos antiguos.

Una defensa clara de esa decisión sería: “Resolvemos la incertidumbre del cliente con estado y estimación. No guardamos ubicación continua porque no hemos demostrado que sea necesaria. Revisaremos la elección si las consultas a soporte siguen siendo altas y si una prueba controlada demuestra un beneficio adicional”.

La decisión incluye una condición de revisión; no se presenta como correcta para siempre.

## 7. Cómo negociar sin ocultar el problema
Cuando dos áreas proponen soluciones diferentes, organiza la conversación así:

1. Repite el problema común con palabras neutrales.
2. Separa lo que ya se sabe de lo que todavía se supone.
3. Pregunta qué resultado necesita cada actor.
4. Compara opciones y costos con los mismos criterios.
5. Escribe los límites que no se deben romper.
6. Define una prueba que permita aprender si la decisión funcionó.

Esto evita que la discusión se convierta en “mi tecnología contra la tuya”.

## 8. Actividad de autoestudio
La empresa quiere guardar la ubicación exacta del repartidor durante toda la jornada para reducir consultas de clientes.

1. Escribe el problema que intenta resolver sin repetir la solución propuesta.
2. Identifica tres actores y lo que necesita cada uno.
3. Anota un hecho y una suposición.
4. Propón dos alternativas que recopilen menos información.
5. Elige una opción inicial y explica un costo aceptado.
6. Define una prueba y una señal que justificaría revisar la decisión.

### Pistas
- “La ubicación continua reducirá las consultas” es una hipótesis que se puede medir.
- No todo el mundo necesita ver la misma información.
- Una ubicación antigua debe identificarse como antigua.

## 9. Respuesta modelo
El problema es que el cliente no sabe si su paquete llegará pronto y soporte recibe consultas repetidas. El cliente necesita una estimación; el repartidor necesita que la ubicación no quede expuesta fuera de entregas activas; soporte necesita el último estado y su hora.

Un hecho del caso es que hoy no hay una vista única del estado. Una suposición es que compartir la posición exacta todo el día reducirá las consultas.

Una opción es mostrar estado y hora estimada. Otra es mostrar ubicación aproximada solo durante una entrega activa. Elegiría primero la estimación porque requiere menos exposición de datos; mediría consultas y retrasos durante un período definido. Si no mejora la experiencia, evaluaría la ubicación aproximada con límites de acceso y retención.

## Comprueba lo que aprendiste
1. ¿Qué diferencia hay entre la necesidad y la solución propuesta?
2. ¿Por qué importa identificar varios actores?
3. ¿Qué información debe acompañar una ubicación que podría estar desactualizada?
4. ¿Qué significa dejar una condición de revisión?

### Respuestas
1. La necesidad describe el problema; la solución es una manera posible de resolverlo.
2. Una decisión puede beneficiar a un grupo y crear riesgos para otro.
3. La hora de la última actualización y una indicación de que no necesariamente es actual.
4. Especificar qué evidencia futura haría reexaminar la decisión.

## Cierre
El liderazgo técnico no es elegir por otras personas. Es aclarar el problema, hacer visibles los impactos, negociar alternativas y comprobar qué resultado produjo la decisión.
