# Video 17: Bounded context y context maps en microservicios

## Para estudiar por tu cuenta
En esta guía descubrirás cómo dividir un sistema según el significado de las palabras y las responsabilidades del negocio, no solo según las pantallas o las herramientas. Al final podrás explicar qué es un **bounded context** (límite de contexto), leer un **context map** (mapa de contextos) sencillo y dibujar uno para una plataforma logística.

No necesitas conocer Domain-Driven Design ni saber programar. Primero entenderemos un problema cotidiano y luego le pondremos nombre a las ideas.

## 1. El problema: una misma palabra puede significar cosas distintas
En una empresa de entregas, todos hablan de “pedido”. Pero no todas las personas usan esa palabra para referirse exactamente a lo mismo:

- Para atención al cliente, el pedido es una compra: quién la hizo, cuánto cuesta y si fue pagada.
- Para el equipo de reparto, el pedido es un trabajo de entrega: dónde recogerlo, dónde llevarlo y quién lo transporta.

Imagina que una pantalla de reparto usa por error el estado “pagado” como si significara “listo para entregar”. El pago confirma una cosa; la preparación física del paquete confirma otra. Si ambos significados se mezclan, la aplicación podría enviar un repartidor por un paquete que todavía no existe en el almacén.

El problema no se resuelve obligando a toda la empresa a usar una sola palabra. Se resuelve acordando qué significa cada concepto en cada parte del trabajo y cómo se comparte la información entre ellas.

## 2. Palabras necesarias para comprender el tema
- **Dominio:** el área de trabajo que el sistema ayuda a resolver. En nuestro ejemplo, logística incluye pedidos, inventario y entregas.
- **Contexto:** la situación y las reglas que dan significado a una palabra o dato.
- **Modelo:** la representación que una parte del sistema usa para hablar de su trabajo. Por ejemplo, la lista de datos que describe una compra.
- **Límite de contexto (bounded context):** una frontera dentro de la cual los términos y las reglas tienen un significado acordado. Dentro de ese límite, el equipo puede usar un modelo coherente.
- **Mapa de contextos (context map):** un dibujo que muestra qué contextos existen, qué información intercambian y qué relación tienen.
- **Contrato:** el acuerdo sobre qué información se comparte y qué significa. Puede ser una conversación documentada, una tabla o una definición técnica.

La palabra inglesa **bounded** significa delimitado, y **context** significa contexto. El límite no tiene que ser una pared física ni un servidor distinto: puede ser una frontera entre módulos dentro de un mismo programa.

## 3. Un ejemplo sencillo fuera del software
La palabra “reserva” puede significar cosas distintas en un hotel y en una aerolínea. El hotel necesita saber qué habitación se asignó y durante qué noches. La aerolínea necesita saber qué asiento se asignó en qué vuelo.

Ambos hablan de una reserva, pero no tienen las mismas reglas ni los mismos datos. Si una aplicación intentara convertir todas las reservas en una ficha universal con los mismos campos, probablemente tendría muchos campos vacíos y reglas confusas.

En software hacemos algo parecido: permitimos que cada área use un modelo adecuado para su trabajo y definimos cómo se traduce o comparte la información con otras áreas.

## 4. Delimitamos dos contextos logísticos
Para el ejemplo, usaremos dos contextos. Sus nombres describen las responsabilidades, no necesariamente microservicios:

### Contexto de Compras y Pedidos
Su trabajo es registrar la compra y responder preguntas como:

- ¿Quién hizo el pedido?
- ¿Qué productos compró?
- ¿Se confirmó el pago?
- ¿El pedido fue cancelado?

Dentro de este contexto, “pedido confirmado” significa que la compra quedó aceptada según las reglas comerciales.

### Contexto de Entregas
Su trabajo es organizar el traslado físico y responder preguntas como:

- ¿El paquete está preparado para recoger?
- ¿Qué repartidor lo llevará?
- ¿En qué etapa está la entrega?
- ¿Cuándo se registró la última ubicación?

Dentro de este contexto, “entrega asignada” significa que existe un repartidor responsable. No significa que el pedido esté pagado ni que haya llegado al cliente.

## 5. Un pequeño glosario para evitar confusiones
| Palabra | En Compras y Pedidos | En Entregas |
|---|---|---|
| Pedido | Compra realizada por un cliente | Trabajo que debe preparar el almacén para enviarlo |
| Confirmado | La compra fue aceptada | La entrega recibió la información necesaria para empezar |
| Cancelado | La compra dejó de estar activa | La entrega debe detenerse si aún puede detenerse |
| Completado | La compra terminó según el proceso comercial | El cliente recibió el paquete y existe evidencia de entrega |

La tabla no dice que toda organización deba usar estas mismas palabras. Muestra por qué el equipo debe escribir sus propios significados y no suponer que todo el mundo entiende lo mismo.

## 6. ¿Qué pertenece al límite y qué no?
Un límite de contexto es útil cuando las reglas, los datos y las palabras dentro de una parte se entienden de forma consistente. Si otra parte necesita esa información, se acuerda qué dato recibe y qué significa.

