# Video 15: Migraciones de base de datos con Flyway

## Propósito de la clase
Al terminar, podrás explicar con tus propias palabras por qué hay que planear los cambios en una base de datos, qué trabajo hace Flyway y qué debe revisar un equipo antes de cambiar información que ya está en uso. No necesitas saber programar para seguir la explicación; los fragmentos técnicos están traducidos a lenguaje cotidiano.

## 1. La situación: necesitamos guardar algo nuevo
Imagina que una empresa de entregas usa un programa para guardar sus pedidos. Por ahora, cada pedido tiene un número, el nombre del cliente y una dirección. La empresa quiere que sus clientes también puedan consultar si el paquete está pendiente, en camino o entregado.

El cambio parece pequeño: agregar el estado del pedido. Pero hay una pregunta importante: **¿qué hacemos con los miles de pedidos que ya existen y que todavía no tienen ese dato?**

Si pensamos solo en los pedidos nuevos, el programa podría fallar al consultar los antiguos. Si inventamos un estado para ellos, podríamos mostrar información falsa al cliente. Por eso el cambio debe planearse, probarse y aplicarse en un orden conocido.

## 2. Una analogía: el archivador de pedidos
Imagina un archivador en el que cada hoja representa un pedido. En cada hoja hay espacios para el número, el nombre y la dirección. El conjunto de hojas es parecido a una **base de datos**: un lugar organizado donde un programa conserva información.

Agregar un espacio nuevo en las hojas equivale a cambiar la **estructura** de la base de datos. Ese cambio puede afectar tanto a las hojas nuevas como a las antiguas. No basta con decidir que el espacio debe existir: también hay que resolver qué escribir en las hojas que ya estaban guardadas.

La comparación tiene un límite: una base de datos no es literalmente un archivador. El programa y la base de datos se comunican mediante instrucciones, y esas instrucciones deben ser compatibles. La analogía solo nos ayuda a entender que hay información existente que debemos proteger.

## 3. Palabras clave, en sencillo
- **Base de datos:** lugar donde un programa guarda información que necesita recordar.
- **Tabla:** grupo de datos del mismo tipo; por ejemplo, una lista de pedidos.
- **Columna o campo:** un tipo de dato que se guarda para cada pedido; por ejemplo, dirección o estado.
- **Fila o registro:** la información de un pedido particular.
- **Estructura:** las tablas, columnas y reglas que organizan la información.
- **Migración:** un cambio planificado a esa estructura o a los datos guardados.
- **Archivo de migración:** una instrucción guardada en el proyecto para repetir el cambio en orden.
- **Flyway:** herramienta que aplica esos archivos y anota cuáles ya se ejecutaron.
- **Entorno de prueba:** una copia separada donde se ensaya el cambio antes de usar información real.
- **Respaldo:** copia de seguridad de los datos. Ayuda a recuperarse, aunque no sustituye las pruebas.

## 4. Entonces, ¿qué hace Flyway?
Flyway no decide qué información necesita la empresa ni adivina cómo modificar la base de datos. El equipo prepara los cambios; Flyway ayuda a ejecutarlos ordenadamente y a llevar un registro.

Podemos imaginarlo como una persona encargada de revisar una bitácora:

1. Busca los archivos de cambio que preparó el equipo.
2. Comprueba cuáles ya se ejecutaron en esa base de datos.
3. Aplica los que todavía faltan, siguiendo su número de versión.
4. Anota que se ejecutaron, para no repetirlos la próxima vez.

El registro queda en una tabla de control que Flyway mantiene en la base de datos. No hace falta memorizar su nombre técnico. Lo importante es que el equipo puede saber qué cambios se aplicaron y en qué orden.

Esto resuelve un problema habitual: si cada persona cambia su base de datos manualmente, es fácil que cada computadora termine con una estructura diferente. Con archivos versionados, todo el equipo puede seguir los mismos pasos.

## 5. El ejemplo completo: agregar el estado de la entrega
Vamos a seguir este caso durante toda la clase. Hoy la tabla de pedidos guarda el número del pedido, el cliente y la dirección. La empresa también registra el estado en una hoja de cálculo que usa el personal de entregas.

El objetivo es que el sistema nuevo pueda guardar y mostrar el estado. Los posibles estados acordados con el negocio son:

- **Pendiente:** todavía no se ha iniciado la entrega.
- **En camino:** el repartidor ya lleva el pedido.
- **Entregado:** el cliente recibió el pedido.
- **Por confirmar:** no tenemos información suficiente para asegurar el estado.

