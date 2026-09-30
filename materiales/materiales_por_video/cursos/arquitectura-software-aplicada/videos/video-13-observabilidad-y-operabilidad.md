# Video 13: Métricas cuantitativas para evaluar arquitecturas limpias

## Para empezar
No necesitas saber programar para seguir la idea principal de este video. Vamos a aprender a hacer una pregunta sencilla: **¿cómo podemos comprobar, con datos, si la organización de un sistema se está volviendo más fácil o más difícil de cambiar?**

Imagina una cocina de restaurante. Si la persona que prepara los platos también tiene que atender el teléfono, cobrar, lavar los platos y comprar los ingredientes, cualquier cambio se vuelve complicado. En un programa puede pasar algo parecido: una misma parte del sistema termina haciendo demasiadas tareas o depende de demasiadas otras partes.

Una **métrica** es una forma de contar o medir algo para comparar. Por ejemplo, contar cuántas veces una condición importante no se cumple. El número no explica toda la historia, pero nos ayuda a saber dónde mirar.

## ¿Qué significa arquitectura limpia?
La **arquitectura** es la manera en que se organizan las partes de un programa y cómo se comunican entre ellas.

En una arquitectura limpia, las reglas importantes del negocio no deberían depender de detalles que pueden cambiar, como la marca de la base de datos, una página web o un servicio externo. Si mañana cambiamos la base de datos, la regla “una entrega no se asigna a un repartidor que no está disponible” debería seguir funcionando.

Piensa en una receta: indica qué resultado queremos preparar, pero no debería depender de una marca concreta de horno. En el programa, las condiciones del negocio son como los pasos de la receta; la base de datos y las pantallas son herramientas que ayudan a ponerlas en práctica.

### ¿Qué quiero decir con “regla”?
En esta clase usamos la palabra de dos maneras distintas:

- **Regla del negocio:** una condición que el sistema debe respetar para hacer bien su trabajo. Ejemplo: “No asignar una entrega a un repartidor que no está disponible”.
- **Regla de organización:** una indicación sobre cómo se conectan las partes del programa. Ejemplo: “La parte que decide a quién asignar una entrega no consulta directamente la base de datos”.

La primera protege el resultado correcto para el negocio. La segunda ayuda a que el programa sea más fácil de cambiar y probar. En las tablas, cada fila dirá cuál de las dos estamos revisando.

## ¿Qué vamos a medir?
No intentaremos medir “si la arquitectura es buena” con un único número. Miraremos señales pequeñas que nos ayuden a encontrar problemas concretos.

### 1. ¿Se está respetando una regla de organización?
Supongamos que acordamos esta regla de organización: “La parte que decide a quién asignar una entrega no debe consultar directamente la base de datos”. Podemos revisar el programa y contar cuántas conexiones directas hay.

Ese conteo es una métrica sencilla:

- Antes de corregir: encontramos 2 conexiones directas que no deberían existir.
- Después de corregir: encontramos 0 conexiones directas.

Esto no prueba que todo el programa sea perfecto. Sí nos dice que esa indicación sobre cómo se conectan sus partes se respeta en los lugares que revisamos.

### 2. ¿Cuántas otras partes necesita una regla para funcionar?
Si la parte del programa que aplica una condición del negocio necesita pedir ayuda a muchas otras partes, puede ser más difícil cambiarla o probarla. A esta cantidad de conexiones entre partes se le llama **acoplamiento**.

Por ahora basta con recordar esta idea: más conexiones no siempre significan un problema, pero cada conexión puede hacer que un cambio afecte a más lugares. Podemos contar cuántas partes necesita consultar la decisión de asignar una entrega y comparar ese número después de un cambio.

### 3. ¿Cuántas decisiones distintas hay en una tarea?
Una instrucción que contiene muchas condiciones, como “si pasa esto, haz aquello; si no, revisa esto otro”, puede resultar difícil de entender y comprobar. Las herramientas pueden contar algunos de esos caminos. Ese número se conoce como **complejidad**.

Un número alto no significa automáticamente que el código esté mal. Es una invitación a leer esa parte con atención: ¿hay varias condiciones del negocio mezcladas?, ¿se puede explicar qué hace cada una?, ¿podemos comprobarlas por separado?

### 4. ¿Podemos comprobar la regla sin encender todo el sistema?
También podemos observar cuánto necesitamos preparar para comprobar una condición del negocio. Si para revisar la asignación de una entrega debemos iniciar la página web, la base de datos y otros servicios, la prueba cuesta más. Si podemos revisar la decisión por separado, es más sencillo repetir la comprobación.

Esto no significa que nunca debamos probar el sistema completo. Significa que algunas preguntas se pueden responder de manera más rápida y sencilla antes de hacer una prueba grande.

## Un ejemplo paso a paso: asignar una entrega
La plataforma logística debe elegir un repartidor para cada pedido. Debe comprobar que la persona esté disponible y que no supere su capacidad.

### Situación inicial
La decisión de elegir al repartidor está mezclada con el código que consulta la base de datos. Para comprobar que se elige a alguien disponible y con capacidad, el equipo tiene que preparar una base de datos aunque solo quiera revisar una decisión sencilla.

Imaginemos que revisamos esta parte y encontramos lo siguiente. Son números de ejemplo para aprender a comparar, no resultados medidos en un sistema real:

