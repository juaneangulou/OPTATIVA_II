# Video 21: Dead Letter Queue en productor-consumidor

## Título
Qué hacer con una tarea que falla repetidamente

## Resumen
En un sistema productor-consumidor, una parte puede dejar tareas en una cola para que otra las procese. Algunas fallan por problemas temporales; otras, porque les falta información o tienen un formato incorrecto. Repetirlas sin límite puede bloquear el trabajo y consumir recursos.

Una **Dead Letter Queue** (DLQ) es una cola separada que conserva las tareas que superaron los intentos permitidos. Permite que la cola normal siga avanzando y que el equipo investigue el error. La DLQ no corrige la tarea: antes de reprocesarla hay que corregir la causa, comprobar si ya produjo algún efecto y evitar duplicados.

## Ejemplo
Si el servicio de rutas está temporalmente fuera de servicio, puede tener sentido reintentar con pausas y un límite. Si al pedido le falta la ciudad, repetirlo sin corregir la dirección no ayuda; la tarea debe apartarse para revisión.

## Ideas principales
- Distingue fallos temporales de datos que necesitan corrección.
- Define cuántas veces se reintenta y cuánto se espera entre intentos.
- Guarda el motivo del fallo y el identificador de la tarea.
- Revisa si la tarea ya tuvo efecto antes de reprocesarla.
- Protege los datos personales que pudieran llegar a la DLQ.

## Preguntas para comprobar tu comprensión
- ¿Qué diferencia hay entre un fallo temporal y una dirección incompleta?
- ¿Por qué no conviene reintentar una tarea indefinidamente?
- ¿Qué revisarías antes de devolver una tarea a la cola normal?
