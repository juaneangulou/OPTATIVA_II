# Video 23: Qué es el patrón Process Manager

## Para estudiar por tu cuenta
Una entrega no siempre se completa con una sola acción. Tal vez primero se confirme el pedido, luego se reserve el producto, después se asigne un repartidor y al final se notifique al cliente. ¿Quién recuerda en qué paso va cada pedido y qué hacer si un paso falla?

En esta clase aprenderás qué es un **Process Manager** (gestor de proceso), cómo coordina un flujo de varios pasos y por qué no debería reemplazar las responsabilidades de los servicios que participan.

## 1. Una orden puede necesitar varios trabajos
Cuando llega un pedido, la plataforma logística debe coordinar varias tareas:

1. Confirmar que el pedido puede atenderse.
2. Reservar los productos.
3. Crear una solicitud de entrega.
4. Asignar un repartidor.
5. Avisar al cliente.

Cada tarea puede pertenecer a una parte distinta del sistema. Algunas tardan más que otras, y no siempre terminan con éxito. El flujo necesita recordar qué ya ocurrió y qué paso corresponde después.

## 2. ¿Qué es un proceso?
Un **proceso** es una secuencia de pasos relacionada con un objetivo de negocio. En el ejemplo, el proceso es “preparar y completar la entrega del pedido 245”.

El proceso no es simplemente una lista fija de instrucciones. También debe considerar resultados distintos:

- ¿Qué hacemos si no hay productos?
- ¿Qué hacemos si no hay repartidores?
- ¿Qué hacemos si el cliente cancela antes de que salga el paquete?
- ¿Qué hacemos si un servicio tarda en responder?

## 3. ¿Qué es un Process Manager?
Un **Process Manager** es un componente que conserva el progreso de un proceso y decide cuál es el siguiente paso según las respuestas que va recibiendo.

Imagina a una persona que coordina una solicitud entre varias oficinas. No realiza el trabajo de cada oficina, pero anota qué se terminó, pregunta por el siguiente paso y decide qué hacer si algo no está disponible.

En el sistema, el Process Manager puede:

- Recordar que el pedido 245 está esperando una reserva.
- Pedir al servicio de Inventario que reserve productos.
- Recibir el resultado de Inventario.
- Si la reserva fue exitosa, pedir una asignación de entrega.
- Si falla, aplicar la respuesta que definió el proceso.

Cada servicio conserva su propio trabajo. Inventario decide si tiene unidades; Entregas asigna una ruta; el Process Manager coordina el orden y recuerda el estado general.

## 4. Palabras que aparecen en estos flujos
- **Estado del proceso:** información sobre el paso actual, como “esperando reserva” o “esperando repartidor”.
- **Comando o instrucción:** solicitud dirigida a un servicio para que haga algo, como “reserva los productos”.
- **Evento o resultado:** aviso de algo que ya ocurrió, como “productos reservados”.
- **Correlación:** forma de relacionar respuestas con el proceso correcto, normalmente mediante el identificador del pedido.
- **Compensación:** una acción de negocio que intenta corregir o contrarrestar un efecto anterior. No es borrar el pasado como si nunca hubiera ocurrido.

## 5. El flujo de una entrega, paso a paso
Usaremos el pedido 245:

### Paso 1: iniciar el proceso
Pedidos confirma la compra y comunica que puede empezar la preparación. El Process Manager crea un registro para el pedido 245 en estado “pendiente de reserva”.

Guardar el estado es importante porque el proceso puede durar segundos o minutos. El sistema no debe depender de que una computadora mantenga toda la secuencia solo en memoria.

### Paso 2: solicitar la reserva
El Process Manager envía al servicio de Inventario la instrucción “reserva los productos del pedido 245”.

### Paso 3: esperar el resultado
Inventario responde con uno de dos resultados:

- “Reserva realizada”.
- “No hay unidades suficientes”.

El Process Manager relaciona esa respuesta con el pedido 245 y guarda qué ocurrió.

### Paso 4A: si la reserva tuvo éxito
El proceso cambia a “pendiente de asignación” y solicita a Entregas que prepare el envío.

### Paso 4B: si no hay productos
El proceso no debe continuar como si sí los hubiera. Puede marcar el pedido para revisión, informar a Pedidos o iniciar una cancelación según las reglas del negocio.

### Paso 5: terminar o recuperarse
Cuando Entregas confirma que asignó un repartidor, el proceso marca la preparación como completada y permite enviar la notificación correspondiente. Si algo falla, conserva el paso y el error para continuar o resolverlo.

## 6. El recorrido dibujado
```text
Pedido confirmado
	|
	v
Process Manager: guarda “pendiente de reserva”
	|
	v
Inventario: recibe “reserva productos”
	|
	+── Reserva exitosa ──> Process Manager ──> pedir asignación a Entregas
	|
	+── Sin existencias ──> Process Manager ──> marcar revisión o cancelación
```

El Process Manager no controla cómo Inventario cuenta unidades ni cómo Entregas calcula una ruta. Coordina el proceso y toma decisiones sobre el siguiente paso del flujo.

## 7. ¿Qué pasa si una respuesta tarda o se repite?
En un sistema distribuido, las partes se comunican por la red. Una respuesta podría tardar, perderse o llegar después de que el proceso ya avanzó.

