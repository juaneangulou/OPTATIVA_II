# Video 14: Strangler Fig para migrar arquitecturas limpias

## Para empezar
Este video explica una forma de cambiar un sistema antiguo sin tener que apagarlo y construir todo de nuevo de una sola vez. No necesitas conocer programación para entender la idea: vamos a imaginar que una empresa quiere renovar su sistema mientras sigue atendiendo a sus clientes.

Un **sistema antiguo** es el programa que la organización ya usa. Puede seguir funcionando, pero tal vez sea difícil de cambiar. **Migrar** significa pasar poco a poco el trabajo de ese sistema a uno nuevo.

## ¿Qué significa Strangler Fig?
Strangler Fig es el nombre en inglés de una técnica de migración. La metáfora viene de una planta que crece alrededor de un árbol: lo va cubriendo poco a poco hasta que, con el tiempo, ocupa su lugar.

En software, hacemos algo parecido: el sistema nuevo empieza a atender una parte pequeña del trabajo. El sistema antiguo continúa atendiendo el resto. Después, cuando comprobamos que esa parte nueva funciona, podemos pasarle otra tarea. Repetimos el proceso hasta que el sistema antiguo ya no tenga trabajo que hacer.

La idea importante es **reemplazar por partes, no todo de una vez**.

## ¿Por qué no cambiarlo todo en un solo paso?
Imagina que una tienda cambia al mismo tiempo la caja, el inventario, los pedidos y el sistema de entregas. Si algo deja de funcionar, será difícil saber qué cambio causó el problema. Además, la tienda podría dejar de atender mientras se arregla.

Si cambia una parte a la vez, la tienda puede seguir trabajando. El equipo también puede revisar cada cambio antes de continuar. Este método reduce el tamaño del riesgo, aunque requiere mantener el sistema antiguo y el nuevo funcionando al mismo tiempo durante una etapa.

## Las palabras que usaremos
- **Parte del sistema:** una tarea concreta, como consultar el estado de un pedido.
- **Desviar una solicitud:** decidir si una petición la atiende el sistema antiguo o el nuevo. Es como enviar una llamada al área correcta.
- **Sistema antiguo:** el programa que ya está en uso y que todavía resuelve algunas tareas.
- **Sistema nuevo:** la solución que va reemplazando esas tareas poco a poco.
- **Volver atrás:** hacer que una tarea regrese temporalmente al sistema antiguo si el cambio nuevo falla.

No es necesario memorizar estos nombres. Lo importante es saber quién hace cada tarea y cómo seguir atendiendo a las personas mientras se cambia el sistema.

## Ejemplo guiado: plataforma logística
Una empresa usa un solo programa para recibir pedidos, revisar el inventario y organizar las entregas. El programa funciona, pero es difícil modificar la parte que informa al cliente dónde está su pedido.

La empresa quiere crear una nueva función para consultar el seguimiento de las entregas. En vez de reemplazar todo el programa, puede hacer lo siguiente:

### Paso 1: elegir una tarea pequeña
El equipo decide empezar solo con la consulta del estado de una entrega. Los pedidos, el inventario y la asignación de repartidores siguen en el sistema antiguo.

### Paso 2: decidir a dónde va cada consulta
Cuando alguien pregunta “¿dónde está mi pedido?”, una puerta de entrada revisa la solicitud y la envía al sistema nuevo. Las demás tareas continúan yendo al sistema antiguo.

La **puerta de entrada** es simplemente el punto que recibe una petición y la dirige al lugar que debe responderla. No hace falta imaginar una herramienta específica: basta entender su función, como la recepción de un edificio que indica a qué oficina ir.

### Paso 3: comprobar que el sistema nuevo responde bien
El equipo verifica casos sencillos: el pedido existe, aparece su estado correcto y se muestra cuándo fue actualizado. También revisa que las otras tareas, como crear pedidos nuevos, sigan funcionando en el sistema antiguo.

### Paso 4: tener una manera de volver atrás
Si el seguimiento nuevo muestra información incorrecta o deja de responder, el equipo puede cambiar el destino de esas consultas para que las atienda otra vez el sistema antiguo mientras investiga el problema.

### Paso 5: continuar solo cuando haya evidencia
Cuando el seguimiento nuevo funciona de manera confiable, el equipo puede escoger otra tarea pequeña para migrar. No pasa todo lo demás automáticamente: cada nueva parte necesita su propia revisión.

