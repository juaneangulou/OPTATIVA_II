# Video 13: Métricas cuantitativas para evaluar arquitecturas limpias

## Título
Cómo usar medidas sencillas para revisar la organización de un programa

## Resumen
La arquitectura es la forma en que se organizan las partes de un programa. En este video veremos cómo comprobar si esa organización ayuda a cambiar y probar el sistema, o si hace que tareas sencillas dependan de demasiadas cosas.

Una métrica es una medida que permite comparar. En este video llamamos **regla del negocio** a una condición que el sistema debe cumplir, como “no asignar una entrega a un repartidor que no está disponible”. Podemos contar cuántas conexiones directas hay entre la parte que toma esa decisión y la base de datos. Si separamos esas responsabilidades, volvemos a contar y revisamos si algo mejoró.

Los números no dan una calificación definitiva al programa. Nos ayudan a encontrar dónde mirar y a comparar antes y después. Siempre debemos comprobar que el sistema siga haciendo correctamente su trabajo.

## Ideas principales
- Una métrica es una medida útil para comparar una situación antes y después.
- Las condiciones importantes del negocio deberían poder comprobarse sin conocer los detalles de la base de datos o de una página web.
- Muchas conexiones entre partes pueden hacer que los cambios sean más difíciles.
- Un número alto es una señal para investigar, no una prueba automática de que algo está mal.
- Después de ordenar el programa, también debemos comprobar que sus resultados siguen siendo correctos.
- No existe un número mágico que garantice una buena arquitectura.

## Conclusión
Medir nos ayuda a hacer mejores preguntas sobre cómo está organizado un programa. Primero entendemos el problema, luego comparamos una medida y finalmente comprobamos que el cambio haya ayudado sin dañar el funcionamiento.

## Preguntas para reflexión
- ¿Qué parte de un programa te gustaría que fuera más fácil de cambiar?
- ¿Qué podrías contar para saber si un cambio ayudó?
- ¿Por qué un número, por sí solo, no basta para decir que un programa está bien organizado?
