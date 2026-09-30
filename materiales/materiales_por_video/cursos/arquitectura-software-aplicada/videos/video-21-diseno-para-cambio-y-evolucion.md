# Video 21: Dead Letter Queue en productor-consumidor

## Para estudiar por tu cuenta
En los videos anteriores viste que una parte puede dejar una tarea en una cola para que otra la procese después. Ahora vamos a responder una pregunta inevitable: **¿qué hacemos cuando una tarea falla una y otra vez?**

Aprenderás qué es una Dead Letter Queue, por qué una tarea no debe desaparecer ni bloquear todo el trabajo, y cómo decidir si se reintenta, se revisa o se vuelve a procesar.

## 1. Recordemos el recorrido normal
En una plataforma logística, Pedidos deja una tarea para que Entregas prepare un envío:

```text
Pedidos ──> Cola de entregas ──> Entregas procesa la tarea
```

La **cola** conserva tareas pendientes. El **consumidor** las recoge y realiza el trabajo. Si todo funciona, Entregas confirma que el paquete fue preparado y la tarea termina.

Pero a veces la tarea falla: el servicio puede estar temporalmente apagado, faltar información o contener un dato que nadie puede interpretar.

## 2. No todos los fallos son iguales
Antes de volver a intentar, conviene entender qué tipo de problema ocurrió:

- **Fallo temporal:** el servicio está ocupado o una conexión se interrumpió. Puede funcionar si se intenta más tarde.
- **Fallo permanente o de datos:** el pedido no tiene dirección o trae un formato que el sistema no reconoce. Repetir exactamente lo mismo probablemente volverá a fallar.
- **Fallo desconocido:** todavía no sabemos por qué ocurrió. Se necesita conservar información para investigarlo.

Un **reintento** es volver a ejecutar una tarea que falló. Reintentar puede ayudar ante un problema temporal, pero repetir sin límite puede saturar el sistema o esconder un error que necesita intervención.

## 3. ¿Qué es una Dead Letter Queue?
Una **Dead Letter Queue** (DLQ), o cola de mensajes fallidos, es un lugar separado al que se envían tareas que no pudieron procesarse correctamente después de los intentos permitidos.

Piensa en una bandeja de excepciones en un centro de distribución. Los paquetes que no pueden seguir el recorrido normal se guardan con la información necesaria para revisar qué pasó; no se tiran ni se dejan atravesados en la fila principal.

```text
Cola normal ──> Consumidor ──> Éxito: tarea completada
					│
					└── Falló varios intentos ──> Cola de fallidos (DLQ)
```

La DLQ no arregla el pedido ni averigua sola la causa. Su función es apartar la tarea fallida, conservarla para diagnóstico y evitar que bloquee el flujo normal.

## 4. Ejemplo paso a paso: una dirección incompleta
El pedido 245 llega a la cola de entregas sin número de casa.

### Intento 1
Entregas intenta preparar la ruta, pero no puede identificar el destino. Registra el error. Repetir inmediatamente no agregará el número que falta.

### Intentos posteriores
El sistema puede volver a probar según una política. Una **política de reintentos** indica cuántas veces se permite intentarlo y cuánto se espera entre intentos. Los límites concretos dependen del sistema; no hay un número universal.

### Se alcanza el límite
Si sigue fallando, el sistema mueve o copia la tarea a la DLQ y deja un registro del motivo. La cola normal continúa con otros pedidos.

### Se investiga y corrige
Una persona autorizada revisa que la dirección esté incompleta. El equipo contacta al cliente o corrige el dato usando una fuente confiable.

### Se procesa de nuevo con cuidado
Cuando el dato está corregido, el equipo puede volver a colocar la tarea en la cola normal. Esto se llama **reprocesar** o **redrive**. Antes, confirma que no se haya creado ya una entrega para ese pedido.

## 5. ¿Cuándo reintentar y cuándo enviar a la DLQ?
| Lo que ocurrió | Acción que podría tener sentido | Por qué |
|---|---|---|
| El servicio de rutas no responde por unos segundos | Esperar y reintentar dentro de un límite | La causa podría desaparecer sin cambiar la tarea |
| El pedido no tiene dirección | Apartar para corregir el dato | Repetir la misma tarea no completará la dirección |
| El mensaje contiene un formato inesperado | Registrar el problema y enviar a revisión | Requiere entender y posiblemente corregir el formato |
| No se conoce la causa | Reintentar de forma limitada y conservar el error | Evita un ciclo infinito y mantiene evidencia para investigar |

Un reintento automático no reemplaza entender el error. Para problemas temporales se suele aumentar la espera entre intentos, evitando que el consumidor golpee un servicio caído muchas veces seguidas.