El último estado es importante. Si un pedido antiguo no aparece en la hoja de cálculo, no debemos marcarlo como “pendiente” solo para llenar el espacio. **Un valor inventado puede engañar al cliente y al equipo de soporte.**

### Paso A: entender qué existe antes del cambio
Antes de escribir una instrucción, el equipo averigua:

- Qué información guarda hoy cada pedido.
- Cuántos pedidos existentes hay.
- Dónde se consulta actualmente el estado de una entrega.
- Qué partes del programa leen la lista de pedidos.
- Qué debe mostrarse cuando el estado aún no se conoce.

Esta revisión evita cambiar una pieza que otras partes del programa esperan encontrar de otra manera.

### Paso B: acordar qué significa cada estado
Antes de implementar, define el significado de cada estado. Por ejemplo, ¿“en camino” empieza cuando el paquete sale del almacén o cuando el repartidor confirma que lo recogió?

Si tienes acceso a las personas que operan el proceso, confirma con ellas esta definición. Si estudias por tu cuenta y no tienes ese dato, escríbelo como una suposición pendiente; no lo presentes como un hecho. Un programa puede guardar un estado correctamente y aun así mostrar información engañosa si el término no tiene un significado compartido.

### Paso C: crear y nombrar el cambio
El equipo guarda la instrucción de base de datos en un archivo. Un nombre posible es:

`V2__Agregar_estado_de_entrega.sql`

Leamos el nombre por partes:

- `V2` significa que este cambio tiene la versión 2.
- `__` separa la versión de la descripción.
- `Agregar_estado_de_entrega` explica el propósito.
- `.sql` indica que contiene instrucciones para la base de datos.

El nombre `V2` solo es un ejemplo. El equipo revisa el historial para elegir una versión que venga después de las que ya existen.

### Paso D: entender la instrucción técnica
Una instrucción podría verse así:

```sql
ALTER TABLE pedidos ADD COLUMN estado_entrega VARCHAR(20);
```

No tienes que aprender SQL para entender la intención. En palabras sencillas, dice: “En la lista de pedidos, agrega un nuevo espacio llamado `estado_entrega` que pueda guardar un texto corto”.

Los nombres y la forma exacta de escribir la instrucción pueden variar según la base de datos que use el proyecto. El ejemplo sirve para reconocer la idea, no para copiarlo directamente en un sistema real.

Al principio, ese nuevo espacio puede quedar vacío en los pedidos antiguos. En términos técnicos, se dice que permite un valor `NULL`; aquí significa simplemente “todavía no hay un dato guardado”. El equipo debe decidir cómo tratar ese caso antes de mostrarlo a los usuarios.

### Paso E: decidir qué pasa con los pedidos antiguos
El equipo compara los pedidos con la hoja de cálculo:

- Si encuentra el estado, lo registra en el pedido.
- Si no encuentra información confiable, usa “Por confirmar”.
- No cambia un estado por otro sin una razón comprobable.

Este proceso de completar los registros antiguos también es parte de una migración. La migración no siempre es solo agregar una columna; también puede requerir adaptar los datos que ya existen.

### Paso F: probar en una copia
Antes de cambiar la base que usa la empresa, el equipo hace el ensayo en una copia parecida. Comprueba tanto el cambio como las tareas que ya funcionaban.

| Prueba | Qué queremos comprobar |
|---|---|
| Abrir un pedido antiguo | El pedido sigue apareciendo con su cliente y dirección. |
| Consultar un pedido con información confiable | Se muestra el estado correcto. |
| Consultar un pedido sin información confiable | Se muestra “Por confirmar”, no un estado inventado. |
| Crear un pedido nuevo | El programa puede guardar sus datos y un estado inicial válido. |
| Revisar tareas que no cambiaron | Crear pedidos y consultar direcciones sigue funcionando. |

Si una prueba falla, el equipo se detiene, entiende por qué y corrige el plan antes de continuar. No se soluciona un resultado incorrecto ocultándolo con otro dato.

### Paso G: aplicar el cambio con control
Cuando las pruebas pasan, el equipo elige cuándo actualizar la base real. Antes de hacerlo confirma que existe un respaldo reciente y que alguien sabe cómo responder si el cambio afecta al servicio.

