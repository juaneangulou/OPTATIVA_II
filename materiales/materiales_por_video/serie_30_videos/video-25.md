# Video 25: Dead Letter Queue y consumidores en tiempo real

## Fuentes de este video
- [Dead Letter Queue en productor-consumidor](https://platzi.com/cursos/software-avanzado/dead-letter-queue-en-productor-consumido/)
- [Comparing Consumers para procesamiento en tiempo real](https://platzi.com/cursos/software-avanzado/patron-comparing-consumers-para-procesam/)

## Navegación
[⬅️ Video anterior: mensajes y productor-consumidor](video-24.md) | [📚 Índice de la serie](README.md) | [➡️ Video siguiente: Process Manager y Durable State](video-26.md)

## Para estudiar por tu cuenta
Un mensaje de entrega puede fallar al procesarse, mientras que un nuevo consumidor puede producir resultados distintos al actual. Este capítulo conecta dos necesidades diferentes: conservar fallos que requieren investigación y comparar una versión candidata antes de darle efecto real.

## 1. Recuerda productor, consumidor y cola
Pedidos puede producir un mensaje para que Entregas procese una tarea. Una **cola** conserva los mensajes pendientes; el **consumidor** los recoge y realiza el trabajo.

Un fallo no siempre significa lo mismo:

- un proveedor temporalmente fuera de servicio puede justificar un reintento;
- una dirección incompleta necesita corrección;
- un error desconocido necesita investigación.

Reintentar sin límite puede bloquear trabajo o saturar dependencias. El sistema necesita un máximo razonado, pausas y registro del motivo.

## 2. Dead Letter Queue: apartar lo que ya no debe bloquear la cola normal
Una **Dead Letter Queue (DLQ)** es una cola separada para mensajes que superaron los intentos permitidos o requieren atención.

```text
Cola normal -> consumidor -> éxito: se registra el resultado
                         -> fallos repetidos: DLQ para investigar
```

La DLQ no repara un pedido ni decide automáticamente que debe reintentarse. Conserva el mensaje y el contexto del fallo para que puedas investigar la causa.

Antes de devolver un mensaje a la cola normal, comprueba que:

1. se corrigió la causa del fallo;
2. el mensaje no produjo ya el efecto deseado;
3. repetirlo no duplicará una reserva o entrega;
4. el sistema puede soportar la cantidad de mensajes que se reprocesará.

## 3. Comparing Consumers: comparar antes de sustituir
**Comparing Consumers** ejecuta el consumidor actual y una versión candidata con entradas equivalentes. El actual sigue controlando las respuestas reales; el candidato calcula y guarda sus resultados para compararlos, sin afectar al usuario.

Este uso de la versión candidata se llama a menudo **modo sombra**. “Sombra” significa que observa el mismo flujo, pero no realiza acciones externas reales como asignar repartidores o enviar avisos.

```text
Mensaje de seguimiento ─┬─> Consumidor actual -> respuesta real
                        └─> Consumidor candidato -> resultado comparativo
```

Las dos versiones necesitan recibir los mismos datos. Si reparten los mensajes entre ellas, cada una verá pedidos distintos y la comparación dejará de ser justa.

## 4. Cómo se complementan
La plataforma quiere cambiar el consumidor que calcula una hora estimada de llegada.

1. El consumidor actual sigue respondiendo al cliente.
2. El candidato recibe una copia de la misma entrada y calcula su resultado.
3. El equipo compara precisión, demora, errores y costo.
4. Si el candidato falla al procesar un mensaje de prueba, ese fallo se registra para investigar; no afecta a la operación real.
5. Si el comportamiento es favorable, se prueba gradualmente antes de reemplazar al actual.

Una diferencia entre resultados no es automáticamente un error ni un mensaje para DLQ. Es evidencia que se analiza. La DLQ es para tareas que no se procesan correctamente; el registro de comparación guarda salidas que pueden ser distintas.

## 5. Qué comparar
Define antes de la prueba qué significa “mejor”:

- diferencia entre hora estimada y hora real;
- porcentaje de errores de cálculo;
- tiempo que tarda cada versión;
- resultado por zona y hora del día;
- recursos que consume el candidato.

Compara suficientes casos normales y excepcionales. Un promedio puede esconder que una versión nueva falla en una zona concreta.

## 6. Evita efectos duplicados
El candidato no debe enviar notificaciones, actualizar el pedido ni asignar una ruta. Si ambas versiones hacen esas acciones, podrías mandar dos mensajes al cliente o crear dos entregas.

Al publicar una nueva versión con efecto real, prepara:

- una forma de habilitarla para un grupo pequeño;
- métricas para detectar errores o demoras;
- un plan para volver a la versión anterior;
- protección para que una tarea repetida no duplique efectos.

## 7. Datos de la DLQ y cuidado operativo
Los mensajes pueden incluir identificadores, direcciones o información de cliente. Limita quién puede leerlos y conserva solo lo necesario. Define cuánto tiempo se mantienen y quién investiga los que llevan demasiado tiempo sin resolver.

Una DLQ sin revisión termina convirtiéndose en un lugar donde se olvidan tareas. Debe tener alertas, responsable y procedimiento de reproceso.

## 8. Actividad de autoestudio
El consumidor actual calcula rutas por distancia. El candidato considera también tráfico. Durante la prueba, un mensaje de una entrega de ensayo no puede procesarse porque le falta el destino.

1. ¿Qué consumidor debe seguir controlando las rutas reales durante la comparación?
2. ¿Qué datos deben recibir ambas versiones?
3. ¿Qué resultados medirías para comparar rutas?
4. ¿Qué harías con el mensaje inválido?
5. ¿Qué acciones debe tener prohibidas el candidato en modo sombra?
6. ¿Qué comprobarías antes de reprocesar el mensaje inválido?

### Respuesta modelo
El consumidor actual mantiene el control. Ambos reciben las mismas condiciones de pedido, ubicación y datos de tráfico permitidos. Compararía duración real, precisión de hora estimada, errores y resultados por zona.

El mensaje inválido se registra con el identificador y la causa, y tras los intentos permitidos va a una DLQ para corregir el destino. El candidato no debe asignar una ruta ni enviar avisos. Antes de reprocesar, se corrige el dato y se comprueba que no exista ya una asignación.

## Comprueba lo que aprendiste
1. ¿Qué diferencia hay entre una DLQ y un registro de comparación?
2. ¿Qué versión responde al cliente durante el modo sombra?
3. ¿Por qué ambas versiones necesitan entradas equivalentes?
4. ¿Qué debe ocurrir antes de reprocesar un mensaje fallido?

### Respuestas
1. La DLQ conserva mensajes que no pudieron procesarse; el registro comparativo guarda resultados para evaluar dos consumidores.
2. El consumidor actual.
3. Para atribuir las diferencias al comportamiento y no a que recibieron datos distintos.
4. Corregir la causa, comprobar si hubo efectos previos y evitar duplicados.

## Taller aplicado: operar una Dead Letter Queue
Para un mensaje `PrepararEntrega` que falló repetidamente, documenta:

1. Cuántos intentos automáticos permites y qué errores no deben reintentarse.
2. Qué campos conservas: `messageId`, tipo, causa, timestamps, número de intentos y correlación.
3. Quién recibe la alerta cuando la DLQ supera un umbral.
4. Cómo se corrige el mensaje sin editar silenciosamente la evidencia original.
5. Qué comprobación confirma que el reproceso no crea una segunda entrega.
6. Cuándo se descarta definitivamente un mensaje y cómo se conserva la razón.

Una DLQ no es un basurero ni una solución automática. Es una cola de trabajo operativo: necesita propietario, retención, métricas, procedimiento de análisis y permiso controlado para reprocesar. El modo sombra del consumidor candidato debe permanecer sin efectos externos hasta que termine la comparación.

## Conclusión
La DLQ protege el flujo normal frente a tareas que fallan repetidamente y conserva evidencia para investigarlas. Comparing Consumers permite evaluar una nueva lógica en paralelo sin que afecte a clientes. Uno maneja fallos; el otro compara comportamientos. Pueden coexistir, pero no cumplen la misma función.