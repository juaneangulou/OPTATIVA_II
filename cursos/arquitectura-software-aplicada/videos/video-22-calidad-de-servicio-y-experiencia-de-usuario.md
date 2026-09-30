# Video 22: Patrón Comparing Consumers para procesamiento en tiempo real

## Título
Cómo comparar una versión nueva del procesamiento antes de darle control

## Resumen
La plataforma logística usa un consumidor para calcular la hora estimada de llegada. El equipo crea una versión nueva que considera tráfico, pero no quiere que un error afecte inmediatamente a los clientes.

Con el patrón **Comparing Consumers**, la versión actual y la candidata procesan las mismas entradas. La actual sigue definiendo lo que ve el usuario; la candidata calcula su resultado sin enviar avisos ni cambiar pedidos. El equipo compara precisión, rapidez, errores y costo antes de decidir si cambia.

No debe confundirse con repartir una cola entre trabajadores. Si los consumidores compiten por una cola, cada tarea suele ir a uno de ellos; para comparar, ambas versiones necesitan entradas equivalentes. Ejecutar dos versiones requiere recursos y cuidado para evitar efectos duplicados o exposición innecesaria de datos.

## Ideas principales
- El modo sombra permite observar una versión candidata sin que afecte al usuario.
- Las entradas deben ser equivalentes para que la comparación sea justa.
- Hay que comparar los casos desfavorables y no solo promedios favorables.
- El candidato no debe realizar efectos reales durante la prueba.
- La adopción debe ser gradual y permitir volver a la versión actual.

## Preguntas para comprobar tu comprensión
- ¿Qué versión mantiene el control durante la comparación?
- ¿Qué diferencia hay entre comparar consumidores y repartir una cola?
- ¿Qué impedirías que hiciera el candidato en modo sombra?
- ¿Qué evidencia pedirías antes de adoptarlo?
