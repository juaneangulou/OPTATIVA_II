# Video 18: Seguridad, datos sensibles y privacidad

## Título
Seguridad, datos sensibles y privacidad

## 🧭 Ficha de la clase
- **Actividad relacionada:** Actividad 3: diseño y dominio
- **Duración sugerida:** 45 a 60 minutos
- **Modalidad:** explicación dialogada, ejemplo resuelto, taller y retroalimentación
- **Producto:** una evidencia que se incorpora al repositorio del proyecto

## 🔗 Continuidad de la ruta
Vienes de trabajar observabilidad y monitoreo de sistemas. No vamos a repetirlo: lo usaremos como punto de partida para estudiar seguridad, datos sensibles y privacidad y añadir una decisión nueva al expediente.

Lo que construyas aquí será la base para la próxima conversación: testing y validación de arquitectura.

## 🎥 Escena de hoy
Hoy te encuentras ante esta situación: Este video refuerza la idea de que la seguridad debe integrarse desde el inicio del diseño. No se trata solo de proteger la aplicación frente a intrusos, sino también de gestionar adecuadamente datos sensibles, permisos de acceso y riesgos derivados del tratamiento de información. Cualquier sistema que maneje datos valiosos debe diseñarse con principios de privacidad, control y minimización.

La arquitectura debe prestar atención a qué información guarda, cómo la protege y quién puede acceder a ella. Cuando se ignora esto, se generan riesgos reales tanto para la empresa como para las personas que usan el sistema. El equipo te pide una decisión sobre seguridad, datos sensibles y privacidad, pero todavía no existe una respuesta única. Tu primera pista es esta idea de la fuente: La seguridad debe estar integrada al diseño, no añadida al final.

## 🧭 Reto de la clase
Tu reto consiste en convertir esa idea en una decisión concreta: qué harías, qué dejarías fuera del alcance y cómo demostrarías que funciona.

## 🎯 Propósito de aprendizaje
Cuando terminemos, quiero que puedas proteger las reglas del negocio dentro de un modelo claro y comprobable usando el caso de la plataforma logística. No te voy a pedir que repitas una definición. Te voy a pedir que mires una situación, me expliques qué está en juego, tomes una decisión y me digas qué consecuencias esperas.

## 🎬 Apertura: pensemos como arquitectos
Bienvenido a esta clase. Hoy no voy a pedirte que empieces por un diagrama ni por una tecnología. Quiero que empecemos por una situación que podría ocurrir en un sistema real.

Antes de entrar en seguridad, datos sensibles y privacidad, quiero que escuchemos primero la idea central de la fuente del curso: Este video refuerza la idea de que la seguridad debe integrarse desde el inicio del diseño. No se trata solo de proteger la aplicación frente a intrusos, sino también de gestionar adecuadamente datos sensibles, permisos de acceso y riesgos derivados del tratamiento de información. Cualquier sistema que maneje datos valiosos debe diseñarse con principios de privacidad, control y minimización.

La arquitectura debe prestar atención a qué información guarda, cómo la protege y quién puede acceder a ella. Cuando se ignora esto, se generan riesgos reales tanto para la empresa como para las personas que usan el sistema. En arquitectura no aprendemos una palabra para repetirla en un diagrama; aprendemos a reconocer una situación, analizar alternativas y tomar una decisión defendible.

Imagina que estamos frente a una pizarra. Yo te miro y te pregunto: ¿qué está pasando?, ¿quién depende de que esto funcione?, ¿qué información nos falta? No me respondas todavía con nombres de herramientas. Primero cuéntame qué problema ves. Esa primera respuesta me permite saber si estamos entendiendo el sistema o si solo estamos repitiendo soluciones conocidas.

Antes de continuar, haz una pausa conmigo. ¿Quién usa el sistema? ¿Qué espera que ocurra? ¿Qué no puede fallar? ¿Qué cambio es probable durante la vida del producto? Te hago estas preguntas porque una arquitectura no se diseña en el vacío. Si todavía no puedes responderlas, no es un problema: acabamos de encontrar la información que necesitamos investigar antes de diseñar.

## 💬 Pregunta central
¿Qué problema real resuelve seguridad, datos sensibles y privacidad y cómo demostraríamos que la solución es adecuada?

## 🧠 Desarrollo de la clase
### Lo que trae la fuente del curso
La fuente describe este tema así: Este video refuerza la idea de que la seguridad debe integrarse desde el inicio del diseño. No se trata solo de proteger la aplicación frente a intrusos, sino también de gestionar adecuadamente datos sensibles, permisos de acceso y riesgos derivados del tratamiento de información. Cualquier sistema que maneje datos valiosos debe diseñarse con principios de privacidad, control y minimización.

