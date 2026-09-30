# Video 20: Patrón productor consumidor vs fan-in y fan-out

## Título
Quién produce una tarea, quién la procesa y hacia dónde viaja la información

## Situación
Cuando se confirma un pedido, la plataforma logística debe iniciar la preparación, avisar al cliente y guardar el hecho para análisis. Además, el historial de una entrega puede recibir actualizaciones del almacén, del repartidor y del cliente.

Para organizar estos flujos distinguimos tres ideas:

- **Productor-consumidor:** una parte crea una tarea y otra la recoge y procesa, normalmente usando una cola para esperar.
- **Fan-out:** una fuente distribuye información a varios destinos.
- **Fan-in:** varias fuentes envían información a un destino común.

No son alternativas excluyentes. Describen aspectos distintos del recorrido y pueden combinarse en un mismo sistema.

## Ejemplos

### Productor-consumidor
Pedidos crea una tarea de entrega y la deja en una cola. Entregas la recoge cuando puede procesarla. Si hay varios trabajadores, normalmente cada tarea la procesa uno de ellos, no todos.

### Fan-out
El hecho “Pedido confirmado” se comunica a Entregas, Notificaciones y Análisis. Cada destino necesita enterarse y puede realizar un trabajo diferente.

### Fan-in
Almacén, repartidor y cliente envían actualizaciones de la entrega a un registro común que construye el historial del pedido.

## Una diferencia que conviene recordar
Una cola compartida puede repartir el trabajo entre varios trabajadores: cada tarea la procesa uno. Fan-out busca que varios destinos reciban el mismo hecho. Si ambos comportamientos se confunden, un área que debía enterarse podría no recibir nada.

## Riesgos a considerar
- Una cola puede acumular tareas si llegan más rápido de lo que se procesan.
- Una tarea puede recibirse más de una vez; el consumidor debe evitar efectos duplicados.
- En fan-in, las actualizaciones pueden llegar en diferente orden.
- En fan-out, un destino puede fallar mientras los otros ya procesaron el hecho.

## Preguntas para comprobar tu comprensión
- ¿Qué patrón describe varias fuentes que alimentan un historial común?
- ¿Qué patrón describe un evento que se comunica a varias áreas?
- ¿En qué se diferencia una cola compartida de fan-out?
- ¿Se pueden usar productor-consumidor y fan-out juntos?
