# Video 18: Infraestructura como código en monorepos para microservicios

## Para estudiar por tu cuenta
En esta clase aprenderás cómo describir con archivos los recursos que necesita una aplicación, en vez de crearlos manualmente de manera distinta cada vez. Después veremos qué cambia cuando varios servicios y esos archivos viven juntos en un **monorepo**.

No necesitas haber creado servidores ni escribir código de infraestructura. El objetivo es comprender el proceso, reconocer qué debe revisar un equipo y explicar los riesgos antes de aplicar un cambio.

## 1. La situación: tres entornos que no se parecen
Una plataforma logística tiene una aplicación de pedidos que envía tareas a una cola y un servicio que las procesa. El equipo trabaja en tres lugares:

- **Desarrollo:** entorno de trabajo para probar cambios.
- **Pruebas:** entorno parecido al real para comprobar el sistema antes de publicarlo.
- **Producción:** entorno real usado por clientes y operaciones.

Al principio, una persona crea manualmente la cola, la base de datos y los permisos en cada entorno. Con el tiempo, las configuraciones se separan: desarrollo tiene una cola llamada `pedidos-dev`; pruebas usa `cola-pruebas`; producción tiene otro tamaño y otros permisos. Nadie sabe con certeza si las diferencias son intencionales o accidentales.

El problema no es que los entornos tengan que ser idénticos en todo. Producción puede necesitar más capacidad que desarrollo. El problema es que las diferencias no estén registradas ni se puedan revisar.

## 2. Conceptos explicados antes de combinarlos
- **Infraestructura:** los recursos que permiten ejecutar un sistema: computadoras o máquinas virtuales, redes, bases de datos, colas y permisos.
- **Configuración:** los valores que indican cómo debe funcionar un recurso, como su tamaño, nombre o tiempo de retención.
- **Infraestructura como código:** describir los recursos y configuraciones en archivos que el equipo puede revisar y volver a usar.
- **Monorepo:** un solo repositorio de código que contiene varios proyectos relacionados. Puede incluir varios servicios y también archivos de infraestructura.
- **Repositorio:** lugar compartido donde el equipo guarda y registra los cambios de un proyecto.
- **Entorno:** lugar separado donde se ejecuta el sistema, por ejemplo desarrollo, pruebas o producción.
- **Aplicar:** pedir a una herramienta que realice los cambios descritos en los archivos sobre un entorno.

La idea clave es: **infraestructura como código describe cómo preparar el entorno; monorepo describe dónde guarda el equipo sus proyectos y archivos.** Son decisiones relacionadas, pero no significan lo mismo.

## 3. Una analogía: el plano y el edificio
Un archivo de infraestructura se parece a un plano de construcción. El plano describe qué espacios y conexiones se necesitan; no es el edificio mismo.

- El **plano** corresponde a la descripción escrita de los recursos.
- La **construcción** corresponde a aplicar esa descripción en una cuenta o entorno real.
- La **revisión del plano** corresponde a leer los cambios antes de construir.
- La **inspección final** corresponde a comprobar que el entorno creado funciona.

La analogía ayuda a entender que escribir una descripción no crea automáticamente el recurso. Hay un paso separado que la aplica. También tiene un límite: en tecnología, una herramienta puede modificar o borrar recursos existentes, por eso una revisión cuidadosa es fundamental.

## 4. Describir la infraestructura de nuestra plataforma
La aplicación de pedidos necesita una cola para dejar una tarea de entrega y un trabajador que la lea. Una **cola** es una lista temporal de tareas: una parte del programa deja una tarea y otra puede recogerla después.

El equipo puede describir esos recursos como archivos dentro del repositorio:

```text
plataforma-logistica/
	servicios/
		pedidos/
		entregas/
	infraestructura/
		cola-entregas/
		base-datos/
```

Este árbol muestra una posible organización. No es una estructura obligatoria ni un archivo que pueda ejecutarse tal cual. Indica que los proyectos de los servicios y las descripciones de sus recursos están en el mismo repositorio.

En un archivo de infraestructura, el equipo podría dejar claro:

- Qué cola necesita el flujo de entregas.
- Qué servicio puede escribir tareas en ella.
- Qué servicio puede leerlas.
- Cuánto tiempo se conserva una tarea sin procesar.
- Qué tamaño o capacidad se requiere en cada entorno.

En lugar de depender de la memoria de una persona, las decisiones quedan visibles para revisión.

## 5. ¿Qué aporta tenerlo en un monorepo?
Supón que una persona cambia el servicio de pedidos para enviar un nuevo tipo de tarea. Si el código y la descripción de la cola están en repositorios distintos, el equipo debe coordinar dos cambios separados. Puede ocurrir que el servicio llegue primero y la cola aún no acepte la nueva tarea.

Si ambos cambios están en un mismo monorepo, una propuesta de cambio puede mostrar el código y la infraestructura juntos. Quien revisa puede preguntar:

