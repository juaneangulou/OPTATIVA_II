# Video 20: Patrón productor consumidor vs fan-in y fan-out

## Para estudiar por tu cuenta
En esta clase aprenderás tres ideas para mover tareas e información entre partes de un sistema. Aunque a veces se presentan juntas, no describen exactamente lo mismo:

- **Productor-consumidor** explica quién crea un trabajo y quién lo procesa.
- **Fan-in** explica cómo varias fuentes se reúnen en un destino.
- **Fan-out** explica cómo una fuente distribuye información a varios destinos.

No necesitas programar. Usaremos ejemplos de una plataforma de entregas y dibujos para que puedas reconocer cada forma de comunicación.

## 1. Empecemos con una situación
Una plataforma logística recibe pedidos durante todo el día. Cada pedido confirmado requiere que se prepare una entrega. A veces entran muchos pedidos al mismo tiempo y los servicios que preparan las entregas no alcanzan a procesarlos de inmediato.

En vez de obligar al servicio de Pedidos a esperar mientras Entregas completa cada tarea, podemos separar dos trabajos:

1. Pedidos registra la nueva tarea.
2. Entregas la procesa cuando tiene capacidad.

Para comprender esta solución, primero veamos quién produce y quién consume.

## 2. ¿Qué es un productor?
Un **productor** es la parte que crea o envía un dato, una tarea o una notificación para que otra parte la use.

En nuestro ejemplo, Pedidos es productor cuando deja una tarea como “preparar la entrega del pedido 245”. El productor conoce que la compra quedó lista, pero no necesita realizar todo el trabajo de entrega.

## 3. ¿Qué es un consumidor?
Un **consumidor** es la parte que recibe esa información y trabaja con ella.

Entregas es consumidor cuando recoge la tarea y empieza a preparar la ruta. Consumir no significa borrar un dato de manera automática; significa que la parte recibió información para procesarla. El sistema debe registrar si el trabajo se completó, falló o todavía está pendiente.

## 4. ¿Qué es una cola?
Una **cola** es un lugar intermedio donde se guardan tareas pendientes. Se parece a una fila de solicitudes:

```text
Pedidos (productor) ──> Cola de entregas ──> Entregas (consumidor)
```

La cola permite que Pedidos deje el trabajo y continúe, aunque Entregas esté ocupado durante unos minutos. Cuando el consumidor queda libre, recoge una tarea.

Esto separa el momento de crear el trabajo del momento de procesarlo. No hace que el trabajo desaparezca ni garantiza que siempre se complete: ayuda a conservarlo y organizarlo para que se procese después.

## 5. El recorrido de una tarea
Sigamos la tarea del pedido 245:

1. **Pedidos confirma la compra.** El pedido queda listo para iniciar la preparación.
2. **Pedidos crea una tarea.** La tarea indica qué pedido debe preparar Entregas.
3. **La cola guarda la tarea.** Si Entregas está ocupado, queda pendiente.
4. **Entregas recoge la tarea.** El consumidor comienza el trabajo.
5. **Entregas registra el resultado.** Puede indicar que la preparación terminó o que requiere atención.

La cola sirve como espacio de espera. Pedidos no tiene que conocer cuántas personas de Entregas están trabajando ni esperar a que se libere una.

## 6. ¿Qué pasa si hay varios consumidores?
Imagina que hay tres trabajadores disponibles leyendo tareas de una misma cola. Una tarea de preparación debe ser atendida por una persona, no por las tres a la vez.

```text
Pedidos ──> Cola ──> Trabajador A
				 ├─> Trabajador B
				 └─> Trabajador C
```

Si los trabajadores están configurados como un grupo que comparte el trabajo, normalmente uno recoge cada tarea. Esto permite procesar varias tareas en paralelo, aunque el equipo debe cuidar que dos trabajadores no realicen accidentalmente la misma asignación.

Esto se diferencia de enviar una copia del mismo aviso a tres áreas interesadas. Esa distribución a múltiples destinos es fan-out y la veremos más adelante.

## 7. ¿Qué significa fan-in?
**Fan-in** significa que varias fuentes envían información hacia un punto común. “In” ayuda a recordar que varios caminos entran.

En logística, imagina que tres lugares informan cambios de una entrega:

- El almacén informa que el paquete fue preparado.
- El repartidor informa que lo recogió.
- El cliente informa que lo recibió.

Esas actualizaciones pueden reunirse en un servicio que construye la historia de la entrega:

```text
Almacén ─────────┐
Repartidor ──────┼──> Registro de seguimiento
Cliente ─────────┘
```

El destino común debe poder reconocer de dónde vino cada actualización y a qué entrega pertenece. Si no lo hace, podría confundir dos pedidos o interpretar el orden incorrectamente.

