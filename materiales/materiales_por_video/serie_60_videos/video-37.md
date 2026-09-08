# Video 37: Agentes de IA revisando código en GitHub

## Título
Agentes de IA revisando código en GitHub

## 🧭 Ficha de la clase
- **Actividad relacionada:** Actividad 4: implementación e integración
- **Duración sugerida:** 45 a 60 minutos
- **Modalidad:** explicación dialogada, ejemplo resuelto, taller y retroalimentación
- **Producto:** una evidencia que se incorpora al repositorio del proyecto

## 🎯 Propósito de aprendizaje
Al finalizar esta clase, quiero que puedas construir un flujo ejecutable que conecte entrada, aplicación, dominio e infraestructura usando el caso de la plataforma logística. No quiero que memorices una definición para repetirla: quiero que aprendas a reconocer el problema, argumentar una decisión y anticipar sus consecuencias.

## 🎬 Apertura: pensemos como arquitectos
Bienvenido a esta clase. Hoy no voy a pedirte que empieces por un diagrama ni por una tecnología. Quiero que empecemos por una situación que podría ocurrir en un sistema real.

Antes de entrar en agentes de ia revisando código en github, deténgase en el problema que lo hace necesario. En arquitectura no aprendemos una palabra para repetirla en un diagrama; aprendemos a reconocer una situación, analizar alternativas y tomar una decisión defendible.

Mientras lees, imagina que estamos frente a una pizarra. Yo te pregunto: ¿qué está pasando?, ¿quién depende de que esto funcione?, ¿qué información nos falta? No respondas todavía con nombres de herramientas. Primero cuéntame qué problema ves.

Antes de continuar, detente un momento y responde: ¿quién usa el sistema?, ¿qué espera que ocurra?, ¿qué no puede fallar?, ¿qué cambio es probable durante la vida del producto? Yo prefiero que lleguemos a estas preguntas antes de mencionar un framework. Si todavía no podemos responderlas, no pasa nada: acabamos de descubrir qué necesitamos investigar antes de diseñar.

## 💬 Pregunta central
¿Qué problema real resuelve agentes de ia revisando código en github y cómo demostraríamos que la solución es adecuada?

## 🧠 Desarrollo de la clase
### 1. Describir el problema antes de diseñar
Ahora déjame mostrarte el primer movimiento. Cuando un equipo recibe una solicitud, suele saltar a la solución: "usemos microservicios", "hagamos una API" o "guardemos todo en una base de datos". Yo quiero que hoy invirtamos ese orden. Primero vamos a describir el comportamiento que el negocio necesita, las personas afectadas, las restricciones y los riesgos. Una decisión arquitectónica solo tiene sentido dentro de ese contexto.

Mira el caso logístico: asignar una ruta implica inventario, ubicación del repartidor, promesa de entrega, tráfico, costo operativo y comunicación. Si tratamos todo como una sola operación, luego será difícil saber qué probar, qué escalar y qué recuperar cuando ocurra un fallo. Aquí aparece la primera lección: antes de diseñar componentes, necesitamos entender las responsabilidades.

### 2. Separar hechos, supuestos y decisiones
Ahora hagamos una pausa. Un hecho es algo observable. Un supuesto es una afirmación que aún necesita validación. Una decisión es una elección entre alternativas. Por ejemplo, "tendremos 10 000 pedidos diarios" puede ser una estimación; "la API de mapas siempre responderá en menos de un segundo" es un supuesto; "aislaremos el proveedor mediante un adaptador" es una decisión. Cada elemento necesita una evidencia distinta. Si mezclamos estas tres cosas, terminaremos defendiendo opiniones como si fueran datos.

### 3. Hacer visibles las consecuencias
Llegamos al punto que más me interesa. No existe una alternativa gratuita. Una solución puede reducir el tiempo inicial y aumentar el costo de operación; otra puede mejorar la mantenibilidad y exigir más diseño; otra puede aumentar la disponibilidad y complicar la consistencia. Cuando yo te pida justificar una arquitectura, no quiero escuchar que una opción es "mejor". Quiero que me expliques qué gana, qué pierde y qué riesgo estamos aceptando.

Agentes de IA revisando código en GitHub se entiende mejor cuando lo conectamos con esta secuencia: contexto, alternativas, decisión, consecuencias y evidencia. Si falta uno de esos pasos, la propuesta queda incompleta.

## ❓ Preguntas del profesor durante la explicación
- ¿Qué parte del problema pertenece realmente a agentes de ia revisando código en github?
- ¿Qué supuesto estamos haciendo y cómo podríamos comprobarlo?
- ¿Qué costo aceptamos al elegir esta alternativa?
- ¿Qué ocurriría si el volumen se multiplica o una dependencia deja de responder?

No leas estas preguntas como un examen. Son las preguntas que yo usaría mientras conversamos frente a la pizarra. Si todavía no tienes una respuesta, anótala como una duda de diseño. Una duda bien formulada es más útil que una respuesta rápida y débil.