Por ejemplo, Entregas no necesita conocer el costo promocional que pagó el cliente para asignar un repartidor. Sí necesita una dirección de entrega y una señal confiable de que la compra puede pasar al proceso logístico.

Separar contextos **no** significa duplicar todo. Significa compartir solo lo necesario para que cada parte cumpla su responsabilidad sin depender de detalles que no le corresponden.

## 7. ¿Qué es un context map?
Un context map es un mapa de esas fronteras y de las relaciones entre ellas. No es un mapa geográfico ni una lista de servidores. Ayuda a responder tres preguntas:

1. ¿Qué contextos reconocemos?
2. ¿Qué información necesita cada contexto de los demás?
3. ¿Quién define el significado de la información compartida?

Un primer dibujo del caso podría ser:

```text
┌────────────────────────────┐
│ Compras y Pedidos          │
│ Compra, cliente y pago     │
└──────────────┬─────────────┘
			   │ Pedido listo para logística
			   │ ID, dirección y productos
			   v
┌────────────────────────────┐
│ Entregas                   │
│ Preparación, ruta y entrega│
└────────────────────────────┘
```

La flecha no significa “copiar toda la base de datos”. Significa que Compras y Pedidos comparte una información acordada para que Entregas pueda iniciar su trabajo.

## 8. El recorrido paso a paso
Sigamos un pedido real, el número 245:

1. **Se realiza la compra.** Compras y Pedidos registra productos, cliente y dirección.
2. **Se confirma la compra.** El contexto de Pedidos verifica sus propias condiciones. La palabra “confirmado” tiene un significado específico allí.
3. **Se prepara la entrega.** Cuando corresponde, se comparte con Entregas el identificador del pedido, la dirección y los productos que deben prepararse.
4. **Entregas crea su propio registro.** Guarda el estado logístico, como “pendiente de asignación”. No necesita copiar el precio ni el método de pago.
5. **La entrega avanza.** Entregas registra “asignada”, “en camino” o “entregada” según sus reglas.
6. **Se comparte el resultado necesario.** Cuando existe evidencia de entrega, el contexto de Pedidos puede actualizar la vista que utiliza atención al cliente.

Cada contexto conserva las decisiones que conoce. El sistema comparte hechos necesarios, no una copia confusa de todas las reglas.

## 9. El contrato entre los contextos
Antes de conectar dos contextos, necesitamos un contrato: una explicación compartida de los datos que se envían y su significado.

| Dato que se comparte | Qué significa | Qué no significa |
|---|---|---|
| `pedido_id` | Identificador de la compra que debe prepararse | No contiene todas las reglas de compra |
| `direccion_entrega` | Lugar al que debe llevarse el paquete | No indica que el cliente haya pagado |
| `productos` | Artículos que deben prepararse | No incluye necesariamente precios o descuentos |
| `pedido_listo_para_logistica` | Compras considera que puede iniciar la preparación logística | No significa que ya exista un repartidor asignado |

Los nombres técnicos pueden variar. La parte esencial es que dos equipos puedan contestar lo mismo cuando pregunten: “¿Qué significa este dato y quién es responsable de él?”.

## 10. ¿Cuándo dos áreas deberían ser contextos distintos?
No se separa un contexto por cada pantalla, tabla o palabra. Conviene estudiar un límite cuando:

- Un mismo término tiene significados distintos y causa errores.
- Las reglas de dos áreas cambian por motivos diferentes.
- Cada área necesita decidir y trabajar sin pedir permiso constantemente a la otra.
- Los cambios de una parte rompen con frecuencia la otra.
- El equipo no puede explicar con claridad quién es responsable de un dato.

En cambio, si dos partes usan las mismas reglas y siempre cambian juntas, dividirlas puede añadir traducciones y coordinación sin beneficio.

## 11. Un bounded context no obliga a usar microservicios
Podemos dibujar límites de contexto aunque todo el programa se ejecute como una sola aplicación. Por ejemplo, el código puede tener módulos separados de Pedidos y Entregas, con reglas claras sobre qué información comparten.

Un **microservicio** es una forma de desplegar y operar una parte del sistema de manera separada. Crear un microservicio agrega trabajo: comunicación por red, despliegues, monitoreo y atención a fallas. Primero podemos aclarar el límite del negocio; después decidimos si existe una razón para desplegarlo aparte.

Una buena secuencia es:

1. Entender el negocio y sus reglas.
2. Dibujar los límites de contexto.
3. Definir qué datos se comparten y quién los mantiene.
4. Decidir si un módulo dentro de una aplicación basta o si se necesita un servicio separado.

## 12. Errores habituales

### Crear un modelo universal para todo
**Problema:** todas las áreas reciben campos que no necesitan y reutilizan palabras con sentidos distintos.

**Mejor pregunta:** ¿qué información necesita esta área para realizar su trabajo?

