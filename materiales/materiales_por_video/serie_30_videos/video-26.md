# Video 26: Process Manager, Durable State y Event Sourcing

## Fuentes de este video
- [Qué es el patrón Process Manager](https://platzi.com/cursos/software-avanzado/que-es-el-patron-process-manager/)
- [Durable State vs Event Sourcing en sistemas](https://platzi.com/cursos/software-avanzado/durable-state-vs-event-sourcing-en-siste/)

## Navegación
[⬅️ Video anterior: Dead Letter Queue y consumidores en tiempo real](video-25.md) | [📚 Índice de la serie](README.md) | [➡️ Video siguiente: máquinas de estado y seguridad](video-27.md)

## Para estudiar por tu cuenta
Una entrega puede tardar minutos u horas y depender de varios pasos. El sistema debe recordar qué ocurrió si se reinicia y decidir qué hacer cuando una respuesta falla.

Este capítulo conecta dos preguntas: quién coordina el proceso y cómo guarda el sistema el progreso para retomarlo más tarde.

## 1. El flujo de una entrega
Para preparar el pedido 245 puede ser necesario:

1. confirmar el pedido;
2. reservar inventario;
3. asignar un repartidor;
4. informar al cliente;
5. registrar la recepción.

Cada paso puede corresponder a un servicio diferente. La comunicación puede demorarse, fallar o repetirse. Una secuencia en memoria no basta si el programa se reinicia mientras espera una respuesta.

## 2. Qué hace un Process Manager
Un **Process Manager** coordina un proceso que tiene varios pasos y decisiones. Guarda el progreso, relaciona respuestas con el pedido correcto y decide qué acción corresponde después.

No reemplaza a los servicios que participan:

- Inventario decide si puede reservar existencias.
- Entregas asigna rutas y repartidores.
- Notificaciones envía mensajes al cliente.
- Process Manager recuerda el proceso completo y coordina el orden.

Una **saga** es una forma de coordinar varios pasos que no comparten una única transacción de base de datos. Si uno no puede continuar, puede ser necesario compensar los efectos anteriores.

## 3. Estado actual persistido
El **estado** describe cómo se encuentra el proceso ahora. Una tabla podría guardar:

| Pedido | Paso actual | Resultado | Actualizado |
|---|---|---|---|
| 245 | Esperando repartidor | Inventario reservado | 13:42 |

Cuando el proceso avanza, se actualiza el registro. El sistema puede leerlo y continuar después de un reinicio.

Esto se suele llamar estado durable o persistido: el dato sigue disponible después de cerrar el programa. Persistir el estado no requiere guardar cada transición como evento principal.

## 4. Event Sourcing
**Event Sourcing** guarda como fuente principal una secuencia de hechos que ocurrieron. El estado actual se obtiene aplicando esos hechos en orden.

Para el pedido 245, los eventos pueden ser:

```text
PedidoConfirmado
ProductosReservados
RepartidorAsignado
EntregaIniciada
EntregaCompletada
```

Al leerlos en orden, el sistema reconstruye el estado actual y puede explicar cómo llegó ahí.

### No confundas historia con logs
Un log técnico ayuda a diagnosticar. En Event Sourcing, los eventos son la fuente principal del estado de negocio. Agregar logs a una aplicación que guarda el estado actual no la convierte automáticamente en Event Sourcing.

## 5. Comparación con una libreta de seguimiento
- **Estado actual:** una ficha dice “Esperando repartidor”. Se consulta rápido, pero puede no mostrar los pasos anteriores.
- **Event Sourcing:** una bitácora guarda “inventario reservado” y otros hechos. El estado se reconstruye leyendo la secuencia.

La primera forma suele ser más sencilla. La segunda puede ser útil si el negocio necesita reconstruir el historial con detalle, pero exige diseñar eventos, correcciones y consultas.

## 6. Cómo se conectan el Process Manager y el almacenamiento
El Process Manager necesita recordar el paso actual. Puede hacerlo guardando una fila actualizada cada vez que recibe una respuesta, o puede reconstruirlo desde eventos.

Una forma sencilla de empezar:

```csharp
public sealed record ProcesoEntrega(
    Guid PedidoId,
    string Estado,
    DateTimeOffset ActualizadoEn);
```

Al recibir `InventarioReservado`, el Process Manager cambia el estado a “Esperando repartidor”. Al recibir `RepartidorAsignado`, cambia a “Esperando recogida”.

El dato debe guardarse antes de responder como si el paso se hubiera completado. Relaciona cada mensaje con `PedidoId` y conserva identificadores para reconocer respuestas repetidas.

## 7. Qué pasa cuando un paso falla
Supón que Inventario reservó productos, pero Entregas no encuentra repartidor.

El Process Manager puede solicitar liberar la reserva. Esto es una **compensación**: una nueva acción que busca corregir o contrarrestar un efecto anterior. No borra que el inventario sí estuvo reservado.

Si la liberación también falla, el proceso no debe marcarse como cancelado con éxito. Se guarda “Requiere revisión” y el error para que pueda retomarse.

Cada paso debe contemplar:

- respuesta exitosa;
- respuesta negativa del negocio;
- timeout o falta de respuesta;
- respuesta duplicada;
- proceso cancelado a mitad del flujo.

## 8. ¿Qué opción elegir?
| Pregunta | Estado actual persistido | Event Sourcing |
|---|---|---|
| ¿Qué se guarda como fuente principal? | Paso y estado más reciente | Hechos que producen los cambios |
| ¿Cómo se obtiene el estado actual? | Se lee el registro | Se aplican eventos en orden |
| ¿Es sencillo ver el progreso actual? | Sí, normalmente directo | Puede requerir una proyección |
| ¿Permite reconstruir la historia? | No necesariamente | Sí, si la secuencia está completa |
| ¿Qué complejidad agrega? | Menor en flujos simples | Versionado de eventos, correcciones y proyecciones |

Para una primera versión, un estado persistido puede bastar. Event Sourcing se justifica si la historia detallada es una necesidad real de negocio, auditoría o reconstrucción.

## 9. Errores que debes evitar
- Usar Event Sourcing solo porque suena más robusto.
- Confundir el estado actual con el historial de eventos.
- Cambiar o borrar eventos antiguos sin entender a quienes dependen de ellos.
- Olvidar que respuestas y mensajes pueden repetirse.
- Marcar el proceso como terminado antes de guardar el estado.
- Tratar una compensación como si borrara una acción ya ocurrida.

## 10. Actividad de autoestudio
El pedido 245 ya reservó inventario, pero no se encuentra repartidor en el tiempo definido por el negocio.

1. Escribe qué estado debería guardar el Process Manager.
2. Decide cuál acción de compensación podría solicitar.
3. Explica qué harías si la respuesta “inventario liberado” llega dos veces.
4. ¿Guardarías solo el paso actual o cada evento? Justifica según la necesidad de la plataforma.
5. Escribe una señal que requiera revisión manual.

### Respuesta modelo
El estado puede ser “Liberando inventario” hasta recibir confirmación; después “Requiere reasignación” o “Cancelado”, según la regla acordada. Si la confirmación llega dos veces, el proceso reconoce que el pedido ya pasó ese paso y no libera ni notifica otra vez.

Para un MVP que solo necesita saber en qué paso está cada pedido, persistir el estado actual puede ser suficiente. Si soporte o auditoría necesitan reconstruir cada transición exacta, se puede evaluar Event Sourcing y aceptar su mayor complejidad.

## Comprueba lo que aprendiste
1. ¿Qué responsabilidad tiene el Process Manager?
2. ¿Qué diferencia hay entre estado persistido y Event Sourcing?
3. ¿Qué es una compensación?
4. ¿Por qué guardar el estado antes de confirmar el paso?

### Respuestas
1. Coordinar pasos y recordar el progreso del proceso.
2. El estado persistido guarda la situación más reciente; Event Sourcing conserva los hechos que producen los cambios y reconstruye la situación.
3. Una acción nueva que intenta corregir o contrarrestar un efecto anterior.
4. Para poder retomar el flujo correctamente después de un reinicio o una falla.

## Conclusión
El Process Manager coordina el proceso de entrega. El estado durable permite retomarlo; Event Sourcing conserva los hechos para reconstruirlo. Empieza con la persistencia que cubra la necesidad demostrada y aumenta complejidad solo cuando el historial completo aporte valor.