## 💡 Ideas esenciales
- Un flujo vertical conecta entrada, aplicación, dominio e infraestructura con límites visibles.
- Los adaptadores aíslan APIs, bases de datos, colas y herramientas de terceros.
- La automatización y la documentación reducen el costo de repetir y verificar el trabajo.
- El ejemplo debe documentarse con sus supuestos, trade-offs y evidencia de validación.

## 🏗️ Ejemplo resuelto
Voy a resolver una situación contigo. En la plataforma logística, un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. Observe qué parte del sistema conoce esa regla, qué información necesita y qué ocurriría si aumenta la carga, falla una dependencia o cambia la política del negocio.

Fíjate en el razonamiento: el problema no es elegir una arquitectura moderna. El problema es mantener la promesa de entrega, proteger la información del cliente y responder ante cambios sin detener la operación. Desde ahí comparamos alternativas y explicamos por qué una es adecuada para este momento. Si cambian los datos del contexto, también puede cambiar nuestra decisión; eso no es una contradicción, es buena arquitectura.

## 🧩 Caso guiado: plataforma logística
Ahora te propongo que caminemos juntos por el flujo. En cada paso voy a pedirte que preguntes qué regla se protege, quién tiene la responsabilidad y qué pasa si falla:

1. Un cliente crea un pedido.
2. El sistema valida los datos y reserva inventario.
3. El módulo de ruteo propone una asignación.
4. La plataforma comunica el estado al cliente y al repartidor.
5. Un incidente puede exigir reintento, compensación o intervención humana.

Haz una pausa después de cada paso y escribe: ¿qué puede salir mal?, ¿qué componente debe enterarse?, ¿qué información cruza el límite?, ¿qué decisión evita que el error se propague? No avances hasta tener una hipótesis. En arquitectura aprendemos pensando sobre las consecuencias, no pasando rápidamente por los títulos.

## ✍️ Taller de clase
Ahora te entrego la palabra. Entra en el papel de arquitecto o arquitecta. Parte del caso: un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. No quiero una respuesta decorativa; quiero acompañarte mientras construyes el razonamiento. Trabaja así:

1. Redacta el problema en tres líneas, sin mencionar tecnologías.
2. Identifica tres actores y qué esperan del sistema.
3. Propón dos alternativas razonables.
4. Compáralas por costo inicial, calidad, riesgo y facilidad de cambio.
5. Elige una para el MVP y declara qué condición obligaría a revisarla.
6. Produce un diagrama, tabla, ADR o fragmento de código que haga visible la decisión.

Cuando termines, vuelve a leer tu propuesta como si fueras un compañero que llega hoy al proyecto. ¿Entendería por qué elegiste esa alternativa? ¿Sabría qué riesgo aceptaste? No busques "la respuesta que yo daría". Quiero que construyas una respuesta propia. Puede ser diferente y seguir siendo correcta si presenta evidencia, reconoce sus costos y explica sus límites. Yo revisaré tres cosas: que delimites el problema, que compares alternativas reales y que hagas visibles sus consecuencias.

### 🔎 Retroalimentación esperada
Cuando revise tu trabajo, no buscaré una frase elegante ni un diagrama lleno de cajas. Buscaré una decisión que pueda seguirse. Una evidencia madura no dice "elegimos X porque es mejor". Dice: "elegimos X porque priorizamos A y B; aceptamos C; descartamos Y por el riesgo D; verificaremos mediante E". Esa forma de escribir convierte una conversación técnica en conocimiento reutilizable.

La evidencia mínima debe incluir contexto, decisión, alternativa descartada, dos consecuencias y una forma de verificación. Guárdala en la carpeta correspondiente a Actividad 4: implementación e integración.



## ⚠️ Errores frecuentes
- Confundir el nombre del tema con una explicación de cómo agentes de ia revisando código en github afecta el sistema.
- Elegir una herramienta antes de describir el problema y sus restricciones.
- Presentar una solución como universal sin explicar cuándo dejaría de ser adecuada.
- Omitir la evidencia, prueba o métrica que permitiría revisar la decisión.

## ✅ Cierre: lo que te llevas de esta clase
Hemos llegado al final. Antes de cerrar, imagina que yo te doy dos minutos frente al equipo. Quiero escucharte defender tu decisión: empieza por el problema, describe el contexto, compara las alternativas, explica tu elección y termina con el trade-off y la evidencia que la respalda. No intentes sonar complicado; intenta ser claro. Si otra persona puede entender tu decisión sin haber estado en esta conversación, has hecho un buen trabajo.

Quédate con esta idea: diseñar arquitectura no es adivinar el futuro ni encontrar una solución perfecta. Es tomar una decisión responsable con la información disponible, reconocer lo que todavía no sabemos y preparar el sistema para aprender y cambiar. Cada vez que documentas un supuesto, nombras un riesgo o explicas un costo, estás actuando como arquitecto.

Ahora mira tu propia propuesta y pregúntate: ¿qué parte defendería con confianza?, ¿qué parte necesita evidencia?, ¿qué cambiaría si el negocio creciera mañana? Esa pregunta es el puente hacia la siguiente clase.