| Qué revisamos | Antes del cambio |
|---|---:|
| Conexiones directas entre la decisión de asignar y la base de datos | 1 |
| Elementos que preparamos para probar la decisión | 3 |
| Condiciones del negocio comprobadas (disponibilidad y capacidad) | 2 |

### ¿Qué queremos mejorar?
Queremos que la decisión de asignación pueda determinar si el repartidor es adecuado sin tener que conocer cómo se guardan los datos. La base de datos seguirá existiendo; simplemente dejaremos que otra parte del programa se encargue de consultarla.

La nueva conexión funciona como pedir información a un compañero: la regla pregunta “¿quién está disponible?” y recibe una respuesta. No necesita saber dónde se guarda la información ni cómo se hizo la consulta.

### ¿Cómo comprobamos el resultado?
Después del cambio, repetimos las mismas preguntas:

| Qué revisamos | Antes | Después, en este ejemplo |
|---|---:|---:|
| Conexiones directas entre la decisión de asignar y la base de datos | 1 | 0 |
| Elementos que preparamos para probar la decisión | 3 | 1 |
| Condiciones del negocio comprobadas (disponibilidad y capacidad) | 2 | 2 |

La última fila importa: además de cambiar cómo se conectan las partes del programa, revisamos que sigan cumpliéndose las dos condiciones del negocio: que el repartidor esté disponible y que tenga capacidad. Una arquitectura mejor organizada no sirve si ahora asigna entregas incorrectamente.

### ¿El cambio fue bueno?
Los números sugieren que ahora es más fácil probar la decisión de asignación y que esta ya no consulta directamente la base de datos. También agregamos una pieza nueva que el equipo tendrá que mantener. Por eso no hacemos cambios solo para bajar un número: comprobamos que el problema era real y que la solución no complicó más de lo necesario.

## Cómo leer una métrica sin confundirse
Una métrica es como la temperatura de un paciente: aporta información, pero no explica por sí sola qué está ocurriendo ni cuál es el tratamiento correcto.

- Pregunta primero qué problema quieres entender.
- Cuenta siempre lo mismo antes y después para que la comparación sea justa.
- Revisa el código o los resultados y pregúntate qué significan; si falta contexto, anótalo como algo que debes investigar.
- Comprueba que el programa sigue dando las respuestas correctas.
- No compares partes que hacen trabajos muy distintos como si fueran iguales.
- No intentes mejorar el número si eso vuelve el programa más difícil de entender.

No existe un número universal que diga cuándo un programa está bien organizado. Cada equipo puede acordar señales y límites para su proyecto, explicar por qué los eligió y cambiarlos cuando cambien las necesidades.

## Ejercicio de autoestudio
Trabaja con este ejemplo aunque todavía no conozcas herramientas de programación. Puedes responder con dibujos, una tabla o frases sencillas.

1. **Elige una condición del negocio:** por ejemplo, “no asignar una entrega a alguien que no está disponible”.
2. **Explica qué podría salir mal:** ¿qué ocurriría si la decisión de asignar queda mezclada con la consulta a la base de datos?
3. **Decide qué contarías:** ¿conexiones directas con la base de datos?, ¿elementos que hay que preparar para probar?, ¿condiciones del negocio comprobadas?
4. **Anota un resultado inicial:** usa los números del ejemplo o inventa unos para practicar; aclara que son supuestos.
5. **Propón un cambio:** describe con palabras cómo separarías la decisión de asignar de la herramienta que guarda los datos.
6. **Vuelve a comprobar:** compara los números y confirma que la entrega todavía se asigna correctamente.
7. **Explica tu decisión:** ¿qué mejoró?, ¿qué nueva dificultad apareció?, ¿mantendrías el cambio?

### Ejemplo de respuesta
Una respuesta posible es proteger esta condición: “La decisión de asignar una entrega no consulta directamente la base de datos”. En el ejemplo de la clase, contaríamos una conexión directa antes del cambio y ninguna después. También revisaríamos que las dos condiciones del negocio —disponibilidad y capacidad— sigan comprobándose.

Los números de práctica no demuestran por sí solos que el diseño sea bueno. La decisión tiene sentido si separar la consulta permite comprobar la regla con menos preparación y no añade una capa que nadie necesita.

## Comprueba tu comprensión
- Si la decisión de asignar necesita muchas otras partes para funcionar, ¿qué cambios podrían volverse difíciles?
- ¿Por qué contar conexiones no basta para afirmar que un programa es bueno o malo?
- Si una prueba es rápida, pero revisa una condición equivocada, ¿nos sirve el resultado?
- ¿Qué cambiarías primero para que la asignación de entregas sea más fácil de entender?

### Respuestas para revisar
- Muchos cambios podrían afectar a varias partes a la vez, aunque eso debe confirmarse mirando sus responsabilidades.
- Un conteo muestra una señal, pero no explica si la conexión es dañina ni si el diseño protege el negocio.
- No. Una prueba rápida que comprueba una condición equivocada no demuestra que la regla correcta funcione.
- Una opción es separar la decisión de asignación de la consulta a la base de datos y probar disponibilidad y capacidad por separado.

## Conclusión
Medir una arquitectura no consiste en sacar una nota definitiva al programa. Consiste en observar una parte concreta, hacer una comparación justa y usar el resultado para decidir qué investigar. Primero entendemos el problema; luego contamos; finalmente comprobamos que el cambio ayuda sin dejar de cumplir las condiciones del negocio.