## 6. Qué información guardar para investigar
Una tarea fallida debe conservar contexto suficiente para que alguien pueda entenderla:

- Identificador del pedido o de la tarea.
- Tipo de tarea y momento en que se creó.
- Número de intentos realizados.
- Error recibido, sin guardar secretos innecesarios.
- Servicio que intentó procesarla.
- Momento del último intento.

La DLQ puede contener direcciones y datos personales. Debe tener acceso limitado, protección adecuada y una política para eliminar datos cuando ya no sean necesarios.

## 7. Reprocesar no significa “darle clic a repetir”
Antes de reprocesar una tarea, comprueba:

1. **¿Se corrigió la causa?** Si la dirección sigue incompleta, volverá a fallar.
2. **¿La tarea ya tuvo efecto?** Quizá el envío se creó pero falló la confirmación.
3. **¿Se puede repetir sin duplicar?** Si el sistema puede crear dos entregas, necesita reconocer que ambas tareas corresponden al mismo pedido.
4. **¿Qué volumen se reprocesará?** Devolver miles de tareas al mismo tiempo puede saturar el servicio.
5. **¿Qué resultado se comprobará?** Hay que verificar que el trabajo termine, no solo que salió de la DLQ.

La **idempotencia** es la capacidad de recibir la misma tarea más de una vez sin repetir efectos no deseados. Por ejemplo, procesar dos veces “crear entrega para el pedido 245” debería dejar una entrega, no dos.

## 8. Errores frecuentes
- **Reintentar para siempre:** una tarea inválida consume recursos indefinidamente.
- **Usar la DLQ como basurero:** si nadie la revisa, se pierden tareas importantes sin resolver.
- **Reprocesar antes de corregir:** la misma causa produce el mismo fallo.
- **Reprocesar todo de golpe:** el servicio puede recibir más trabajo del que soporta.
- **Ignorar duplicados:** la tarea puede haberse completado aunque la respuesta se haya perdido.
- **Guardar datos privados sin protección:** una cola de fallidos también puede exponer información sensible.

## 9. Actividad de autoestudio
La cola de entregas recibe estas tareas:

1. Pedido A: el servicio de rutas estuvo fuera de servicio por un minuto.
2. Pedido B: la dirección no incluye ciudad.
3. Pedido C: el consumidor dejó de funcionar y volvió a iniciar.

Para cada caso escribe:

- ¿Intentarías de nuevo? ¿Por qué?
- ¿Cuándo enviarías la tarea a una DLQ?
- ¿Qué información guardarías para investigarla?
- ¿Qué comprobarías antes de reprocesarla?

### Pistas
- Pregúntate si repetir la misma tarea puede cambiar el resultado.
- Distingue una falla temporal de un dato incompleto.
- No supongas que una respuesta perdida significa que la tarea no produjo ningún efecto.

## 10. Solución comentada
- **Pedido A:** sí, permitiría un número limitado de reintentos con pausas. Si el servicio sigue sin responder, enviaría la tarea a la DLQ y revisaría la disponibilidad antes de reprocesar.
- **Pedido B:** no repetiría sin cambios. Enviaría la tarea a revisión para corregir la dirección, guardando el identificador y el motivo sin exponer más datos de los necesarios.
- **Pedido C:** primero comprobaría si la tarea ya se completó. Si no hay evidencia de éxito, permitiría un reintento; el consumidor debe protegerse contra duplicar efectos.

Las respuestas pueden variar según el costo y el riesgo del negocio. Una entrega duplicada puede ser más grave que una demora, así que la política debe expresar qué se protege.

## 11. Comprueba lo que aprendiste
1. ¿Qué problema resuelve una DLQ?
2. ¿Por qué no conviene reintentar una dirección incompleta sin corregirla?
3. ¿Qué se debe revisar antes de devolver una tarea a la cola normal?
4. ¿La DLQ corrige automáticamente una tarea? Explica.

### Respuestas
1. Aparta tareas que fallaron repetidamente para que el flujo normal avance y el equipo pueda investigarlas.
2. La causa sigue siendo la misma; repetir no agrega la información que falta.
3. Que la causa se corrigió, que la tarea no haya tenido efecto ya y que reprocesarla no duplique acciones.
4. No. Conserva la tarea y evidencia del fallo; una persona o proceso debe corregir la causa y decidir si reprocesar.

## Conclusión
Una DLQ permite tratar con cuidado las tareas que no pueden continuar por el flujo normal. Una buena estrategia combina reintentos limitados para fallos temporales, registro útil del error, revisión de tareas fallidas y reprocesamiento controlado.

La pregunta importante no es solo “¿cómo reintento?”, sino también: “¿qué pasó, qué efecto tuvo, cómo evito duplicarlo y cómo confirmo que ya quedó resuelto?”.
