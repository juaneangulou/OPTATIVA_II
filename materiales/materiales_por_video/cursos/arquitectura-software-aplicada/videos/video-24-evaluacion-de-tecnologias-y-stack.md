# Video 24: Durable State vs Event Sourcing en sistemas

## Para estudiar por tu cuenta
Un sistema necesita recordar información entre una ejecución y la siguiente. En esta clase compararás dos formas de guardar ese historial: conservar el estado actual o conservar cada hecho que lo fue cambiando.

Seguiremos una entrega logística para responder: **¿nos basta con saber cómo está ahora el pedido, o necesitamos conservar también cómo llegó a ese estado?**

## 1. La necesidad de recordar
Cuando la aplicación muestra “Entregado”, alguien debe haber guardado esa información. Si se apaga el programa, el estado no puede desaparecer.

Guardar información de manera que siga disponible después de reiniciar se llama **persistir**. La información guardada se llama **estado** cuando describe cómo se encuentra algo en un momento determinado.

Para el pedido 245, el estado actual podría ser:

```text
Pedido: 245
Estado: Entregado
Repartidor: Camila
Hora de entrega: 14:24
```

Ese registro responde rápidamente cómo está el pedido ahora. Pero, si alguien pregunta quién lo cambió de “En camino” a “Entregado”, quizá el registro actual no cuente toda la historia.

## 2. Opción A: guardar el estado actual
En una forma común de persistencia, el sistema guarda el estado actual y lo actualiza cuando hay un cambio.

1. El pedido se crea como “Pendiente”.
2. Al salir del almacén, el registro cambia a “En camino”.
3. Al llegar, cambia a “Entregado”.

Al final, la base de datos conserva el valor actual: “Entregado”. Las versiones anteriores pueden no estar disponibles, salvo que el sistema las guarde aparte.

Piensa en una pizarra: cada vez que cambia el estado, borras el texto anterior y escribes el nuevo. Es simple consultar la respuesta actual, pero no necesariamente puedes reconstruir lo que se escribió antes.

### Ventajas
- Es fácil preguntar por el estado actual.
- El modelo suele ser más sencillo de construir y mantener.
- Requiere menos almacenamiento que conservar cada cambio, según el sistema.

### Límites
- Puede ser difícil explicar la historia de cambios si no se guarda por separado.
- Un error al actualizar puede borrar información previa que era útil.
- Reconstruir cómo se tomó una decisión puede ser complicado.

## 3. Opción B: Event Sourcing
**Event Sourcing** es una forma de guardar información en la que los hechos que cambian el sistema se conservan como una secuencia de eventos. El estado actual se obtiene leyendo esa secuencia y aplicando cada hecho en orden.

Un **evento** describe algo que ya ocurrió. Para el pedido 245, la secuencia podría ser:

```text
PedidoCreado(245, 09:10)
PedidoListoParaEntrega(245, 11:30)
RepartidorAsignado(245, Camila, 12:05)
PedidoEntregado(245, 14:24)
```

El sistema lee los eventos desde el primero hasta el último:

1. `PedidoCreado`: el estado pasa a “Pendiente”.
2. `PedidoListoParaEntrega`: pasa a “Listo para entrega”.
3. `RepartidorAsignado`: pasa a “En camino” y registra a Camila.
4. `PedidoEntregado`: pasa a “Entregado” a las 14:24.

La lista de hechos es la fuente de la historia. A partir de ella, el sistema puede calcular el estado actual y también consultar cómo se llegó allí.

## 4. Comparación con dos formas de llevar un cuaderno
- **Estado actual:** mantienes una ficha que dice cómo está el pedido hoy.
- **Event Sourcing:** guardas cada cambio importante en páginas consecutivas y reconstruyes la ficha leyendo las páginas.

No se trata de que una forma sea moderna y la otra anticuada. Resuelven necesidades distintas y tienen costos diferentes.

## 5. Tabla comparativa
| Pregunta | Estado actual persistido | Event Sourcing |
|---|---|---|
| ¿Qué se guarda como fuente principal? | El estado más reciente | La secuencia de hechos que ocurrieron |
| ¿Cómo se obtiene el estado de hoy? | Se lee directamente | Se aplican los eventos en orden |
| ¿Es sencillo consultar “cómo está ahora”? | Generalmente sí | Puede requerir una vista calculada |
| ¿Se conserva la historia completa? | No necesariamente | Sí, como parte del modelo principal |
| ¿Qué complejidad agrega? | Menor en casos habituales | Orden, correcciones, lectura y mantenimiento de eventos |
| ¿Cuándo puede ser útil? | Cuando importa principalmente el estado actual | Cuando la historia completa es necesaria para auditoría o reconstrucción |

## 6. “Tenemos logs” no significa “usamos Event Sourcing”
Un **log** es un registro que ayuda a diagnosticar qué ocurrió. Una copia de seguridad guarda datos para recuperarse de un daño. Ninguna de esas cosas convierte por sí sola el sistema en Event Sourcing.

Para usar Event Sourcing, los eventos deben ser la fuente principal desde la que se reconstruye el estado del dominio. Si la aplicación guarda el estado actual como fuente principal y además anota algunos cambios para diagnóstico, está combinando un estado persistido con un historial auxiliar; eso puede ser útil, pero es otra decisión.