La arquitectura debe prestar atención a qué información guarda, cómo la protege y quién puede acceder a ella. Cuando se ignora esto, se generan riesgos reales tanto para la empresa como para las personas que usan el sistema.

Yo voy a traducir esa idea a una situación de diseño. No quiero que la recibas como una definición cerrada; quiero que observes qué problema intenta resolver, qué decisiones implica y qué evidencia necesitaríamos para confiar en ella.

### 1. Escuchemos la fuente y llevémosla al sistema
Quiero que empecemos por la afirmación que trae la fuente: La seguridad debe estar integrada al diseño, no añadida al final. Si la tomamos en serio, seguridad, datos sensibles y privacidad deja de ser una etiqueta y se convierte en una decisión que debemos observar en el sistema.

Ahora conectemos esa afirmación con la siguiente: Los datos sensibles requieren más criterios de control y protección. Pregúntate qué componente, actor o regla del negocio queda afectado. No me interesa que repitas la frase; me interesa que puedas señalar dónde aparece en el caso logístico.

La tercera conversación es sobre las consecuencias: La privacidad es parte del valor del sistema.. Aquí es donde una propuesta deja de ser teórica. Dime qué ganamos, qué sacrificamos y qué evidencia nos permitiría revisar la elección.

Finalmente, la fuente añade: Un sistema debe minimizar exposición de información innecesaria. Esta idea nos ayuda a completar el análisis y a evitar una solución parcial. Cuando terminemos, deberás poder relacionar este principio con una decisión concreta del proyecto.

Mientras avanzamos, separa tres cosas: lo que la fuente afirma, lo que el caso logístico necesita y lo que tú decides hacer. Esa separación evita que una explicación general se convierta en una receta automática.

## ❓ Preguntas del profesor durante la explicación
- **Te pregunto:** ¿Qué datos sensibles maneja mi sistema? **La razón:** así conectamos el tema con el problema real en lugar de aplicarlo por moda.
- **Te pregunto:** ¿qué supuesto estamos haciendo y cómo podríamos comprobarlo? **La razón:** una decisión basada en una suposición no validada puede fallar en producción.
- **Te pregunto:** ¿qué costo aceptamos al elegir esta alternativa? **La razón:** toda arquitectura gana algo y renuncia a otra cosa.
- **Te pregunto:** ¿qué ocurriría si el volumen se multiplica o una dependencia deja de responder? **La razón:** una solución se demuestra cuando conocemos sus límites.

Estas no son preguntas para atraparte ni para calificarte de inmediato. Son las preguntas que te haría mientras conversamos frente a la pizarra. Si no tienes una respuesta todavía, dime qué dato te falta. En arquitectura, reconocer una duda y saber cómo investigarla demuestra más criterio que responder con seguridad algo que no podemos justificar.

## 💡 Ideas esenciales
- La seguridad debe estar integrada al diseño, no añadida al final.
- Los datos sensibles requieren más criterios de control y protección.
- La privacidad es parte del valor del sistema.
- Un sistema debe minimizar exposición de información innecesaria.
- El diseño debe recordar quién tiene acceso y bajo qué condiciones.
- La confianza del usuario depende del manejo responsable de datos.
- Las entidades protegen identidad y comportamiento, no solo datos.
- El ejemplo debe documentarse con sus supuestos, trade-offs y evidencia de validación.

### Mi lectura como profesor
La seguridad y la privacidad no son requisitos secundarios: son elementos fundamentales de una arquitectura responsable y confiable.

Cuando conectamos esta conclusión con el proyecto, la pregunta deja de ser "¿conozco el concepto?" y pasa a ser "¿puedo usarlo para tomar una decisión concreta y explicar sus consecuencias?".

## 🏗️ Ejemplo resuelto
Voy a resolver una situación contigo. La fuente plantea lo siguiente: Este video refuerza la idea de que la seguridad debe integrarse desde el inicio del diseño. No se trata solo de proteger la aplicación frente a intrusos, sino también de gestionar adecuadamente datos sensibles, permisos de acceso y riesgos derivados del tratamiento de información. Cualquier sistema que maneje datos valiosos debe diseñarse con principios de privacidad, control y minimización.

