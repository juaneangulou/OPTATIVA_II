# Video 19: Mensajes vs eventos en microservicios

## Para estudiar por tu cuenta
En esta clase aprenderás a distinguir dos tipos de comunicación entre partes de un sistema: una que **pide que alguien haga algo** y otra que **avisa que algo ya ocurrió**. La diferencia parece pequeña, pero ayuda a que los servicios se entiendan y no dependan de supuestos escondidos.

No necesitas programar. Seguiremos el recorrido de un pedido logístico y usaremos frases cotidianas antes de ver ejemplos de cómo se podrían nombrar los mensajes.

## 1. El problema: varios servicios necesitan coordinarse
Cuando una compra queda lista, pueden ocurrir varias cosas:

- El inventario debe reservar los productos.
- El equipo de entregas debe preparar el paquete.
- El cliente debe recibir una confirmación.
- El área de análisis debe contar la compra.

Si una sola parte llama una por una a todas las demás, conoce demasiados detalles sobre quién necesita saber qué. Si el sistema crece, cada nueva tarea obliga a modificar esa coordinación.

Una alternativa es enviar información para que otros servicios puedan actuar cuando corresponda. Para elegir bien qué enviar, primero hay que distinguir **una instrucción** de **un aviso de algo ocurrido**.

## 2. ¿Qué significa mensaje?
Un **mensaje** es información que una parte de un programa envía a otra. Es como dejar una nota para comunicar una pregunta, una instrucción o un hecho.

“Mensaje” es el término general. Dentro de esa categoría, la intención puede ser diferente:

- Puede pedir a alguien que haga algo.
- Puede informar que algo ya pasó.

La frase escrita y el contexto permiten reconocer la intención. El nombre importa porque quien recibe el mensaje necesita saber si debe actuar o solo enterarse.

## 3. Una instrucción: “Reserva estos productos”
Una **instrucción** (a menudo llamada comando) pide que un destinatario haga algo.

Ejemplo: “Inventario, reserva dos cajas del producto A para el pedido 245”.

Esta frase:

- Está dirigida al servicio de inventario.
- Pide una acción que todavía falta realizar.
- Puede ser aceptada o rechazada, por ejemplo, si no hay existencias.
- Necesita que alguien responsable intente cumplirla.

Una instrucción suele usar un verbo de acción: reservar, cancelar, asignar, enviar o actualizar.

## 4. Un evento: “El pedido fue confirmado”
Un **evento** comunica un hecho que ya ocurrió y que puede interesar a otras partes.

Ejemplo: “El pedido 245 fue confirmado”.

Esta frase:

- Describe algo que ya pasó.
- No le ordena al inventario que reserve productos.
- Puede ser útil para inventario, entregas, notificaciones o análisis.
- Permite que cada parte interesada decida qué acción le corresponde.

Un evento suele nombrarse como un hecho en pasado: pedido confirmado, pago recibido, entrega completada.

## 5. Una comparación con la vida diaria
Imagina que una persona dice: “Por favor, abre la puerta”. Está pidiendo una acción: es una instrucción.

Después dice: “La puerta ya está abierta”. Está comunicando un hecho: es un evento.

La diferencia importa. Si escuchas la primera frase, debes decidir si puedes abrir la puerta. Si escuchas la segunda, no debes volver a abrirla; solo sabes que ya ocurrió.

## 6. El recorrido del pedido 245
Veamos una secuencia completa:

### Paso 1: el pedido se confirma
El servicio de Pedidos verifica sus condiciones y cambia el estado del pedido 245 a “confirmado”. Esta parte es responsable de saber que la confirmación ocurrió.

### Paso 2: se comunica el hecho
Pedidos publica un evento: “Pedido 245 confirmado”, junto con los datos acordados que otros servicios necesitan.

**Publicar** significa dejar el aviso disponible para que los servicios interesados puedan recibirlo. No significa que Pedidos llame y espere a que todos terminen su trabajo.

### Paso 3: otras partes reaccionan
- Inventario escucha el evento y decide iniciar la reserva de productos.
- Entregas escucha el evento y crea una preparación logística si las reglas lo permiten.
- Notificaciones escucha el evento y prepara un mensaje para el cliente.