Flyway encuentra la migración `V2`, la aplica y registra que ya se ejecutó. Si se inicia otra vez, Flyway ve ese registro y no vuelve a aplicar la versión 2. Si aparece más adelante una versión 3, ejecuta la nueva después de la 2.

### Paso H: verificar después del cambio
El trabajo no termina cuando Flyway dice que la migración se ejecutó. El equipo revisa el resultado real: pedidos, estados, pantallas y tareas relacionadas. Si ve algo inesperado, detiene los siguientes cambios y sigue el plan de recuperación.

## 6. Lo que cambia, explicado visualmente

| Momento | Qué existe en la lista de pedidos | Qué hacemos con el estado |
|---|---|---|
| Antes | Número, cliente y dirección | El estado se consulta en otro lugar. |
| Después de preparar la estructura | Número, cliente, dirección y estado | Los pedidos antiguos todavía pueden no tener valor. |
| Después de revisar los datos | La misma información y un campo de estado | Usamos el estado comprobado o “Por confirmar”. |
| Después de verificar la aplicación | El sistema muestra el nuevo dato | Confirmamos que los pedidos y las demás tareas siguen funcionando. |

Esta tabla describe el plan. No es el resultado de una base de datos real. En cada proyecto hay que medir cuántos registros existen y comprobar los datos propios de la organización.

## 7. ¿Qué podría salir mal?

### Error 1: llenar todos los estados antiguos con “Pendiente”
**Por qué es un problema:** algunos pedidos podrían estar entregados. El programa mostraría una respuesta falsa.

**Qué hacer:** confirmar el estado con una fuente confiable. Si no existe, usar un estado explícito como “Por confirmar” y decidir cómo resolver esos casos.

### Error 2: agregar el campo y olvidar que los programas también lo usan
**Por qué es un problema:** la base de datos puede tener el nuevo espacio, pero una pantalla podría no saber leerlo o mostrarlo.

**Qué hacer:** probar el cambio junto con el programa, no solo en la base de datos.

### Error 3: editar el archivo V2 después de aplicarlo
**Por qué es un problema:** una computadora ya pudo ejecutar la versión anterior, mientras otra recibe el archivo editado. Los equipos dejan de tener el mismo historial.

**Qué hacer:** dejar V2 como registro de lo que ocurrió y preparar V3 para corregir o ampliar el cambio. En un equipo real, avisar y coordinarlo con quienes mantienen la base de datos.

### Error 4: creer que Flyway es un respaldo
**Por qué es un problema:** Flyway registra y ejecuta cambios; su historial no es una copia de todos los pedidos.

**Qué hacer:** usar una política de respaldos y recuperación independiente, y ensayar los cambios antes de producción.

### Error 5: pensar que todo cambio se puede deshacer con un botón
**Por qué es un problema:** quitar un campo puede borrar los datos guardados en él. Restaurar un respaldo antiguo también podría perder pedidos nuevos.

**Qué hacer:** planear la recuperación según el cambio. A veces es más seguro crear una nueva migración que corrija los datos, en vez de borrar lo que se acaba de agregar.

## 8. Cómo se relaciona con la arquitectura
La base de datos forma parte del sistema y también cambia con el tiempo. Una decisión de arquitectura debe considerar no solo cómo se organiza el programa, sino cómo se guardan y protegen los datos cuando el programa evoluciona.

Un archivo de migración deja evidencia de una decisión concreta: “a partir de este cambio, cada pedido puede tener un estado de entrega”. Su historial ayuda a que el equipo pueda reconstruir qué cambios se hicieron y preparar otros entornos de la misma manera.

Flyway aporta orden, pero no toma las decisiones del negocio. El equipo todavía debe decidir qué significa cada estado, qué hacer con los pedidos antiguos y cómo verificar que el sistema continúa funcionando.

## 9. Actividad guiada: agregar el teléfono de contacto
Una plataforma logística quiere guardar un teléfono para avisar al cliente sobre una entrega. Resuelve el caso en papel o en una tabla; no necesitas programar.

### Parte 1: entender la necesidad
1. ¿Quién necesita el teléfono y para qué lo usará?
2. ¿El teléfono es obligatorio para todos los pedidos o solo para algunos?
3. ¿Qué debería ocurrir con los pedidos antiguos que no tienen teléfono?

### Parte 2: planear el cambio
4. Describe con una frase qué nueva información se guardará.
5. Propón un nombre de archivo de migración que siga a `V1__Crear_pedidos.sql`.
6. Anota tres pruebas que harías en una copia antes de aplicar el cambio real.
7. Explica qué protección prepararías si una prueba falla.