## 7. ¿Qué es una vista calculada?
Leer cientos o miles de eventos cada vez que alguien abre un pedido puede ser lento. Por eso, un sistema con Event Sourcing puede guardar una **vista** o **proyección**: un resumen calculado a partir de los eventos para consultar más rápido.

La vista no reemplaza la historia original. Si se pierde o queda desactualizada, se puede reconstruir leyendo los eventos de nuevo.

Ejemplo de vista actual:

```text
Pedido 245: Entregado
Repartidor: Camila
Hora: 14:24
```

## 8. ¿Qué pasa cuando un evento era incorrecto?
Los eventos describen hechos que ya se registraron. Si se publicó un evento equivocado, editar la historia como si nunca hubiera ocurrido puede borrar evidencia y confundir a otros sistemas.

Una alternativa es registrar un nuevo hecho que corrija la información. Por ejemplo: `EntregaMarcadaPorError(245)` seguido de la acción correcta. La manera de corregir depende del negocio y debe quedar clara para quien reconstruye el estado.

Event Sourcing exige pensar cómo se corregirán datos, quién puede hacerlo y cómo se interpretarán eventos antiguos. La historia no debe volverse una colección de frases cuyo significado nadie entiende.

## 9. ¿Cuál elegir para el pedido de la plataforma?
### El estado actual puede ser suficiente cuando:
- La pantalla necesita consultar principalmente el estado vigente.
- Hay pocas razones legales u operativas para reconstruir cada paso.
- El equipo necesita una solución sencilla y fácil de mantener.
- Se puede guardar por separado una auditoría breve de cambios importantes.

### Event Sourcing puede valer la pena cuando:
- Es imprescindible explicar la secuencia completa de decisiones.
- Hay auditorías que requieren saber cuándo y por quién cambió un estado.
- Se necesitan reconstruir distintas vistas a partir de los mismos hechos.
- El negocio puede definir eventos duraderos y mantener sus significados.

No conviene elegir Event Sourcing solo porque “guarda todo”. También conserva errores, necesita políticas de privacidad y eliminación, y aumenta la complejidad de consultas y correcciones.

## 10. Actividad de autoestudio
Un pedido pasó por estos cambios:

1. Fue creado a las 09:10.
2. Se canceló a las 09:20 porque el cliente cambió de opinión.
3. Se creó de nuevo a las 09:35 con otro pedido.

Responde:

- ¿Qué información mostraría una ficha que guarda solo el estado actual?
- ¿Qué información permitiría reconstruir una secuencia de eventos?
- ¿Qué preguntas podría responder el equipo con cada alternativa?
- ¿Qué costos adicionales tendría guardar todos los eventos?
- ¿Qué método elegirías para un sistema de pedidos pequeño y por qué?

### Pistas
- Distingue “cómo está ahora” de “qué ocurrió antes”.
- Un historial solo es útil si cada evento tiene significado claro.
- La decisión depende de necesidades reales de consulta, auditoría y mantenimiento.

## 11. Respuesta comentada
La ficha actual podría mostrar el estado vigente del nuevo pedido, por ejemplo “Pendiente”. Si no conserva historial, no mostraría necesariamente la cancelación anterior.

Una secuencia de eventos permitiría reconstruir que el primer pedido fue creado y cancelado, y que luego se creó otro. Esto puede servir para auditoría o para entender el comportamiento del cliente.

Para un sistema pequeño que solo necesita atender pedidos y mostrar el estado actual, guardar el estado directamente puede ser más sencillo. Si el negocio necesita una historia verificable de cada cambio, puede guardar un historial explícito o evaluar Event Sourcing, aceptando su costo de diseño y operación.

No hay una opción universal. Una respuesta completa menciona la necesidad, el dato que se debe poder consultar y el costo que se acepta.

## 12. Comprueba lo que aprendiste
1. ¿Qué guarda como fuente principal el estado actual persistido?
2. ¿Qué guarda Event Sourcing como fuente principal?
3. ¿Por qué una vista calculada puede ser útil?
4. ¿Tener un log de errores basta para afirmar que un sistema usa Event Sourcing?
5. ¿Por qué Event Sourcing no debe elegirse automáticamente?

### Respuestas
1. El estado más reciente del elemento.
2. Los eventos o hechos que causaron los cambios.
3. Permite consultar un resumen sin volver a leer todos los eventos cada vez.
4. No. El historial debe ser la fuente principal para reconstruir el estado del dominio.
5. Guarda y hace mantenible una historia completa, lo que agrega complejidad y decisiones de privacidad, corrección y consulta.

## Conclusión
Guardar el estado actual facilita responder cómo está algo ahora. Event Sourcing conserva los hechos que produjeron ese estado y permite reconstruir la historia, a cambio de mayor complejidad.

Antes de elegir, pregunta qué necesita saber el usuario y qué historia necesita conservar el negocio. Luego compara la facilidad de consulta, auditoría, corrección, privacidad y mantenimiento. La tecnología debe seguir a la necesidad, no al revés.
