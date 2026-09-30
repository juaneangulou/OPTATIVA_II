# Video 14: Strangler Fig para migrar arquitecturas limpias

## Título
Cómo reemplazar un sistema antiguo por partes, sin apagarlo todo

## Resumen
Este video presenta una manera gradual de renovar un programa que ya está en uso. En vez de apagarlo y construir otro completo de una sola vez, trasladamos una tarea pequeña al sistema nuevo, comprobamos que funciona y luego decidimos si trasladamos otra.

El nombre Strangler Fig viene de una planta que crece alrededor de un árbol y poco a poco ocupa su lugar. En una migración de software, el sistema nuevo va asumiendo tareas mientras el antiguo sigue atendiendo las que todavía no se han cambiado. Una plataforma logística podría empezar trasladando solo la consulta del estado de una entrega.

El cambio gradual ayuda a limitar el riesgo, pero significa que los dos sistemas convivirán durante un tiempo. Por eso hay que comprobar que muestran información coherente y tener una manera de volver atrás si la nueva parte falla.

## Ideas principales
- No es necesario reemplazar todo el programa en un solo cambio.
- Se puede empezar con una tarea pequeña y trasladarla al sistema nuevo.
- El sistema antiguo sigue funcionando mientras aún atiende tareas pendientes.
- Cada parte nueva debe comprobarse antes de continuar con la siguiente.
- Los dos sistemas pueden mostrar datos distintos; hay que decidir cómo evitarlo.
- Conviene saber cómo volver temporalmente al sistema antiguo si algo falla.

## Conclusión
Strangler Fig es una estrategia para cambiar un sistema por etapas. Cada etapa debe ser pequeña, comprobable y contar con una respuesta si falla. Así la organización puede seguir trabajando mientras renueva su programa.

## Preguntas para reflexión
- ¿Qué tarea pequeña cambiarías primero en la plataforma logística?
- ¿Cómo comprobarías que el sistema nuevo muestra la información correcta?
- ¿Qué harías si el sistema nuevo deja de responder?
