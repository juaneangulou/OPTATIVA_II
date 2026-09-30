# Video 23: Bounded Context e infraestructura como código

## Fuentes de este video
- [Bounded context y context maps en microservicios](https://platzi.com/cursos/software-avanzado/bounded-context-y-context-maps-en-micros/)
- [Infraestructura como código en monorepos](https://platzi.com/cursos/software-avanzado/infraestructura-como-codigo-en-monorepos/)

## Para estudiar por tu cuenta
Un sistema puede tener límites de negocio claros y aun así desplegar sus servicios de forma manual e inconsistente. También puede tener archivos de infraestructura muy ordenados y repartir mal las responsabilidades del negocio.

Este capítulo conecta ambas preguntas: primero decides qué responsabilidad pertenece a cada contexto; después describes de manera repetible los recursos que necesita.

## 1. Bounded Context: una frontera de significado
Un **contexto delimitado** (Bounded Context) es una zona del sistema en la que los términos y reglas tienen un significado acordado.

En la plataforma logística, “pedido” puede significar una compra para el contexto de Pedidos y un trabajo de traslado para Entregas. Cada contexto mantiene las reglas que conoce:

- **Pedidos:** confirma la compra, registra cliente y productos.
- **Entregas:** asigna repartidor, ruta y estado del traslado.
- **Inventario:** conoce existencias y reservas.

Los contextos no son necesariamente servicios. Pueden ser módulos dentro de una sola aplicación. Definirlos aclara quién es responsable de cada dato antes de decidir cómo desplegarlo.

## 2. Context Map: quién comparte qué
Un **Context Map** (mapa de contextos) dibuja las fronteras y relaciones entre ellas.

```text
Pedidos -- pedido listo para logística --> Entregas
Inventario -- disponibilidad/reserva --> Pedidos
```

Cada flecha debe decir qué información cruza y qué significa. Pedidos podría compartir identificador, dirección y productos. Entregas no necesita recibir contraseñas ni copiar toda la información de pago.

Una relación confusa, como dos contextos modificando libremente la misma tabla, dificulta saber quién puede cambiar un dato y qué significado debe conservar.

## 3. ¿Qué es infraestructura como código?
La **infraestructura** son los recursos que permiten ejecutar el sistema: bases de datos, colas, redes, permisos y máquinas.

**Infraestructura como código (IaC)** significa describir esos recursos y sus propiedades en archivos que pueden revisarse y aplicarse mediante herramientas. Los archivos sirven como una receta versionada; no son la base de datos ni el servicio que describen.

Un **monorepo** guarda varios proyectos relacionados en un repositorio. Puede alojar código y descripciones de infraestructura juntos, pero no convierte automáticamente el sistema en una aplicación ni obliga a desplegar todas sus partes al mismo tiempo.

## 4. El ejemplo: una cola para Entregas
Cuando Pedidos confirma una compra, Entregas necesita recibir una tarea. El equipo decide usar una cola.

```text
plataforma/
  servicios/pedidos/
  servicios/entregas/
  infraestructura/cola-entregas/
```

La descripción IaC de la cola debería especificar, según las necesidades reales:

- quién puede publicar tareas: Pedidos;
- quién puede leerlas: Entregas;
- cuánto tiempo se conserva una tarea no procesada;
- qué tamaño o límites aplican a cada entorno;
- cómo se observan fallos y acumulación de mensajes.

Esto deja visible la relación entre el código que produce la tarea, el consumidor y el recurso compartido.

## 5. Un cambio coordinado, paso a paso
1. **Define el requisito:** Pedidos debe dejar una tarea después de confirmar la compra.
2. **Define el contrato:** acuerda qué significa el mensaje y qué campos necesita Entregas.
3. **Cambia el productor y el consumidor:** actualiza sus códigos para el mismo contrato.
4. **Describe el recurso:** agrega o modifica la cola y sus permisos en los archivos IaC.
5. **Revisa el plan:** usa la herramienta del proyecto para ver qué recursos creará, cambiará o eliminará.
6. **Prueba en desarrollo:** envía una tarea de prueba y confirma que Entregas la recibe.
7. **Repite en un entorno de pruebas:** verifica configuración y permisos antes de producción.
8. **Aplica en producción con control:** conserva el plan de recuperación y los permisos aprobados.

En un monorepo, el código y la IaC pueden revisarse juntos en una Pull Request. Eso permite encontrar, por ejemplo, que Entregas espera un campo que la definición del mensaje no contiene.

## 6. Qué significa “revisar el plan”
Una herramienta de IaC suele mostrar una **previsualización** o plan antes de cambiar un entorno. Ese plan puede indicar recursos que se crearán, modificarán o borrarán.

No lo apruebes sin leerlo. Si la tarea era añadir una cola y el plan propone reemplazar la base de datos de producción, detente y averigua por qué. El archivo puede ser válido y aun así el efecto no ser el esperado.

## 7. Entornos, permisos y secretos
Desarrollo, pruebas y producción pueden necesitar valores distintos, como nombres y capacidad. La diferencia debe estar descrita y ser intencional.

Un **secreto** es un dato que permite acceder o modificar recursos, como una contraseña o token. No lo escribas en archivos versionados. Usa el almacén protegido que adopte el proyecto y concede a cada servicio solo los permisos que necesita.

Una cola puede recibir un permiso de escritura para Pedidos y lectura para Entregas. No necesitan permiso para borrar cualquier recurso del entorno.

## 8. Riesgos al combinar contextos e IaC
- **Límite de negocio mal definido:** el código y la infraestructura son reproducibles, pero nadie sabe quién es dueño del dato.
- **Contrato ambiguo:** Pedidos y Entregas interpretan “confirmado” de manera diferente.
- **Cambio manual no registrado:** el entorno ya no coincide con los archivos.
- **Permisos demasiado amplios:** un servicio puede acceder a datos que no necesita.
- **Cambios destructivos:** una previsualización puede advertir que un recurso será reemplazado o eliminado.

Resolver primero el significado y la responsabilidad del recurso hace que la IaC describa una necesidad concreta, no una colección de servidores sin propósito.

## 9. Actividad de autoestudio
Pedidos debe enviar a Entregas la solicitud de preparar un paquete. Resuelve:

1. ¿Qué contexto es dueño del estado de compra?
2. ¿Qué contexto es dueño de la preparación y asignación?
3. ¿Qué información mínima se comparte?
4. Dibuja los proyectos y la cola en un monorepo.
5. Escribe quién puede publicar, leer y administrar la cola.
6. Anota tres cosas que revisarías en la previsualización de IaC.
7. Explica cómo probarías que el mensaje llega al consumidor correcto.

### Respuesta modelo
Pedidos mantiene la compra; Entregas mantiene preparación, ruta y entrega. Pedidos comparte identificador, dirección y artículos necesarios. La cola se describe dentro de `infraestructura`; solo Pedidos publica y Entregas consume. En la previsualización revisarías creación correcta, permisos limitados y ausencia de eliminaciones inesperadas. Una tarea ficticia de prueba permite confirmar que el consumidor la recibe.

## Comprueba lo que aprendiste
1. ¿Un Bounded Context tiene que ser un microservicio?
2. ¿Qué describe un archivo IaC?
3. ¿Monorepo significa desplegar todos los proyectos juntos?
4. ¿Qué debes hacer si una previsualización muestra una eliminación inesperada?

### Respuestas
1. No; puede ser un módulo dentro de una aplicación.
2. Los recursos necesarios y su configuración.
3. No; los proyectos pueden desplegarse por separado.
4. Detener la aplicación del plan e investigar qué causa el cambio.

## Conclusión
Los contextos delimitan significados y responsabilidades; la infraestructura como código describe los recursos que permiten ejecutar esos módulos o servicios. Al alojarlos en un monorepo, puedes revisar juntos cambios relacionados, pero sigues necesitando contratos claros, permisos mínimos y revisión del plan antes de modificar entornos reales.