- ¿El servicio escribe los datos que la cola espera?
- ¿El servicio de entregas puede leerlos?
- ¿El recurso conserva las tareas el tiempo necesario?
- ¿El cambio elimina o reemplaza otro recurso?

Esto facilita revisar cambios relacionados en una sola propuesta. Sin embargo, un monorepo no obliga a desplegar todos los servicios juntos ni garantiza que las descripciones estén bien hechas.

## 6. El flujo de trabajo, paso a paso

### Paso 1: describir el cambio que necesita el producto
La necesidad no es “usar infraestructura como código”. La necesidad es concreta: “Cuando se confirma una compra, el servicio debe dejar una tarea que Entregas pueda procesar aunque ese servicio esté ocupado”.

Comenzar por la necesidad evita crear recursos que nadie necesita.

### Paso 2: identificar recursos y responsables
El equipo escribe qué partes participan: servicio de pedidos, cola de tareas y servicio de entregas. También define quién puede enviar tareas, quién puede leerlas y qué datos se incluyen.

### Paso 3: cambiar los archivos del monorepo
El cambio puede incluir el servicio de pedidos, el servicio de entregas y la descripción de la cola. Los tres quedan relacionados en una sola propuesta para que se puedan revisar juntos.

### Paso 4: revisar antes de aplicar
Antes de crear o modificar recursos reales, una herramienta puede mostrar un resumen de lo que planea hacer. A esta vista a veces se le llama **plan** o **previsualización**.

El equipo revisa especialmente si el cambio:

- Creará el recurso esperado.
- Cambiará permisos o capacidad.
- Reemplazará o borrará recursos existentes.
- Afectará a otro entorno o servicio.

Si el resumen propone borrar la base de datos de producción y eso no era parte de la tarea, el equipo no continúa: primero investiga la razón.

### Paso 5: aplicar en un entorno seguro
Primero se aplica en desarrollo o pruebas. El equipo confirma que los servicios pueden comunicarse con la cola y que una tarea llega a su destino.

Después, y con la aprobación necesaria, se aplica en producción. Que funcione en desarrollo es una buena señal, pero no demuestra automáticamente que producción tiene los mismos permisos, datos o capacidad.

### Paso 6: comprobar el resultado
El equipo verifica que la cola existe, que solo los servicios esperados pueden usarla y que un pedido de prueba recorre el camino completo.

### Paso 7: mantener la descripción actualizada
Si una persona cambia un recurso manualmente en la consola y no actualiza los archivos, la descripción guardada puede dejar de coincidir con la realidad. Esta diferencia se conoce como **desviación**: el entorno real ya no corresponde a lo que dicen los archivos.

La revisión periódica ayuda a detectar diferencias antes de que causen errores.

## 7. Desarrollo, pruebas y producción
Los tres entornos necesitan recursos parecidos, pero no siempre del mismo tamaño:

| Entorno | Para qué se usa | Diferencia razonable |
|---|---|---|
| Desarrollo | Probar cambios mientras se construye el sistema | Puede usar recursos pequeños y datos de ejemplo |
| Pruebas | Comprobar cambios en condiciones similares a las reales | Puede tener más datos y varias pruebas simultáneas |
| Producción | Atender pedidos y clientes reales | Requiere capacidad, protección y recuperación adecuadas |

Una forma segura de organizarlo es describir la base de los recursos una vez y declarar por separado qué valores cambian entre entornos. Por ejemplo, el nombre puede cambiar y producción puede requerir más capacidad. Esto evita copiar archivos completos que luego se separan y acumulan errores.

## 8. Lo que NO debe guardarse como texto normal
Algunos valores permiten entrar o modificar recursos, por ejemplo contraseñas, llaves privadas y claves de acceso. Se llaman **secretos** porque deben mantenerse confidenciales.

No los escribas directamente en los archivos del repositorio. Si se guardan allí, otras personas con acceso al código podrían verlos y podrían quedar registrados en el historial incluso después de borrar la línea.

En su lugar, el equipo usa un almacén protegido de secretos y da acceso solo a los procesos y personas que lo necesitan. Los archivos de infraestructura pueden indicar dónde obtener el secreto sin revelar su valor.

También se deben revisar los **permisos**. Un servicio que solo necesita leer tareas no debería recibir permiso para borrar toda la base de datos.

## 9. Qué resuelve y qué no resuelve
### Infraestructura como código puede ayudar a:
- Repetir una preparación de entorno de forma consistente.
- Revisar quién propuso un cambio y por qué.
- Detectar cambios antes de aplicarlos.
- Mantener alineados el código de los servicios y los recursos que necesitan.

### No garantiza por sí sola:
- Que el diseño sea correcto o seguro.
- Que un cambio nunca borre datos.
- Que los secretos estén protegidos automáticamente.
- Que todos los entornos deban ser idénticos.
- Que el sistema esté listo para producción solo porque los archivos están en Git.

