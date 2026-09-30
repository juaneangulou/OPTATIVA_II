# Video 25: Máquinas de estado finito en el front-end

## Título
Cómo representar las situaciones posibles de una pantalla

## Resumen
Una pantalla que consulta una entrega puede estar esperando, mostrando un resultado, indicando que el pedido no existe o avisando de un error. Una **máquina de estado finito** representa estas situaciones con estados definidos y describe qué evento permite pasar de uno a otro.

Por ejemplo, tocar “Consultar” lleva la interfaz de “Sin consulta” a “Cargando”. Solo cuando llega una respuesta válida puede pasar a “Resultado disponible”. Esto evita mostrar a la vez estados incompatibles, como un resultado exitoso y un error.

El estado de la interfaz no es lo mismo que el estado real del pedido: la pantalla puede estar “Cargando” mientras el pedido está “En camino”. La interfaz presenta el resultado; el sistema responsable confirma qué ocurrió.

## Ideas principales
- Un estado describe la situación actual de la interfaz.
- Un evento es algo que ocurre y puede cambiar ese estado.
- Una transición define el paso permitido entre dos estados.
- Las transiciones ayudan a impedir resultados y acciones incoherentes.
- Una falla de comunicación no demuestra que la acción no llegó al servidor.
- El patrón es útil cuando el flujo tiene varias situaciones; no hace falta forzarlo en una pantalla simple.

## Preguntas para comprobar tu comprensión
- ¿Qué diferencia hay entre “Cargando” y “En camino”?
- ¿Qué evento permite mostrar un resultado confirmado?
- ¿Por qué no se muestra “Cancelada” apenas se toca el botón?
- ¿Qué combinaciones confusas ayudan a prevenir los estados explícitos?