- Si Inventario tarda, el proceso puede permanecer en “pendiente de reserva” y volver a consultar según una política.
- Si la respuesta se repite, el Process Manager debe reconocer que corresponde al mismo pedido y no crear dos entregas.
- Si llega una respuesta para un pedido que ya se canceló, el proceso debe decidir si la ignora, la registra o inicia una compensación.

Una **compensación** no siempre puede deshacer literalmente una acción. Si se reservó inventario y después no se consigue repartidor, una compensación podría liberar las unidades. Si ya se envió un mensaje al cliente, no se puede hacer que nunca lo haya leído; se puede enviar una corrección.

## 8. ¿Qué guarda el Process Manager?
El registro puede incluir:

| Dato | Para qué sirve |
|---|---|
| Identificador del pedido | Relacionar todo con el pedido correcto |
| Paso actual | Saber qué tarea sigue o está pendiente |
| Resultados recibidos | No repetir decisiones ya tomadas |
| Intentos y momentos | Investigar retrasos y fallos |
| Decisión siguiente | Continuar, esperar, pedir revisión o cancelar |

No necesita guardar una copia de cada dato de todos los servicios. Guarda lo necesario para coordinar el proceso, mientras cada servicio conserva la información de su propia área.

## 9. Process Manager frente a coordinación directa
Para un proceso de dos pasos muy sencillo, un servicio podría llamar directamente al siguiente y esperar la respuesta. Esto es fácil de entender al principio.

Un Process Manager puede resultar útil cuando:

- Hay varios pasos y distintas rutas de éxito o error.
- El flujo dura más que una llamada inmediata.
- Se necesita recordar el progreso aunque el sistema se reinicie.
- Es importante reintentar, cancelar o compensar pasos.

También añade costo: otro componente, un estado que mantener y más casos que probar. Si el flujo es corto y no tiene estados complejos, la coordinación directa puede ser suficiente.

## 10. El Process Manager no debe convertirse en “el servicio que hace todo”
Un error sería trasladar al Process Manager las reglas internas de Inventario, Entregas, Pagos y Notificaciones.

Por ejemplo, el Process Manager puede preguntar si hay existencias y reaccionar a la respuesta. No debería inventar su propia forma de contar el inventario mientras el servicio de Inventario mantiene otra.

Su responsabilidad es coordinar el orden del proceso y recordar su progreso. Las decisiones locales y los datos detallados siguen en los servicios responsables.

## 11. Actividad de autoestudio
Un pedido requiere reservar productos, asignar repartidor y avisar al cliente. Si no se encuentra repartidor, se mantiene la reserva durante diez minutos; después se libera y el pedido pasa a revisión. El tiempo es una regla inventada para el ejercicio, no una recomendación universal.

1. Escribe los pasos del proceso en el orden correcto.
2. Dibuja el Process Manager y los servicios que participan.
3. Anota qué estado guardarías después de cada paso.
4. Explica qué harías si la confirmación de asignación llega dos veces.
5. Explica qué harías si pasan diez minutos sin repartidor.
6. Identifica una regla que pertenece a Inventario y otra que pertenece al proceso completo.

### Pistas
- No marques el proceso como completado solo porque se envió una solicitud.
- Relaciona cada respuesta con el identificador del pedido.
- Liberar la reserva es una acción nueva que corrige el flujo; no borra la reserva que sí ocurrió.

## 12. Solución comentada
1. Pedido confirmado → reservar productos → asignar repartidor → avisar al cliente.
2. El Process Manager se comunica con Inventario, Entregas y Notificaciones, y guarda el progreso del pedido.
3. Estados posibles: “esperando reserva”, “esperando asignación”, “esperando notificación” y “completado”. También se guardan “requiere revisión” o “cancelado” si el proceso toma esas rutas.
4. Si la respuesta repetida tiene el mismo identificador y ya se procesó, no se crea otra entrega; se conserva el resultado previo.
5. El proceso solicita liberar las unidades, registra el resultado y marca el pedido para revisión o cancelación según las reglas acordadas.
6. Inventario decide si puede reservar las unidades. El proceso decide que, si no se asigna repartidor dentro del plazo acordado, debe liberar la reserva y pedir revisión.

## 13. Comprueba lo que aprendiste
1. ¿Qué información conserva un Process Manager?
2. ¿Qué diferencia hay entre coordinar una reserva y decidir cuántas unidades hay disponibles?
3. ¿Por qué una compensación no siempre equivale a deshacer una acción?
4. ¿Cuándo puede ser suficiente una coordinación directa?

### Respuestas
1. El paso actual, las respuestas recibidas y la decisión sobre el siguiente paso del proceso.
2. Coordinar significa pedir la reserva y reaccionar al resultado; Inventario es responsable de conocer y actualizar sus unidades.
3. Algunas acciones ya tuvieron efectos visibles o externos; pueden requerir una acción correctiva, no borrarse.
4. Cuando hay pocos pasos, respuesta inmediata y pocos caminos de error, sin necesidad de conservar un proceso largo.

## Conclusión
Un Process Manager coordina una secuencia de tareas, recuerda dónde va cada caso y decide el paso siguiente según las respuestas. Ayuda cuando el flujo tiene duración, alternativas y fallos que deben gestionarse.

No sustituye a los servicios que realizan cada tarea. Su valor está en que el proceso completo no dependa de memoria improvisada; su costo está en que hay que guardar, probar y mantener sus estados y decisiones.