### Paso 6: retirar lo antiguo cuando ya no haga falta
El sistema antiguo no se apaga al principio. Se retira solo cuando el equipo ha comprobado que las tareas importantes ya fueron trasladadas y que nadie depende de la parte antigua.

## El recorrido en una tabla
Este es un ejemplo ilustrativo, no el resultado de una migración real:

| Momento | Quién consulta el estado del pedido | Qué sigue en el sistema antiguo |
|---|---|---|
| Antes de empezar | Sistema antiguo | Pedidos, inventario y entregas |
| Primer cambio | Sistema nuevo | Pedidos, inventario y asignación de repartidores |
| Tras comprobar el cambio | Sistema nuevo | Solo las tareas que aún no se han migrado |
| Al terminar | Sistema nuevo | Nada; se puede retirar el sistema antiguo |

## ¿Qué puede salir mal?
Durante la migración, los dos sistemas conviven. Eso puede hacer que el equipo tenga que revisar información en dos lugares. También hay que evitar que una misma tarea quede atendida por ambos sistemas de forma confusa.

Un riesgo importante aparece si el sistema nuevo muestra datos distintos de los que tiene el antiguo. Por ejemplo, el sistema de seguimiento dice “entregado”, pero el sistema de pedidos dice “en camino”. Antes de avanzar, el equipo debe decidir cuál sistema guarda el dato correcto y cómo se mantiene la información al día.

Por eso, migrar poco a poco no significa que no haya riesgos. Significa que se intenta limitar cada cambio a una parte que se pueda comprobar y, si es necesario, revertir.

## Ejercicio de autoestudio
Puedes resolver este ejercicio con palabras o un dibujo. No necesitas programar.

1. **Imagina el sistema actual:** escribe tres tareas de una plataforma logística, por ejemplo, recibir pedidos, revisar inventario y mostrar el seguimiento.
2. **Elige una tarea pequeña para cambiar primero:** explica por qué empezarías por esa y no por todas a la vez.
3. **Dibuja el recorrido:** indica quién recibe una consulta y si la atiende el sistema antiguo o el nuevo.
4. **Define cómo sabrías que funciona:** escribe dos cosas que comprobarías. Por ejemplo, que se muestra el estado correcto y que crear un pedido sigue funcionando.
5. **Decide cómo volver atrás:** explica qué harías si el sistema nuevo muestra un estado equivocado.
6. **Explica cuándo seguirías:** ¿qué evidencia necesitas antes de trasladar otra tarea?

### Ejemplo de respuesta
Una migración inicial razonable sería mover solo la consulta del estado de una entrega. Dibujaría que esa consulta va al sistema nuevo, mientras la creación de pedidos y las demás funciones continúan en el antiguo.

Antes de seguir, comprobaría que el estado del pedido sea correcto, que las otras tareas sigan funcionando y que una consulta pueda volver al sistema antiguo si el sistema nuevo falla. También aclararía cuál sistema mantiene el dato oficial para evitar que ambos muestren estados distintos.

No es la única respuesta correcta. La tarea que elijas debe poder probarse por separado y tener una manera clara de responder si el cambio falla.

## Comprueba tu comprensión
- ¿Qué tarea de la plataforma logística sería pequeña y útil para migrar primero?
- ¿Qué problema podría ocurrir si el sistema antiguo y el nuevo muestran datos distintos?
- ¿Qué tendría que funcionar antes de pasar otra tarea al sistema nuevo?
- ¿Por qué conviene mantener una forma de volver atrás?

### Respuestas para revisar
- Una tarea adecuada es una que se pueda separar y comprobar, como mostrar el seguimiento, sin migrar al mismo tiempo pedidos e inventario.
- El cliente podría recibir información contradictoria y el equipo no sabría cuál sistema refleja el dato correcto.
- La nueva tarea debe dar resultados correctos y las funciones que siguen en el sistema antiguo deben continuar operando.
- Volver atrás limita el impacto si la nueva parte falla mientras se investiga y corrige.

## Conclusión
Strangler Fig permite renovar un sistema por etapas: se elige una tarea, se pasa al sistema nuevo, se comprueba y luego se decide si continuar. Así el servicio puede seguir funcionando durante el cambio. La clave no es avanzar rápido, sino cambiar una parte manejable y saber cómo verificarla y cómo responder si falla.