Fan-in describe la forma de los caminos. No indica por sí solo si los mensajes esperan en una cola ni quién es el productor o consumidor; esas decisiones se pueden combinar.

## 8. ¿Qué significa fan-out?
**Fan-out** significa que una fuente distribuye información a varios destinos. “Out” ayuda a recordar que los caminos salen hacia afuera.

Cuando el pedido 245 queda confirmado, diferentes áreas pueden necesitar enterarse:

- Entregas necesita iniciar la preparación.
- Notificaciones necesita avisar al cliente.
- Análisis necesita contar pedidos confirmados.

La información sale de un origen y se dirige a varios destinos:

```text
					┌──> Entregas
Pedido confirmado ──┼──> Notificaciones
					└──> Análisis
```

Cada destino recibe la información y decide qué trabajo le corresponde. Notificaciones no debe reservar productos, y Análisis no debe cambiar el pedido; cada consumidor mantiene su responsabilidad.

## 9. ¿Todos reciben una tarea o cada uno recibe una copia?
Esta diferencia es importante:

- En una **cola de trabajo compartida**, varios trabajadores compiten por tareas. Cada tarea se asigna para que la procese un trabajador del grupo.
- En un **fan-out**, cada área interesada necesita enterarse del mismo hecho. El sistema organiza la entrega para que cada destino reciba una copia o una versión de la información.

Si Entregas y Notificaciones leen de una sola fila de trabajo que se reparte entre ambos, podría ocurrir que solo uno reciba la tarea. Eso sería incorrecto si ambos deben actuar.

Antes de elegir una configuración, pregunta: **¿quiero repartir el trabajo para que una sola persona lo haga, o quiero informar el mismo hecho a varias áreas?**

## 10. Comparación directa
| Idea | Qué describe | Ejemplo logístico | Pregunta para reconocerla |
|---|---|---|---|
| Productor-consumidor | Quién crea una tarea y quién la procesa | Pedidos deja una tarea; Entregas la realiza | ¿Quién produce el trabajo y quién lo consume? |
| Fan-in | Varias fuentes convergen en un destino | Almacén, repartidor y cliente informan cambios al seguimiento | ¿Varias flechas entran a un punto? |
| Fan-out | Una fuente distribuye a varios destinos | Pedido confirmado informa a Entregas, Notificaciones y Análisis | ¿Una flecha se reparte hacia varios puntos? |

**No son patrones excluyentes.** Una solución puede usar productor-consumidor y fan-out al mismo tiempo: Pedidos publica un hecho, el sistema lo distribuye a varias áreas y cada área pone su trabajo pendiente en una cola propia para procesarlo después.

## 11. Un mismo sistema puede combinar las tres formas
Veamos el flujo de un pedido completo:

### Fan-out al confirmar el pedido
Pedidos confirma la compra y avisa a Entregas, Notificaciones y Análisis. Un mismo hecho interesa a varios destinos.

### Productor-consumidor para preparar cada entrega
Pedidos deja una tarea en la cola de Entregas. El servicio de Entregas la recoge cuando puede procesarla.

### Fan-in para formar la historia de entrega
Almacén, repartidor y cliente envían actualizaciones a Seguimiento. Seguimiento las reúne para mostrar la historia del pedido.

Así, los patrones resuelven preguntas distintas:

- ¿Quién crea el trabajo y quién lo procesa? Productor-consumidor.
- ¿Cómo se reúnen las actualizaciones de varias fuentes? Fan-in.
- ¿Cómo se informa un hecho a varios destinos? Fan-out.

## 12. Problemas que debemos prever

### La tarea tarda en procesarse
Una cola puede acumular solicitudes cuando hay más trabajo del que se procesa. El equipo debe observar cuánto crece la fila y si Entregas tiene capacidad suficiente.

### Una tarea se recibe más de una vez
Una comunicación puede repetirse. Si procesarla dos veces crea dos repartos para un pedido, el consumidor debe reconocer la repetición y evitar duplicar el efecto.

### Una tarea no se puede procesar
Puede faltar información o el sistema puede estar temporalmente indisponible. La tarea no debería desaparecer silenciosamente: se registra el problema y se define cómo reintentar o pedir revisión. El video siguiente profundiza en qué hacer con mensajes que siguen fallando.

### Los datos llegan en un orden distinto
En fan-in, una actualización de “entregado” podría llegar antes que una de “recogido”. El destino necesita comparar el momento o la secuencia de los hechos y no asumir que el último en llegar ocurrió después.

### Un destino de fan-out falla
Si Entregas recibe el aviso pero Notificaciones no, el sistema debe poder reintentar el aviso a Notificaciones sin repetir el trabajo de Entregas.