En un sistema real, cada servicio debe comprobar sus propias condiciones. Haber recibido el evento no significa que toda acción posterior vaya a tener éxito.

### Paso 4: una parte puede necesitar una instrucción
Inventario podría enviar una instrucción concreta a otro componente: “Reserva dos unidades del producto A para el pedido 245”. Esa solicitud espera una acción, no anuncia que la reserva ya ocurrió.

### Paso 5: se comunica el resultado
Si la reserva tiene éxito, Inventario puede publicar otro evento: “Productos reservados para el pedido 245”. Si no hay unidades, comunica el resultado según el diseño del sistema.

## 7. Tabla para reconocer la intención
| Mensaje | ¿Pide una acción o cuenta un hecho? | Tipo | Por qué |
|---|---|---|---|
| “Reserva dos unidades para el pedido 245” | Pide una acción | Instrucción | El inventario todavía debe intentar reservarlas |
| “El pedido 245 fue confirmado” | Cuenta un hecho | Evento | La confirmación ya ocurrió |
| “Cancela la entrega 245” | Pide una acción | Instrucción | Alguien debe intentar cancelar la entrega |
| “La entrega 245 fue cancelada” | Cuenta un hecho | Evento | La cancelación se completó |
| “Envía un aviso al cliente” | Pide una acción | Instrucción | Notificaciones debe intentar enviarlo |
| “El aviso al cliente fue enviado” | Cuenta un hecho | Evento | El envío ya ocurrió |

Una pregunta útil es: **¿la frase quiere que algo ocurra o informa que ya ocurrió?**

## 8. Entonces, ¿todos los eventos son mensajes?
En la práctica, un evento suele viajar dentro de un mensaje. “Mensaje” habla de la comunicación que se envía; “evento” habla de la intención y el significado de esa comunicación.

Por eso no son necesariamente dos tecnologías opuestas. Un equipo puede usar el mismo sistema de transporte para enviar tanto instrucciones como eventos, pero debe nombrarlos y tratarlos según lo que significan.

La diferencia no es “un evento usa una herramienta y un mensaje otra”. La diferencia principal es si pedimos una acción o comunicamos un hecho ocurrido.

## 9. Instrucción dirigida y evento compartido
Una instrucción normalmente tiene un destinatario claro: “Inventario, reserva estos productos”. Si nadie responde, quien la envió puede necesitar conocer el resultado.

Un evento puede interesar a varios servicios. “Pedido confirmado” podría interesar a Inventario, Entregas y Notificaciones. El servicio de Pedidos no necesita conocer todos los detalles internos de cada reacción.

Esto puede reducir dependencias directas, pero crea otras responsabilidades:

- Los consumidores deben saber qué significa el evento.
- El productor debe evitar publicar un hecho que no ocurrió.
- El equipo debe decidir cómo manejar mensajes repetidos o retrasados.
- Los servicios no deben asumir que todos recibirán el aviso exactamente en el mismo instante.

## 10. ¿Qué pasa si un evento llega dos veces?
Supongamos que Inventario recibe dos veces “Pedido 245 confirmado”. Si reserva dos cajas cada vez, el cliente podría quedarse sin existencias por una reserva duplicada.

El consumidor debe reconocer que ya procesó ese pedido o ese evento y evitar repetir una acción que no debe duplicarse. Esta propiedad se conoce a veces como **idempotencia**: recibir la misma instrucción otra vez no produce un efecto adicional no deseado.

No hace falta memorizar la palabra para esta clase. Recuerda el problema: en sistemas distribuidos, una comunicación puede repetirse, así que el receptor debe protegerse contra efectos duplicados cuando una repetición sea dañina.

## 11. Qué información incluir
Un evento útil no es una frase ambigua como “algo cambió”. Debe identificar el hecho y aportar contexto suficiente para que un servicio interesado sepa si le corresponde reaccionar.

Ejemplo de información que podría acompañar “Pedido 245 confirmado”:

| Dato | Para qué sirve |
|---|---|
| Identificador del pedido | Saber a qué pedido se refiere |
| Momento de confirmación | Comprender cuándo ocurrió |
| Productos y cantidades | Permitir que Inventario identifique qué debe revisar |
| Versión del formato | Reconocer qué estructura de información se está usando |

No todos los consumidores necesitan todos esos datos. El equipo comparte lo necesario y evita incluir información personal que no hace falta.

