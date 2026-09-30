# Video 6: Modelo C4 para diagramar arquitecturas

## Para estudiar por tu cuenta
Un diagrama de arquitectura puede volverse difícil de leer si mezcla usuarios, servicios, clases y detalles de red en una sola imagen. El **modelo C4** propone describir un sistema con varios niveles de acercamiento, como si primero vieras un mapa de una ciudad y luego ampliaras hasta una calle.

Los cuatro niveles se llaman Context, Container, Component y Code. En esta clase aprenderás qué pregunta responde cada uno y cuándo detenerte.

## 1. Contexto: ¿quién usa el sistema y con qué se conecta?
El diagrama de **Contexto** muestra el sistema como una caja, sus usuarios y los sistemas externos con los que conversa.

Para la plataforma logística podrías mostrar:

- Cliente: consulta el estado del pedido.
- Operador: registra y revisa pedidos.
- Plataforma logística: organiza pedidos y entregas.
- Proveedor de pagos: confirma transacciones.
- Proveedor de notificaciones: envía avisos.

Este nivel ayuda a entender el alcance sin mostrar todavía la organización interna del código.

## 2. Contenedores: ¿qué aplicaciones y almacenes forman el sistema?
En C4, un **contenedor** es una unidad ejecutable o almacén de datos, como una aplicación web, una API, un proceso en segundo plano o una base de datos. No significa necesariamente un contenedor Docker.

Un diagrama de contenedores podría mostrar la aplicación del cliente, la API, el trabajador de notificaciones y la base de datos, con flechas que expliquen quién llama a quién.

## 3. Componentes: ¿qué partes principales hay dentro de una unidad?
El diagrama de **Componentes** amplía un contenedor. Dentro de la API podrías mostrar Pedidos, Seguimiento y Adaptador de pagos. Cada componente tiene una responsabilidad y se comunica mediante conexiones identificables.

No incluyas todas las clases si eso vuelve ilegible el dibujo. Elige componentes que ayuden a responder una pregunta de diseño.

## 4. Código: ¿cómo se implementa un componente?
El nivel de **Código** puede mostrar clases, interfaces o módulos de un componente. No siempre se necesita un diagrama de este nivel: el código suele ser la descripción más exacta y se actualiza más rápido que una imagen detallada.

## 5. Un mismo sistema, cuatro acercamientos
```text
Contexto: cliente -> plataforma logística -> pagos/notificaciones
Contenedores: aplicación web -> API -> base de datos/worker
Componentes en API: pedidos -> seguimiento -> adaptador de pagos
Código de pedidos: clases y contratos que implementan esa capacidad
```

Cada nivel responde una pregunta diferente. No es necesario que todos los sistemas tengan cuatro diagramas grandes; crea el nivel que ayude a quien va a leerlos.

## 6. Reglas para que un diagrama se entienda
- Escribe el nombre y la responsabilidad de cada caja.
- Nombra las flechas con la información o la acción que viaja.
- Indica el tipo de usuario o sistema externo.
- Incluye una leyenda si usas colores o símbolos.
- Mantén un nivel de detalle consistente dentro del dibujo.
- Actualiza el diagrama cuando una decisión importante cambie.

## 7. Actividad de autoestudio
Dibuja el contexto y los contenedores de una consulta de pedido:

1. Incluye cliente, soporte y plataforma logística.
2. Incluye aplicación, API, base de datos y proveedor de notificaciones.
3. Dibuja flechas y escribe qué información cruza cada una.
4. Elige la API y amplíala con tres componentes.
5. Explica qué detalles decidiste no mostrar y por qué.

### Respuesta modelo
En contexto, el cliente y soporte usan la plataforma; la plataforma se comunica con notificaciones. En contenedores, la aplicación llama a la API, la API consulta la base de datos y puede solicitar un aviso al trabajador de notificaciones. Dentro de la API, Pedidos valida acceso, Seguimiento obtiene el estado y el Adaptador de notificaciones solicita el envío.

Las flechas deben tener nombres comprensibles, por ejemplo “consulta estado del pedido” y “solicita envío de aviso”. No hace falta mostrar todas las clases para explicar este recorrido.

## Comprueba lo que aprendiste
1. ¿Qué muestra el diagrama de contexto?
2. ¿Un contenedor C4 tiene que ser Docker?
3. ¿Cuándo es útil dibujar componentes?
4. ¿Debes crear siempre los cuatro niveles?

**Respuestas:** usuarios, sistema y relaciones externas; no, es una unidad ejecutable o almacén lógico; cuando necesitas explicar la organización interna de un contenedor; no, eliges los niveles que ayudan a responder una pregunta.

## Conclusión
C4 organiza diagramas por nivel de acercamiento: contexto, contenedores, componentes y código. Su objetivo es que cada persona encuentre el nivel de explicación que necesita sin mezclar toda la arquitectura en un solo dibujo.