## 🧪 Comprobación de aprendizaje
- ¿Puedes explicarme el problema sin mencionar primero una tecnología?
- ¿Puedes defender la comparación entre dos alternativas con criterios concretos?
- ¿Puedes decirme qué cambiaría ante un nuevo requisito o un fallo?
- ¿Puedes mostrarme qué evidencia respaldaría o refutaría tu decisión?

## 🤔 Preguntas para reflexión
- ¿Dónde empieza y termina el caso de uso?
- ¿Qué ocurre si la dependencia externa falla?
- ¿Cómo se puede ejecutar y verificar el flujo en otro entorno?

## 🗣️ Respuestas orientadoras

No quiero que memorices estas respuestas como si fueran una clave de examen. Úsalas para comparar tu razonamiento. Si tu respuesta es diferente, debe explicar el contexto, el costo y la evidencia que la sostiene.

1. **¿Qué problema resuelve esta clase?**  En este caso, un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado. El problema arquitectónico consiste en organizar responsabilidades y decisiones para que ese resultado sea posible sin perder calidad, trazabilidad ni capacidad de cambio.
2. **¿Qué supuesto debemos comprobar?**  Debemos comprobar los datos que condicionan la decisión: volumen, tiempos de respuesta, disponibilidad de dependencias, reglas del negocio y capacidad real del equipo. No debemos tratar una estimación como un hecho.
3. **¿Qué costo aceptamos?**  La alternativa elegida siempre sacrifica algo. Podemos aceptar más trabajo inicial para ganar mantenibilidad, o aceptar una solución más sencilla para reducir el costo del MVP. Lo importante es declarar el intercambio y ponerle una condición de revisión.
4. **¿Qué pasa si falla una dependencia?**  El sistema debe tener una respuesta definida: timeout, reintento controlado, degradación, compensación, cola de mensajes o intervención humana. Decir solamente “el sistema falla” no es una estrategia arquitectónica.
5. **¿Qué evidencia demostraría que la decisión funciona?**  Depende del tema: una métrica, una prueba, un contrato, un diagrama revisado, un registro de ejecución o una demostración del flujo. La evidencia debe corresponder al riesgo que queremos controlar.

En resumen, la respuesta correcta no es el nombre de una tecnología. Es una relación clara entre problema, decisión, consecuencia y evidencia.

## 🛠️ Solución modelo de la actividad

Esta es una resolución de referencia para que puedas comparar tu trabajo.

### 🔹 Paso 1. Delimitar el problema
La plataforma necesita procesar pedidos y asignar entregas de forma trazable. El riesgo principal es que una decisión local, como cambiar el ruteo, rompa inventario, notificaciones o la promesa de entrega. Por eso debemos establecer límites antes de implementar.

### 👥 Paso 2. Identificar actores y necesidades
- **Cliente:** espera crear el pedido y recibir estados confiables.
- **Operador logístico:** necesita visualizar incidentes y corregir asignaciones.
- **Repartidor:** necesita una ruta actualizada y una instrucción clara.
- **Equipo de desarrollo y operación:** necesita modificar, probar y observar el sistema sin afectar todo el flujo.

### 🔀 Paso 3. Proponer alternativas
- **Alternativa A:** una aplicación única con módulos internos para pedidos, inventario, ruteo y notificaciones.
- **Alternativa B:** separar los módulos críticos mediante servicios o eventos con contratos explícitos.

### ⚖️ Paso 4. Comparar consecuencias
La alternativa A reduce el costo inicial y simplifica el despliegue, pero exige disciplina para proteger los límites internos. La alternativa B permite aislar y escalar partes por separado, pero agrega latencia, monitoreo, despliegues y problemas de consistencia. No conviene elegir B solo porque suena más moderna.

### ✅ Paso 5. Tomar una decisión para el MVP
La decisión inicial recomendada es comenzar con un monolito modular, mantener puertos claros y preparar adaptadores para las integraciones externas. Esta opción reduce el costo operativo mientras conserva una ruta de evolución. Revisaremos la decisión si el volumen, la disponibilidad o la autonomía de un módulo justifican separarlo.

### 🧪 Paso 6. Definir la verificación
Verificaremos la solución con una prueba del flujo de creación de pedido, una prueba de fallo del proveedor de mapas, una métrica de tiempo de respuesta y una revisión de dependencias entre módulos. Si el resultado no cumple el escenario acordado, revisaremos la decisión.

### 📦 Paso 7. Preparar la entrega
Guarda en GitHub el problema, los actores, la comparación, la decisión, los trade-offs, el diagrama o código y las pruebas. En el video de sustentación explica qué elegiste, qué descartaste, qué riesgo aceptaste y cómo sabrás si debes cambiarlo.


## 🚀 Preparación para la siguiente clase
Revisa la evidencia, registra los supuestos aún no validados y lleva una pregunta abierta sobre costo, calidad, dependencia o evolución. Cada clase debe agregar una pieza al expediente arquitectónico.