### Parte 3: tomar una decisión responsable
8. ¿Quién podrá ver el teléfono? No es necesario que todas las personas que usan el sistema tengan acceso a él.
9. ¿Qué dato mostrarías si el teléfono falta o no es válido?
10. ¿Qué revisarías después de aplicar la migración?

## 10. Respuesta modelo de la actividad
Una respuesta razonable podría ser:

- Guardaremos el teléfono porque el equipo de entregas necesita contactar al cliente ante un problema. Solo las personas que coordinan esa entrega deberían verlo.
- Los pedidos antiguos no tendrán teléfono si no contamos con un dato confiable. No inventaremos uno ni impediremos consultar el pedido por esa razón.
- El archivo podría llamarse `V2__Agregar_telefono_contacto.sql`, siempre que V2 sea la siguiente versión libre del proyecto.
- En una copia comprobaríamos que los pedidos antiguos siguen abriendo, que se puede guardar un teléfono para un pedido nuevo y que la aplicación funciona cuando el teléfono está vacío.
- Antes de aplicar el cambio real confirmaríamos el respaldo y el plan para detenernos si una prueba falla.
- Después revisaríamos que se guarde el dato correcto y que solo las personas autorizadas puedan verlo.

Esta no es la única respuesta posible. Lo importante es explicar qué problema se resuelve, cómo se protegen los datos existentes y cómo sabremos si el cambio funcionó.

## 11. Lista de comprobación
Antes de considerar listo tu plan de migración, comprueba:

- ¿Entendemos por qué se necesita este dato o cambio?
- ¿Sabemos qué programas y personas usan la información actual?
- ¿Decidimos qué pasará con los registros antiguos?
- ¿El archivo tiene una versión y una descripción claras?
- ¿Probamos tanto la base de datos como el programa que la utiliza?
- ¿Comprobamos los resultados con datos representativos?
- ¿Tenemos respaldo y una respuesta acordada si algo falla?
- ¿El archivo ya aplicado se conserva sin editar?

No todas las migraciones necesitan el mismo nivel de preparación. Cuanto más importante sea la información y mayor sea el impacto de una falla, más cuidadosa debe ser la revisión.

## 12. Comprueba tu comprensión
Responde sin volver a leer las secciones anteriores y después revisa las respuestas:

1. ¿Qué trabajo hace Flyway y qué decisión debe tomar el equipo?
2. ¿Qué podría ocurrir si agregas un campo obligatorio sin pensar en los pedidos antiguos?
3. ¿El registro de Flyway es un respaldo de los pedidos?
4. ¿Por qué no conviene editar un archivo de migración que ya se aplicó en otros entornos?

### Respuestas para revisar
1. Flyway aplica en orden los cambios preparados y registra cuáles ya ejecutó. El equipo decide qué información necesita el negocio y cómo tratar los datos existentes.
2. Los pedidos antiguos podrían quedar incompletos o la aplicación podría dejar de leerlos correctamente.
3. No. Flyway registra cambios en la estructura; un respaldo conserva una copia de los datos.
4. Distintos entornos podrían tener versiones diferentes del mismo cambio. Se conserva el archivo aplicado y se crea uno nuevo para corregirlo.

Si puedes explicar estas respuestas con tus propias palabras y completar la actividad del teléfono, ya comprendiste la idea central. Si no, vuelve al ejemplo de pedidos antiguos y sigue qué cambia antes, durante y después de la migración.

## Cierre
Una migración es un cambio planificado en la forma de guardar o interpretar información. Flyway ayuda a aplicar los cambios en orden y deja constancia de cuáles ya se hicieron. Para que el cambio sea seguro, las personas deben entender qué información existe, decidir cómo tratar los datos antiguos, probar el resultado y proteger la información real.

La idea que queremos conservar es esta: **no cambiamos una base de datos solo porque podemos agregar un campo; la cambiamos porque hay una necesidad, y comprobamos que el cambio cuida tanto los datos de hoy como el trabajo de mañana.**

## Preguntas para llevarse
- ¿Qué parte del ejemplo te ayudó a entender qué hace Flyway?
- ¿Por qué un dato “Por confirmar” puede ser más honesto que inventar un estado?
- ¿Qué diferencia hay entre el registro de Flyway y un respaldo?
- ¿Qué comprobarías antes de permitir que el cambio llegue a los pedidos reales?