## 12. Errores comunes

### Llamar evento a una instrucción
“Reserva los productos” no describe algo ocurrido. Es una solicitud dirigida a Inventario. Nombrarla “Productos reservados” sería engañoso porque la reserva todavía no existe.

### Publicar un hecho antes de que ocurra
Si Pedidos anuncia “Pedido confirmado” antes de guardar la confirmación, otros servicios podrían actuar sobre una compra que luego no se considera válida.

### Convertir los eventos en órdenes disfrazadas
“Evento: Notificaciones, envía un correo ahora” sigue siendo una instrucción para un destinatario. Un evento describiría algo que ya pasó, como “Pedido confirmado”.

### Pensar que publicar un evento garantiza que todo terminó
El aviso permite que otros servicios reaccionen; no garantiza que todos lo recibieran o terminaran su trabajo. Cada acción tiene su propio resultado.

### Usar eventos cuando hace falta una respuesta inmediata
Si la pantalla debe saber ahora mismo si un pago fue aceptado, una comunicación que solo avisa más tarde puede no servir. Hay que elegir el tipo de interacción según la necesidad del usuario.

## 13. Actividad de autoestudio: clasifica los mensajes
Para cada frase, escribe “instrucción” o “evento” y explica qué palabra te ayudó a decidir:

1. “Asigna un repartidor al pedido 245”.
2. “El pedido 245 quedó listo para preparar”.
3. “Envía al cliente la hora estimada de llegada”.
4. “La hora estimada de llegada fue actualizada”.
5. “Reserva tres unidades del producto B”.
6. “Tres unidades del producto B fueron reservadas”.

Después responde: ¿qué servicio debería recibir cada instrucción? ¿Qué otros servicios podrían interesarse por cada evento?

## 14. Respuesta comentada
1. **Instrucción:** pide que alguien asigne un repartidor. La podría recibir el servicio responsable de asignaciones.
2. **Evento:** comunica que el pedido ya quedó listo. Entregas y Notificaciones podrían interesarse.
3. **Instrucción:** pide que Notificaciones envíe un aviso.
4. **Evento:** informa que la actualización ya ocurrió. La aplicación y el análisis podrían usar el hecho.
5. **Instrucción:** pide una reserva. La recibe Inventario.
6. **Evento:** informa que la reserva se completó. Entregas podría seguir con la preparación.

La señal más útil suele ser el verbo: “asigna”, “envía” y “reserva” piden acciones; “quedó listo”, “fue actualizada” y “fueron reservadas” describen hechos terminados. Si la frase es ambigua, debe reescribirse.

## 15. Comprueba lo que aprendiste
Antes de continuar, intenta explicar estas ideas sin mirar el texto:

1. ¿Cuál es la diferencia entre una instrucción y un evento?
2. ¿Por qué “Pedido confirmado” puede interesar a varios servicios?
3. ¿Qué riesgo habría si un consumidor procesa dos veces una reserva?
4. ¿Por qué un evento no garantiza que todos los servicios terminaron su trabajo?
5. ¿Qué comunicación conviene si una pantalla necesita una respuesta inmediata?

### Respuestas para revisar
1. Una instrucción pide una acción; un evento comunica que un hecho ya ocurrió.
2. Inventario, Entregas y Notificaciones podrían tener una tarea que iniciar después de la confirmación.
3. Podría reservarse dos veces la misma cantidad; el consumidor debe evitar un efecto duplicado dañino.
4. El aviso se envía, pero cada servicio puede procesarlo más tarde, fallar o no completar su tarea.
5. Una interacción que devuelva el resultado de manera inmediata puede ser más adecuada; no se debe usar una notificación eventual si el usuario necesita decidir ahora.

## Conclusión
“Mensaje” es una forma general de transportar información entre partes. Una instrucción pide que un destinatario haga algo; un evento informa de un hecho que ya ocurrió y puede interesar a varios servicios.

Nombrar bien la intención ayuda a asignar responsabilidades: no anunciamos como hecho una acción que aún no se completó y no asumimos que todos los servicios reaccionaron solo porque se publicó un evento.

En el siguiente video veremos cómo se producen y consumen estas tareas y cómo se distribuyen entre varios destinos.