La herramienta sigue instrucciones. El equipo tiene que entender las instrucciones y comprobar el resultado.

## 10. La decisión: ¿monorepo o varios repositorios?
Un **monorepo** guarda varios proyectos en un mismo repositorio. Un enfoque de **varios repositorios** guarda cada servicio o componente por separado.

| Opción | Puede ayudar cuando | Costo o cuidado |
|---|---|---|
| Un monorepo | Los servicios cambian juntos y es útil revisar código e infraestructura en una sola propuesta | Hay que organizar carpetas, permisos y pruebas para que el repositorio siga manejable |
| Varios repositorios | Los equipos despliegan y mantienen servicios con mucha independencia | Coordinar un cambio que cruza varios repositorios puede llevar más pasos y tiempo |

La decisión depende de cómo trabaja el equipo. Un monorepo no es automáticamente mejor, y tener IaC no obliga a usarlo.

## 11. Actividad de autoestudio
### Situación
El servicio de pedidos necesita dejar en una cola una tarea cada vez que una compra queda lista para entrega. El servicio de Entregas lee la tarea y la procesa. El equipo tiene un solo repositorio con ambos servicios.

Resuelve el caso sin instalar herramientas:

1. Dibuja los dos servicios, la cola y los entornos de desarrollo, pruebas y producción.
2. Indica qué servicio puede escribir en la cola y cuál puede leerla.
3. Escribe qué cambio harías en el servicio de pedidos y qué recurso describirías en infraestructura.
4. Antes de aplicar, anota tres elementos que revisarías en la previsualización.
5. Explica cómo comprobarías que la tarea llega al servicio correcto.
6. Indica qué valor no guardarías directamente en los archivos del repositorio.
7. Describe qué podría salir mal si alguien cambia producción manualmente y no actualiza los archivos.

### Pistas
- No empieces por elegir una herramienta; primero identifica la necesidad.
- “Escribir” significa dejar una tarea en la cola; “leer” significa recogerla para trabajarla.
- En la previsualización, presta atención a cambios y eliminaciones, no solo a recursos nuevos.
- Un cambio manual que no queda anotado hace que el archivo y el entorno puedan describir realidades distintas.

## 12. Solución modelo
1. El servicio de pedidos produce una tarea; la cola la conserva temporalmente; Entregas la recoge. Desarrollo y pruebas sirven para validar antes de producción.
2. Pedidos puede escribir. Entregas puede leer. No hace falta dar a ambos permisos para hacer todo.
3. Se modifica el servicio para enviar la tarea y se describe la cola y sus permisos en archivos versionados junto a los servicios.
4. Se revisa que el plan cree la cola correcta, asigne solo los permisos necesarios y no borre ni reemplace recursos ajenos al cambio.
5. Se envía un pedido de prueba y se comprueba que Entregas recibe y procesa la tarea una sola vez según el comportamiento esperado.
6. Contraseñas y claves de acceso son secretos; deben estar en un almacén protegido, no escritas directamente en el repositorio.
7. El entorno puede dejar de coincidir con la descripción guardada. Una aplicación futura del plan podría modificar recursos inesperadamente, así que primero se detecta y resuelve esa diferencia.

La solución puede variar según la organización. Se considera razonada si identifica los recursos, limita permisos, revisa el plan antes de aplicar y comprueba el recorrido completo.

## 13. Comprueba lo que aprendiste
Responde sin mirar las secciones anteriores y luego revisa:

1. ¿Cuál es la diferencia entre infraestructura como código y monorepo?
2. ¿Por qué se revisa una previsualización antes de aplicar un cambio?
3. ¿Qué riesgo hay al guardar una contraseña en un repositorio?
4. ¿Qué significa que producción tenga una desviación respecto a los archivos?
5. ¿Un monorepo obliga a desplegar todos los servicios al mismo tiempo?

### Respuestas
1. Infraestructura como código describe recursos mediante archivos; monorepo es una forma de guardar varios proyectos en un mismo repositorio.
2. Permite descubrir cambios inesperados, especialmente reemplazos o eliminaciones, antes de afectar un entorno.
3. Otras personas podrían verla y puede permanecer en el historial aun después de borrarla del archivo actual.
4. Que el entorno real y la descripción guardada ya no coinciden.
5. No. El repositorio puede contener varios servicios que se despliegan por separado.

## Cierre
Infraestructura como código convierte instrucciones sobre los recursos del sistema en cambios que el equipo puede revisar y repetir. Un monorepo puede reunir esos archivos junto con varios servicios para que los cambios relacionados se vean en un mismo lugar.

La seguridad no aparece por usar una herramienta: primero se entiende qué se necesita, se revisa qué cambiará, se protege la información confidencial, se prueba en un entorno seguro y se comprueba el resultado.