La arquitectura debe prestar atención a qué información guarda, cómo la protege y quién puede acceder a ella. Cuando se ignora esto, se generan riesgos reales tanto para la empresa como para las personas que usan el sistema. Ahora llévalo a la plataforma logística: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. Pregúntate qué parte del sistema conoce esa regla, qué información necesita y qué ocurriría si aumenta la carga, falla una dependencia o cambia la política del negocio.

Fíjate en el razonamiento: el problema no es elegir una arquitectura moderna. El problema es mantener la promesa de entrega, proteger la información del cliente y responder ante cambios sin detener la operación. Desde ahí comparamos alternativas y explicamos por qué una es adecuada para este momento. Si cambian los datos del contexto, también puede cambiar nuestra decisión; eso no es una contradicción, es buena arquitectura.

## 🧩 Caso guiado: plataforma logística
Ahora caminemos juntos por el flujo. Yo voy a detenerme en cada paso y te voy a pedir que mires tres cosas: qué regla estamos protegiendo, quién tiene la responsabilidad y qué ocurre si algo falla:

1. Un cliente crea un pedido.
2. El sistema valida los datos y reserva inventario.
3. El módulo de ruteo propone una asignación.
4. La plataforma comunica el estado al cliente y al repartidor.
5. Un incidente puede exigir reintento, compensación o intervención humana.

Después de cada paso, respóndeme: ¿qué puede salir mal?, ¿qué componente debe enterarse?, ¿qué información cruza el límite?, ¿qué decisión evita que el error se propague? No avances deprisa. Quiero que construyas una hipótesis y me expliques por qué la sostienes. Así pasamos de leer arquitectura a practicarla.

## ✍️ Taller de clase
Ahora te entrego la palabra. Entra en el papel de arquitecto o arquitecta. Parte del caso: una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega. No quiero una respuesta decorativa; quiero acompañarte mientras construyes el razonamiento. Trabaja así:

1. Redacta el problema en tres líneas, sin mencionar tecnologías.
2. Identifica tres actores y qué esperan del sistema.
3. Propón dos alternativas razonables.
4. Compáralas por costo inicial, calidad, riesgo y facilidad de cambio.
5. Elige una para el MVP y declara qué condición obligaría a revisarla.
6. Produce un diagrama, tabla, ADR o fragmento de código que haga visible la decisión.

Cuando termines, vuelve a leer tu propuesta como si fueras un compañero que llega hoy al proyecto. ¿Entendería por qué elegiste esa alternativa? ¿Sabría qué riesgo aceptaste? No busques adivinar "la respuesta que yo daría". Quiero que construyas una respuesta propia y que me la puedas defender. Puede ser diferente y seguir siendo correcta si presenta evidencia, reconoce sus costos y explica sus límites. Cuando la revisemos juntos, miraré tres cosas: que hayas delimitado el problema, que compares alternativas reales y que hagas visibles sus consecuencias.

### 🔎 Retroalimentación esperada
Cuando revise tu trabajo, no buscaré una frase elegante ni un diagrama lleno de cajas. Buscaré una decisión que pueda seguirse. Una evidencia madura no dice "elegimos X porque es mejor". Dice: "elegimos X porque priorizamos A y B; aceptamos C; descartamos Y por el riesgo D; verificaremos mediante E". Esa forma de escribir convierte una conversación técnica en conocimiento reutilizable.

Cuando termines, guarda en la carpeta correspondiente a Actividad 3: diseño y dominio el contexto, la decisión, la alternativa descartada, dos consecuencias y una forma de verificación. No lo guardes como un trámite: este documento será la memoria de por qué decidiste construir así el sistema.



## ⚠️ Errores frecuentes
- Confundir el nombre del tema con una explicación de cómo seguridad, datos sensibles y privacidad afecta el sistema.
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
- ¿Qué datos sensibles maneja mi sistema?
- ¿Estoy reduciendo la exposición innecesaria de información?
- ¿Mis controles de acceso y seguridad están alineados con el riesgo real?

## 🗣️ Respuestas orientadoras

Ahora vamos a responder las preguntas que aparecieron durante la clase. No quiero que memorices una respuesta exacta. Quiero que compares mi razonamiento con el tuyo. Si llegaste a otra conclusión, puede ser válida si puedes explicarme el contexto, el costo y la evidencia que la sostiene.

La fuente de este video plantea: Este video refuerza la idea de que la seguridad debe integrarse desde el inicio del diseño. No se trata solo de proteger la aplicación frente a intrusos, sino también de gestionar adecuadamente datos sensibles, permisos de acceso y riesgos derivados del tratamiento de información. Cualquier sistema que maneje datos valiosos debe diseñarse con principios de privacidad, control y minimización.