### Crear un servicio por cada sustantivo
**Problema:** aparecen muchas partes que necesitan coordinarse y mantener acuerdos, aunque no exista una necesidad de cambio independiente.

**Mejor pregunta:** ¿esta responsabilidad tiene reglas propias y una razón para cambiar por separado?

### Compartir una base de datos y asumir que ya existe un contrato
**Problema:** dos áreas modifican la misma información con supuestos distintos. El cambio de una puede romper a la otra.

**Mejor pregunta:** ¿quién es dueño del dato y qué significa para quien lo consume?

### Dividir los contextos y no explicar sus relaciones
**Problema:** el dibujo muestra cajas, pero nadie sabe qué información cruza entre ellas ni quién resuelve los conflictos.

**Mejor pregunta:** ¿qué viaje hace cada dato y quién confirma su significado?

## 13. Actividad de autoestudio: dibuja el mapa de contexto
Puedes resolverla con papel o en un documento. No necesitas programar.

### Situación
En una plataforma logística, Compras registra qué adquirió el cliente. Entregas organiza la preparación y el traslado. Atención al cliente responde preguntas sobre la compra y sobre la llegada.

### Paso 1: clasifica la información
Coloca cada dato en el contexto que debería definirlo:

- Precio pagado
- Dirección de entrega
- Repartidor asignado
- Estado del pago
- Hora de la última ubicación
- Evidencia de que el paquete fue recibido

### Paso 2: dibuja el mapa
Dibuja un recuadro por contexto. Escribe dentro qué responsabilidad tiene y dibuja flechas solo cuando un contexto necesite información de otro.

### Paso 3: define una flecha
Para cada flecha, completa estas frases:

- “El contexto ___ comparte ___ con ___”.
- “Ese dato significa ___”.
- “El contexto responsable de mantenerlo es ___”.

### Paso 4: comprueba el límite
Responde:

- ¿Compras necesita saber qué repartidor fue asignado?
- ¿Entregas necesita conocer el precio promocional?
- ¿Quién puede afirmar que el paquete fue recibido?
- ¿Qué error ocurriría si “pedido confirmado” se entiende como “entrega completada”?

## 14. Solución modelo, explicada
Una distribución posible sería:

| Dato | Contexto responsable | Razón |
|---|---|---|
| Precio pagado | Compras y Pedidos | Describe la operación comercial |
| Dirección de entrega | Compras y Pedidos; se comparte con Entregas | Se captura al comprar y Entregas la necesita para realizar el traslado |
| Estado del pago | Compras y Pedidos | Entregas no decide si se cobró correctamente |
| Repartidor asignado | Entregas | Describe quién realiza el trabajo logístico |
| Hora de última ubicación | Entregas | Proviene del seguimiento de la ruta |
| Evidencia de recepción | Entregas | La registra quien confirma que el paquete se entregó |

Compras comparte con Entregas el identificador, la dirección y los productos cuando el pedido está listo para preparación. Entregas puede devolver un resultado de entrega confirmado. El precio promocional no cruza porque no ayuda a preparar ni transportar el paquete.

Una respuesta equivocada sería poner toda la información en un único “Pedido universal” porque parece más fácil compartir una sola ficha. Eso vuelve menos claro quién puede cambiar cada dato y qué significa cada estado.

No existe una única división correcta para todas las empresas. La respuesta debe respetar las reglas reales de la organización y mostrar quién es responsable de cada dato.

## 15. Comprueba lo que aprendiste
Intenta responder sin mirar la guía y luego compara:

1. ¿Qué es un bounded context con tus propias palabras?
2. ¿Para qué sirve un context map?
3. ¿Los límites de contexto obligan a separar el sistema en microservicios?
4. ¿Por qué “pedido confirmado” puede significar algo distinto de “entrega completada”?
5. En tu mapa, ¿quién debe ser responsable de la última ubicación del repartidor?

### Respuestas para revisar
1. Es una parte delimitada del negocio donde los términos y reglas tienen un significado acordado.
2. Muestra los contextos, las relaciones entre ellos y la información que comparten.
3. No. Los límites pueden existir dentro de una sola aplicación; microservicios son una decisión de despliegue y operación adicional.
4. La confirmación de compra pertenece al proceso comercial; completar una entrega requiere que el paquete llegue al cliente y exista evidencia.
5. El contexto de Entregas, porque administra la ruta y sus actualizaciones.

Si tus respuestas usan otras palabras pero explican las mismas ideas, están bien. Si todavía parece que todo es “un pedido” con un único estado universal, vuelve a revisar las diferencias entre Compras y Entregas.

## Conclusión
Un bounded context es un límite que protege un lenguaje y unas reglas coherentes. Un context map muestra cómo se relaciona ese límite con otros y qué información cruza. Primero aclaramos el negocio y las responsabilidades; solo después decidimos si conviene desplegar esas partes como servicios independientes.

La próxima clase conecta estos límites con otra decisión: cómo describir y mantener la infraestructura de varios servicios cuando el código vive en un monorepo.
