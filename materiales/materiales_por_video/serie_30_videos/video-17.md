# Video 17: BDD y modelo C4

## Fuentes de este video
- [Behavior Driven Development para alinear equipos técnicos y de negocio](https://platzi.com/cursos/software-avanzado/behavior-driven-development-para-alinear/)
- [Modelo C4 para diagramar arquitecturas](https://platzi.com/cursos/software-avanzado/modelo-c4-para-diagramar-arquitecturas/)

## Navegación
[⬅️ Video anterior: monorepos y calidad](video-16.md) | [📚 Índice de la serie](README.md) | [➡️ Video siguiente: documentación viva y revisión con IA](video-18.md)

## Para estudiar por tu cuenta
BDD y C4 responden preguntas diferentes, pero pueden usarse juntos. **Behavior Driven Development (BDD)** ayuda a aclarar qué comportamiento necesita una persona. El **modelo C4** ayuda a explicar qué partes del sistema participan para ofrecerlo.

Usaremos un solo caso de la plataforma logística: confirmar un pedido cuando hay inventario suficiente.

## 1. Antes de programar: aclara el comportamiento
Una frase como “el pedido se confirma correctamente” deja preguntas abiertas:

- ¿Qué significa “correctamente”?
- ¿Qué pasa si el inventario no alcanza?
- ¿Qué debería ver el cliente?
- ¿Se descuenta el inventario si el pedido no se confirma?

BDD busca responder esas preguntas con ejemplos concretos antes de construir la función.

## 2. Dado–Cuando–Entonces
Un escenario suele tener tres partes:

- **Dado:** el contexto que ya existe.
- **Cuando:** la acción que realiza alguien o el sistema.
- **Entonces:** el resultado observable que debe ocurrir.

Ejemplo del camino exitoso:

```text
Escenario: confirmar un pedido con inventario suficiente
Dado que hay 5 unidades del producto A
Cuando la clienta solicita 2 unidades
Entonces el pedido queda confirmado
Y quedan 3 unidades disponibles
```

Y un caso de rechazo:

```text
Escenario: rechazar un pedido que supera las existencias
Dado que hay 1 unidad del producto A
Cuando la clienta solicita 2 unidades
Entonces el pedido no queda confirmado
Y las existencias siguen siendo 1 unidad
```

Los números y reglas son ejemplos. En un proyecto real se acuerda con el negocio si reservar unidades al iniciar, al pagar o en otro momento.

## 3. Qué aporta BDD y qué no
Los escenarios BDD hacen visible el significado del requisito y permiten convertir ejemplos en pruebas. No sustituyen todas las pruebas unitarias ni obligan a escribir cada detalle técnico en lenguaje natural.

Un escenario es útil si alguien del negocio puede entenderlo y si la condición final puede comprobarse. Si una frase admite dos interpretaciones, todavía falta acordarla.

## 4. Modelo C4: cuatro niveles de acercamiento
C4 organiza diagramas como acercamientos sucesivos:

1. **Contexto:** quién usa el sistema y con qué sistemas externos se comunica.
2. **Contenedores:** aplicaciones, procesos y almacenes de datos principales.
3. **Componentes:** partes importantes dentro de un contenedor.
4. **Código:** clases o estructuras internas cuando explicarlas realmente ayuda.

En C4, un **contenedor** es una unidad ejecutable o un almacén de datos. No significa necesariamente que use Docker.

No siempre necesitas cuatro diagramas. Elige el nivel que responda una pregunta concreta y detente cuando añadir detalle ya no ayude a quien lee.

## 5. El mismo escenario, explicado con C4

### Contexto
La clienta usa la tienda digital. La plataforma logística valida el pedido. El proveedor de pagos confirma el pago.

```text
Clienta -> Plataforma logística -> Proveedor de pagos
```

Este dibujo responde quién participa, pero todavía no explica qué aplicaciones contiene la plataforma.

### Contenedores
```text
Tienda web -> API logística -> Base de datos
                         -> Proveedor de pagos
```

La API recibe la solicitud; la base de datos conserva pedidos e inventario. El proveedor de pagos es externo.

### Componentes dentro de la API
```text
Endpoint de pedidos -> Caso de uso ConfirmarPedido
                               |             |
                               v             v
                         Pedidos        Inventario
```

El caso de uso coordina la confirmación. Pedidos conserva su información; Inventario comprueba y actualiza existencias según las reglas acordadas.

## 6. Cómo se conectan BDD y C4
El escenario BDD dice qué comportamiento debe suceder. El diagrama C4 explica qué partes podrían colaborar para ofrecerlo.

- BDD: “Con 5 unidades, solicitar 2 confirma el pedido y deja 3 disponibles”.
- C4: muestra que la API recibe la solicitud, el caso de uso coordina y los componentes de Pedidos e Inventario participan.

Si el escenario dice una cosa y el diagrama describe un flujo incompatible, hay una pregunta para resolver antes de implementar. Uno no reemplaza al otro: el escenario se concentra en el resultado; el diagrama, en la estructura y las relaciones.

## 7. Del ejemplo a las pruebas
Puedes convertir el camino exitoso en una prueba del caso de uso con inventario de ensayo. Una prueba de integración puede verificar después que la base de datos real guarda la reserva junto con el pedido.

El escenario de rechazo permite verificar que no se confirme el pedido ni se descuenten unidades que no existen. El nivel de prueba depende de la parte que quieras comprobar:

- regla pura: prueba unitaria;
- conexión entre caso de uso y almacenamiento: prueba de integración;
- límites entre partes: prueba de arquitectura.

## 8. Actividad de autoestudio
Dibuja y describe el caso “la tienda solicita una devolución”:

1. Escribe un escenario Dado–Cuando–Entonces para una devolución aceptada.
2. Escribe otro para una devolución rechazada.
3. Dibuja el contexto con cliente, plataforma y sistema de pagos.
4. Dibuja contenedores para la tienda, API, base de datos y proveedor de pagos.
5. Amplía la API con componentes que expliquen quién valida la devolución y quién solicita el reembolso.
6. Anota qué decisión de negocio no puedes inventar, como el plazo permitido para devolver un producto.

## 9. Respuesta modelo
```text
Escenario: aceptar una devolución dentro del plazo
Dado que el pedido fue entregado y todavía está dentro del plazo acordado
Cuando la clienta solicita la devolución con un motivo válido
Entonces la solicitud queda registrada para revisión
Y el sistema no afirma que el dinero ya fue reembolsado
```

La tienda envía la solicitud a la API. Un caso de uso consulta Pedidos y la política de devoluciones. Si se aprueba, puede pedir al sistema externo de pagos que procese el reembolso. La API registra el resultado y lo comunica a la clienta.

El plazo y los motivos aceptados deben venir de una política real del negocio; no los determina el diagrama ni la herramienta de pruebas.

## Comprueba lo que aprendiste
1. ¿Qué explica un escenario BDD que un diagrama C4 no explica por sí solo?
2. ¿Qué muestra C4 que el escenario no detalla?
3. ¿Todos los diagramas C4 deben llegar al nivel de clases?
4. ¿Por qué no debes inventar el plazo de una devolución?

### Respuestas
1. El comportamiento esperado ante una situación concreta.
2. Las partes principales del sistema, sus responsabilidades y comunicaciones.
3. No; se llega solo al nivel necesario para responder la pregunta.
4. Porque es una regla del negocio que debe confirmarse con la organización.

## Taller aplicado: conectar escenario, diagrama y prueba
Toma el caso “confirmar un pedido con inventario suficiente” y produce tres evidencias relacionadas:

1. En BDD, escribe el resultado observable para el cliente y el rechazo por inventario insuficiente.
2. En C4, muestra quién inicia la acción, qué contenedor recibe la solicitud, dónde se consulta inventario y qué sistema externo participa.
3. En la prueba, comprueba que el caso exitoso confirma una vez y que el caso rechazado no descuenta existencias.
4. Compara los tres artefactos: los nombres del escenario, el diagrama y la prueba deben usar los mismos términos.
5. Si el diagrama incluye un servicio que el escenario no necesita, explica por qué existe o retíralo.

### Error que debes evitar
Un diagrama lleno de cajas no demuestra una arquitectura madura. Un escenario lleno de detalles técnicos tampoco demuestra que el comportamiento sea correcto. La calidad está en la relación: una necesidad concreta, una estructura suficiente para cumplirla y una prueba que compruebe la afirmación importante.

### Evidencia de aprendizaje
Conserva dos escenarios, un diagrama de contexto, un diagrama de contenedores y una tabla que relacione cada escenario con su prueba. Esa tabla permite detectar rápidamente qué parte del comportamiento todavía no tiene protección.

## Conclusión
BDD convierte requisitos ambiguos en ejemplos revisables. C4 muestra qué partes intervienen para cumplirlos. Juntos ayudan a conectar lo que una persona espera con la estructura que el sistema necesita, sin confundir el comportamiento con la tecnología.