## 13. Actividad de autoestudio: clasifica los flujos
Decide si cada situación muestra productor-consumidor, fan-in, fan-out o una combinación. Justifica tu respuesta con una frase.

1. Pedidos deja tareas en una cola y Entregas las procesa cuando queda disponible.
2. Almacén, repartidor y cliente reportan datos que se reúnen en el historial del pedido.
3. El hecho “Pedido confirmado” se comunica a Entregas, Notificaciones y Análisis.
4. Tres trabajadores comparten una cola para procesar distintas entregas.
5. Un mensaje de pedido confirmado se distribuye a varios servicios y, después, cada servicio crea tareas que procesa por separado.

## 14. Respuesta comentada
1. **Productor-consumidor:** Pedidos produce tareas y Entregas las consume desde la cola.
2. **Fan-in:** varias fuentes envían actualizaciones a un destino que las reúne.
3. **Fan-out:** un origen comunica un mismo hecho a varios destinos.
4. **Productor-consumidor con varios consumidores:** varios trabajadores se reparten las tareas de la cola; no significa que todos ejecuten cada entrega.
5. **Combinación:** hay fan-out cuando se informa a varios servicios y productor-consumidor cuando cada uno procesa sus tareas pendientes.

Si una situación parece encajar en más de un patrón, describe qué aspecto estás nombrando. La misma solución puede tener productores, consumidores y una forma de distribución al mismo tiempo.

## 15. Diseña una solución para una entrega
Una entrega puede generar tres necesidades:

- Preparar el paquete.
- Avisar al cliente que ya salió.
- Guardar la actualización en el historial.

Responde:

1. ¿Qué parte produce el hecho de que la entrega salió?
2. ¿Qué destinos necesitan enterarse?
3. ¿Cuál de esas áreas requiere una tarea pendiente que se procese después?
4. Dibuja el flujo y escribe “fan-out”, “fan-in” o “productor-consumidor” junto a cada parte que corresponda.
5. ¿Qué debería ocurrir si falla el aviso al cliente pero el historial sí se actualiza?

### Una solución posible
Entregas produce el hecho “Entrega salió”. Ese hecho se distribuye a Notificaciones y al servicio de historial: eso es fan-out. Notificaciones crea una tarea para enviar el aviso y un consumidor la procesa: eso es productor-consumidor. Si varias fuentes —almacén, repartidor y cliente— reportan cambios al historial, el registro que los reúne usa fan-in.

Si falla el aviso, se puede reintentar ese trabajo sin borrar el hecho de que la entrega salió ni repetir la actualización del historial. Cada destino necesita registrar su propio resultado.

## 16. Autoevaluación
Responde sin mirar el texto y comprueba con la clave:

1. ¿Qué diferencia hay entre productor-consumidor y fan-out?
2. En una cola compartida por tres trabajadores, ¿cada trabajador debe realizar todas las tareas?
3. ¿Qué significa fan-in?
4. ¿Se pueden usar fan-out y productor-consumidor juntos?
5. ¿Qué harías si un consumidor recibe dos veces la misma tarea?

### Clave de respuestas
1. Productor-consumidor describe quién crea y procesa trabajo; fan-out describe que una fuente distribuye información a varios destinos.
2. No. En una cola de trabajo compartida, normalmente cada tarea la procesa un trabajador del grupo.
3. Varias fuentes envían información a un punto común.
4. Sí. El mismo hecho puede llegar a varios destinos y cada destino puede procesar sus tareas con una cola.
5. Comprobar si ya procesó esa tarea y evitar repetir un efecto que no debe duplicarse.

Si puedes explicar las formas de las flechas y quién hace el trabajo, comprendiste la diferencia central. No necesitas memorizar un producto o una tecnología para reconocer el patrón.

## Conclusión
Productor-consumidor separa a quien crea una tarea de quien la procesa. Fan-in reúne información de varias fuentes; fan-out distribuye información de una fuente a varios destinos. Son maneras distintas de describir un flujo y pueden combinarse.

Al diseñar, primero pregunta qué debe ocurrir con la información: ¿se procesa una tarea?, ¿se reúnen actualizaciones?, ¿varias áreas deben enterarse? Luego define cómo manejar retrasos, repeticiones y fallas, para que una tarea importante no desaparezca ni se ejecute de manera incorrecta.

## Preguntas para llevarte
- ¿Qué patrón reconoces en una cola de tareas compartida por varios trabajadores?
- ¿Qué forma tiene un flujo fan-in? ¿Y uno fan-out?
- ¿Por qué productor-consumidor puede aparecer dentro de una solución fan-out?
- ¿Qué problema del sistema real resolverías primero con estos patrones?