La arquitectura debe prestar atención a qué información guarda, cómo la protege y quién puede acceder a ella. Cuando se ignora esto, se generan riesgos reales tanto para la empresa como para las personas que usan el sistema.

Fíjate en algo importante: ninguna respuesta depende de pronunciar el nombre de una tecnología. Lo que importa es que puedas unir cuatro cosas: el problema que observaste, la decisión que tomaste, la consecuencia que aceptaste y la evidencia que te permitirá comprobarla. Así quiero que pienses durante todo el curso.

### Cómo responder este tema concreto
1. **Cuando te preguntes: ¿Qué datos sensibles maneja mi sistema?** Mi respuesta de partida sería: relaciona esta pregunta con la idea de que La seguridad debe estar integrada al diseño, no añadida al final. Después busca una evidencia en el caso, no una opinión.
2. **Cuando te preguntes: ¿Estoy reduciendo la exposición innecesaria de información?** Mi respuesta de partida sería: relaciona esta pregunta con la idea de que Los datos sensibles requieren más criterios de control y protección. Después busca una evidencia en el caso, no una opinión.
3. **Cuando te preguntes: ¿Mis controles de acceso y seguridad están alineados con el riesgo real?** Mi respuesta de partida sería: relaciona esta pregunta con la idea de que La privacidad es parte del valor del sistema. Después busca una evidencia en el caso, no una opinión.

## 🛠️ Solución modelo de la actividad

Esta es una resolución de referencia para que puedas comparar tu trabajo.

### 🔹 Paso 1. Delimitar el problema
El tema de esta clase se concreta así: Este video refuerza la idea de que la seguridad debe integrarse desde el inicio del diseño. No se trata solo de proteger la aplicación frente a intrusos, sino también de gestionar adecuadamente datos sensibles, permisos de acceso y riesgos derivados del tratamiento de información. Cualquier sistema que maneje datos valiosos debe diseñarse con principios de privacidad, control y minimización.

La arquitectura debe prestar atención a qué información guarda, cómo la protege y quién puede acceder a ella. Cuando se ignora esto, se generan riesgos reales tanto para la empresa como para las personas que usan el sistema. En el proyecto, el riesgo consiste en aplicar esa idea de forma superficial y terminar con una decisión que no protege el objetivo real. Por eso debemos establecer límites antes de implementar.

### 👥 Paso 2. Identificar actores y necesidades
- **Cliente:** espera crear el pedido y recibir estados confiables.
- **Operador logístico:** necesita visualizar incidentes y corregir asignaciones.
- **Repartidor:** necesita una ruta actualizada y una instrucción clara.
- **Equipo de desarrollo y operación:** necesita modificar, probar y observar el sistema sin afectar todo el flujo.

### 🔀 Paso 3. Proponer alternativas
- **Alternativa A:** resolver el problema dentro de la estructura actual con una regla, módulo, prueba o contrato explícito.
- **Alternativa B:** introducir una separación o mecanismo especializado que atienda el riesgo señalado por la fuente.

### ⚖️ Paso 4. Comparar consecuencias
La alternativa A reduce el costo inicial y conserva simplicidad, pero puede dejar expuesto el riesgo principal de seguridad, datos sensibles y privacidad. La alternativa B ofrece una protección más explícita, pero agrega trabajo, dependencias o complejidad operativa. No conviene elegir B solo porque suena más moderna; debe responder a la evidencia del caso.

### ✅ Paso 5. Tomar una decisión para el MVP
Para el MVP, recomiendo elegir la alternativa que proteja primero esta idea de la fuente: La seguridad debe estar integrada al diseño, no añadida al final.. Declara qué complejidad estás aceptando y qué señal te obligaría a cambiar la decisión.

### 🧪 Paso 6. Definir la verificación
Verificaremos la decisión con una evidencia relacionada directamente con el tema: una prueba, métrica, revisión de contrato, inspección de dependencias o demostración del flujo. El criterio debe responder: ¿cómo sabremos que la idea de la fuente está funcionando en nuestro sistema?

### 📦 Paso 7. Preparar la entrega
Guarda en GitHub el problema específico, las ideas de la fuente que aplicaste, la comparación, la decisión, los trade-offs y la evidencia. En el video de sustentación explícame qué entendiste, cómo lo aplicaste y qué riesgo aceptaste.


## 🚀 Preparación para la siguiente clase
Revisa la evidencia, registra los supuestos aún no validados y lleva una pregunta abierta sobre costo, calidad, dependencia o evolución. Cada clase debe agregar una pieza al expediente arquitectónico.
