# Video 60: Calidad de servicio y experiencia de usuario

## Título
Calidad de servicio y experiencia de usuario

## 🧭 Ficha de la clase
- **Actividad relacionada:** Actividad 5: pruebas, operación y defensa final
- **Duración sugerida:** 45 a 60 minutos
- **Modalidad:** explicación dialogada, ejemplo resuelto, taller y retroalimentación
- **Producto:** una evidencia que se incorpora al repositorio del proyecto

## 🔗 Continuidad de la ruta
Llegas a esta clase después de trabajar riesgos, continuidad y decisiones bajo incertidumbre. Ahora reuniremos esas decisiones para mirar la arquitectura como una práctica completa.

Esta clase cierra el recorrido y te prepara para defender tu expediente arquitectónico con criterio propio.

## 🎥 Escena de hoy
Hoy te encuentras ante esta situación: La arquitectura de software no solo se mide por qué tan bien se ejecuta internamente, sino por la experiencia que entrega a quienes la usan. Si el sistema es técnicamente sólido pero lento, poco intuitivo o inconsistente, la arquitectura termina fallando en la práctica. Este video conecta calidad técnica con calidad percibida por el usuario: tiempo de respuesta, confiabilidad, claridad, disponibilidad y consistencia.

Cuando el sistema es parte de una experiencia de negocio, la calidad de servicio se vuelve una necesidad de diseño. Un sistema puede estar bien estructurado, pero si no entrega valor de forma clara y confiable, no cumple su propósito. La arquitectura debe aportar experiencia y resultados, no solo estructura interna. El equipo te pide una decisión sobre calidad de servicio y experiencia de usuario, pero todavía no existe una respuesta única. Tu primera pista es esta idea de la fuente: La experiencia del usuario es una consecuencia del diseño arquitectónico.

## 🧭 Reto de la clase
Tu reto consiste en convertir esa idea en una decisión concreta: qué harías, qué dejarías fuera del alcance y cómo demostrarías que funciona.

## 🎯 Propósito de aprendizaje
Cuando terminemos, quiero que puedas validar la arquitectura frente a fallos, métricas, operación y escenarios de cambio usando el caso de la plataforma logística. No te voy a pedir que repitas una definición. Te voy a pedir que mires una situación, me expliques qué está en juego, tomes una decisión y me digas qué consecuencias esperas.

## 🎬 Apertura: Calidad de servicio y experiencia de usuario
Hoy vamos a trabajar una situación concreta: La arquitectura de software no solo se mide por qué tan bien se ejecuta internamente, sino por la experiencia que entrega a quienes la usan. Si el sistema es técnicamente sólido pero lento, poco intuitivo o inconsistente, la arquitectura termina fallando en la práctica. Este video conecta calidad técnica con calidad percibida por el usuario: tiempo de respuesta, confiabilidad, claridad, disponibilidad y consistencia.

Cuando el sistema es parte de una experiencia de negocio, la calidad de servicio se vuelve una necesidad de diseño. Un sistema puede estar bien estructurado, pero si no entrega valor de forma clara y confiable, no cumple su propósito. La arquitectura debe aportar experiencia y resultados, no solo estructura interna. No quiero que empieces por un diagrama ni por una tecnología. Quiero que me expliques qué problema aparece aquí y por qué merece una decisión arquitectónica propia.

Antes de entrar en calidad de servicio y experiencia de usuario, quiero que escuchemos primero la idea central de la fuente del curso: La arquitectura de software no solo se mide por qué tan bien se ejecuta internamente, sino por la experiencia que entrega a quienes la usan. Si el sistema es técnicamente sólido pero lento, poco intuitivo o inconsistente, la arquitectura termina fallando en la práctica. Este video conecta calidad técnica con calidad percibida por el usuario: tiempo de respuesta, confiabilidad, claridad, disponibilidad y consistencia.

Cuando el sistema es parte de una experiencia de negocio, la calidad de servicio se vuelve una necesidad de diseño. Un sistema puede estar bien estructurado, pero si no entrega valor de forma clara y confiable, no cumple su propósito. La arquitectura debe aportar experiencia y resultados, no solo estructura interna. En arquitectura no aprendemos una palabra para repetirla en un diagrama; aprendemos a reconocer una situación, analizar alternativas y tomar una decisión defendible.

Imagina que estamos frente a una pizarra. Yo te miro y te pregunto: ¿qué está pasando en este caso?, ¿quién depende de que esto funcione?, ¿qué información nos falta? No me respondas todavía con nombres de herramientas. Primero cuéntame qué problema ves en calidad de servicio y experiencia de usuario. Esa primera respuesta me permite saber si estamos entendiendo el tema o si solo estamos repitiendo soluciones conocidas.

Antes de continuar, haz una pausa conmigo. ¿Quién usa el sistema? ¿Qué espera que ocurra? ¿Qué no puede fallar? ¿Qué cambio es probable durante la vida del producto? Te hago estas preguntas porque una arquitectura no se diseña en el vacío. Si todavía no puedes responderlas, no es un problema: acabamos de encontrar la información que necesitamos investigar antes de diseñar.

## 💬 La pregunta que vamos a resolver sobre calidad de servicio y experiencia de usuario
¿Qué problema real resuelve calidad de servicio y experiencia de usuario y cómo demostraríamos que la solución es adecuada?

## 🧠 Entender calidad de servicio y experiencia de usuario desde el caso
### 📚 Lo que la fuente nos enseña sobre calidad de servicio y experiencia de usuario
La fuente describe este tema así: La arquitectura de software no solo se mide por qué tan bien se ejecuta internamente, sino por la experiencia que entrega a quienes la usan. Si el sistema es técnicamente sólido pero lento, poco intuitivo o inconsistente, la arquitectura termina fallando en la práctica. Este video conecta calidad técnica con calidad percibida por el usuario: tiempo de respuesta, confiabilidad, claridad, disponibilidad y consistencia.

Cuando el sistema es parte de una experiencia de negocio, la calidad de servicio se vuelve una necesidad de diseño. Un sistema puede estar bien estructurado, pero si no entrega valor de forma clara y confiable, no cumple su propósito. La arquitectura debe aportar experiencia y resultados, no solo estructura interna.

Yo voy a traducir esa idea a una situación de diseño. No quiero que la recibas como una definición cerrada; quiero que observes qué problema intenta resolver, qué decisiones implica y qué evidencia necesitaríamos para confiar en ella.

### 1. Escuchemos la fuente y llevémosla al sistema
Quiero que empecemos por la afirmación que trae la fuente: La experiencia del usuario es una consecuencia del diseño arquitectónico. Si la tomamos en serio, calidad de servicio y experiencia de usuario deja de ser una etiqueta y se convierte en una decisión que debemos observar en el sistema.

Ahora conectemos esa afirmación con la siguiente: Calidad técnica y calidad de servicio no son conceptos separados. Pregúntate qué componente, actor o regla del negocio queda afectado. No me interesa que repitas la frase; me interesa que puedas señalar dónde aparece en el caso logístico.

La tercera conversación es sobre las consecuencias: El tiempo de respuesta, la estabilidad y la claridad influyen en la percepción del sistema.. Aquí es donde una propuesta deja de ser teórica. Dime qué ganamos, qué sacrificamos y qué evidencia nos permitiría revisar la elección.

Finalmente, la fuente añade: Un servicio bueno no solo funciona; funciona con un nivel de calidad soportable. Esta idea nos ayuda a completar el análisis y a evitar una solución parcial. Cuando terminemos, deberás poder relacionar este principio con una decisión concreta del proyecto.

Mientras avanzamos, separa tres cosas: lo que la fuente afirma, lo que el caso logístico necesita y lo que tú decides hacer. Esa separación evita que una explicación general se convierta en una receta automática.

## ❓ Preguntas para pensar en calidad de servicio y experiencia de usuario
- **Te pregunto:** ¿Qué tan buena es la experiencia de uso de mi sistema? **La razón:** así conectamos el tema con el problema real en lugar de aplicarlo por moda.
- **Te pregunto:** ¿qué supuesto estamos haciendo y cómo podríamos comprobarlo? **La razón:** una decisión basada en una suposición no validada puede fallar en producción.
- **Te pregunto:** ¿qué costo aceptamos al elegir esta alternativa? **La razón:** toda arquitectura gana algo y renuncia a otra cosa.
- **Te pregunto:** ¿qué ocurriría si el volumen se multiplica o una dependencia deja de responder? **La razón:** una solución se demuestra cuando conocemos sus límites.

Estas no son preguntas para atraparte ni para calificarte de inmediato. Son las preguntas que te haría mientras conversamos frente a la pizarra. Si no tienes una respuesta todavía, dime qué dato te falta. En arquitectura, reconocer una duda y saber cómo investigarla demuestra más criterio que responder con seguridad algo que no podemos justificar.

## 💡 Lo esencial sobre Calidad de servicio y experiencia de usuario
- La experiencia del usuario es una consecuencia del diseño arquitectónico.
- Calidad técnica y calidad de servicio no son conceptos separados.
- El tiempo de respuesta, la estabilidad y la claridad influyen en la percepción del sistema.
- Un servicio bueno no solo funciona; funciona con un nivel de calidad soportable.
- La arquitectura debe anticipar la experiencia real del usuario final.
- El impacto del software se mide también por la continuidad y confiabilidad que ofrece.
- Una arquitectura saludable produce señales observables sobre rendimiento y fallos.
- El ejemplo debe documentarse con sus supuestos, trade-offs y evidencia de validación.

### 🔎 Mi lectura de calidad de servicio y experiencia de usuario como profesor
La arquitectura debe diseñarse para entregar valor no solo dentro del equipo técnico, sino también en la experiencia real del usuario. La calidad de servicio aparece como indicador de que la solución responde bien a las necesidades del entorno.

Cuando conectamos esta conclusión con el proyecto, la pregunta deja de ser "¿conozco el concepto?" y pasa a ser "¿puedo usarlo para tomar una decisión concreta y explicar sus consecuencias?".

## 🏗️ Cómo resolver calidad de servicio y experiencia de usuario en la práctica
Voy a resolver una situación contigo. La fuente plantea lo siguiente: La arquitectura de software no solo se mide por qué tan bien se ejecuta internamente, sino por la experiencia que entrega a quienes la usan. Si el sistema es técnicamente sólido pero lento, poco intuitivo o inconsistente, la arquitectura termina fallando en la práctica. Este video conecta calidad técnica con calidad percibida por el usuario: tiempo de respuesta, confiabilidad, claridad, disponibilidad y consistencia.

Cuando el sistema es parte de una experiencia de negocio, la calidad de servicio se vuelve una necesidad de diseño. Un sistema puede estar bien estructurado, pero si no entrega valor de forma clara y confiable, no cumple su propósito. La arquitectura debe aportar experiencia y resultados, no solo estructura interna. Ahora llévalo a la plataforma logística: durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. Pregúntate qué parte del sistema conoce esa regla, qué información necesita y qué ocurriría si aumenta la carga, falla una dependencia o cambia la política del negocio.

Fíjate en el razonamiento: el problema no es elegir una arquitectura moderna. El problema es mantener la promesa de entrega, proteger la información del cliente y responder ante cambios sin detener la operación. Desde ahí comparamos alternativas y explicamos por qué una es adecuada para este momento. Si cambian los datos del contexto, también puede cambiar nuestra decisión; eso no es una contradicción, es buena arquitectura.

## 🧩 Calidad de servicio y experiencia de usuario: caso de la plataforma logística
Ahora caminemos juntos por el flujo. Yo voy a detenerme en cada paso y te voy a pedir que mires tres cosas: qué regla estamos protegiendo, quién tiene la responsabilidad y qué ocurre si algo falla:

1. Un cliente crea un pedido.
2. El sistema valida los datos y reserva inventario.
3. El módulo de ruteo propone una asignación.
4. La plataforma comunica el estado al cliente y al repartidor.
5. Un incidente puede exigir reintento, compensación o intervención humana.

Después de cada paso, respóndeme: ¿qué puede salir mal?, ¿qué componente debe enterarse?, ¿qué información cruza el límite?, ¿qué decisión evita que el error se propague? No avances deprisa. Quiero que construyas una hipótesis y me expliques por qué la sostienes. Así pasamos de leer arquitectura a practicarla.

## ✍️ Tu reto: aplicar calidad de servicio y experiencia de usuario
Ahora te entrego la palabra. Entra en el papel de arquitecto o arquitecta. Parte del caso: durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable. No quiero una respuesta decorativa; quiero acompañarte mientras construyes el razonamiento. Trabaja así:

1. Redacta el problema en tres líneas, sin mencionar tecnologías.
2. Identifica tres actores y qué esperan del sistema.
3. Propón dos alternativas razonables.
4. Compáralas por costo inicial, calidad, riesgo y facilidad de cambio.
5. Elige una para el MVP y declara qué condición obligaría a revisarla.
6. Produce un diagrama, tabla, ADR o fragmento de código que haga visible la decisión.

Cuando termines, vuelve a leer tu propuesta como si fueras un compañero que llega hoy al proyecto. ¿Entendería por qué elegiste esa alternativa? ¿Sabría qué riesgo aceptaste? No busques adivinar "la respuesta que yo daría". Quiero que construyas una respuesta propia y que me la puedas defender. Puede ser diferente y seguir siendo correcta si presenta evidencia, reconoce sus costos y explica sus límites. Cuando la revisemos juntos, miraré tres cosas: que hayas delimitado el problema, que compares alternativas reales y que hagas visibles sus consecuencias.

### 🔎 Retroalimentación esperada
Cuando revise tu trabajo, no buscaré una frase elegante ni un diagrama lleno de cajas. Buscaré una decisión que pueda seguirse. Una evidencia madura no dice "elegimos X porque es mejor". Dice: "elegimos X porque priorizamos A y B; aceptamos C; descartamos Y por el riesgo D; verificaremos mediante E". Esa forma de escribir convierte una conversación técnica en conocimiento reutilizable.

Cuando termines, guarda en la carpeta correspondiente a Actividad 5: pruebas, operación y defensa final el contexto, la decisión, la alternativa descartada, dos consecuencias y una forma de verificación. No lo guardes como un trámite: este documento será la memoria de por qué decidiste construir así el sistema.



## ⚠️ Errores frecuentes
- Confundir el nombre del tema con una explicación de cómo calidad de servicio y experiencia de usuario afecta el sistema.
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
- ¿Qué tan buena es la experiencia de uso de mi sistema?
- ¿Qué factores técnicos afectan la percepción del usuario?
- ¿Estoy optimizando para robustez interna sin considerar la calidad percibida?

## 🗣️ Respuestas orientadoras

Ahora vamos a responder las preguntas que aparecieron durante la clase. No quiero que memorices una respuesta exacta. Quiero que compares mi razonamiento con el tuyo. Si llegaste a otra conclusión, puede ser válida si puedes explicarme el contexto, el costo y la evidencia que la sostiene.

La fuente de este video plantea: La arquitectura de software no solo se mide por qué tan bien se ejecuta internamente, sino por la experiencia que entrega a quienes la usan. Si el sistema es técnicamente sólido pero lento, poco intuitivo o inconsistente, la arquitectura termina fallando en la práctica. Este video conecta calidad técnica con calidad percibida por el usuario: tiempo de respuesta, confiabilidad, claridad, disponibilidad y consistencia.

Cuando el sistema es parte de una experiencia de negocio, la calidad de servicio se vuelve una necesidad de diseño. Un sistema puede estar bien estructurado, pero si no entrega valor de forma clara y confiable, no cumple su propósito. La arquitectura debe aportar experiencia y resultados, no solo estructura interna.

Fíjate en algo importante: ninguna respuesta depende de pronunciar el nombre de una tecnología. Lo que importa es que puedas unir cuatro cosas: el problema que observaste, la decisión que tomaste, la consecuencia que aceptaste y la evidencia que te permitirá comprobarla. Así quiero que pienses durante todo el curso.

### Cómo responder este tema concreto
1. **Cuando te preguntes: ¿Qué tan buena es la experiencia de uso de mi sistema?** Mi respuesta de partida sería: relaciona esta pregunta con la idea de que La experiencia del usuario es una consecuencia del diseño arquitectónico. Después busca una evidencia en el caso, no una opinión.
2. **Cuando te preguntes: ¿Qué factores técnicos afectan la percepción del usuario?** Mi respuesta de partida sería: relaciona esta pregunta con la idea de que Calidad técnica y calidad de servicio no son conceptos separados. Después busca una evidencia en el caso, no una opinión.
3. **Cuando te preguntes: ¿Estoy optimizando para robustez interna sin considerar la calidad percibida?** Mi respuesta de partida sería: relaciona esta pregunta con la idea de que El tiempo de respuesta, la estabilidad y la claridad influyen en la percepción del sistema. Después busca una evidencia en el caso, no una opinión.

## 🛠️ Solución modelo de la actividad

Esta es una resolución de referencia para que puedas comparar tu trabajo.

### 🔹 Paso 1. Delimitar el problema
El tema de esta clase se concreta así: La arquitectura de software no solo se mide por qué tan bien se ejecuta internamente, sino por la experiencia que entrega a quienes la usan. Si el sistema es técnicamente sólido pero lento, poco intuitivo o inconsistente, la arquitectura termina fallando en la práctica. Este video conecta calidad técnica con calidad percibida por el usuario: tiempo de respuesta, confiabilidad, claridad, disponibilidad y consistencia.

Cuando el sistema es parte de una experiencia de negocio, la calidad de servicio se vuelve una necesidad de diseño. Un sistema puede estar bien estructurado, pero si no entrega valor de forma clara y confiable, no cumple su propósito. La arquitectura debe aportar experiencia y resultados, no solo estructura interna. En el proyecto, el riesgo consiste en aplicar esa idea de forma superficial y terminar con una decisión que no protege el objetivo real. Por eso debemos establecer límites antes de implementar.

### 👥 Paso 2. Identificar actores y necesidades
- **Cliente:** espera crear el pedido y recibir estados confiables.
- **Operador logístico:** necesita visualizar incidentes y corregir asignaciones.
- **Repartidor:** necesita una ruta actualizada y una instrucción clara.
- **Equipo de desarrollo y operación:** necesita modificar, probar y observar el sistema sin afectar todo el flujo.

### 🔀 Paso 3. Proponer alternativas
- **Alternativa A:** resolver el problema dentro de la estructura actual con una regla, módulo, prueba o contrato explícito.
- **Alternativa B:** introducir una separación o mecanismo especializado que atienda el riesgo señalado por la fuente.

### ⚖️ Paso 4. Comparar consecuencias
La alternativa A reduce el costo inicial y conserva simplicidad, pero puede dejar expuesto el riesgo principal de calidad de servicio y experiencia de usuario. La alternativa B ofrece una protección más explícita, pero agrega trabajo, dependencias o complejidad operativa. No conviene elegir B solo porque suena más moderna; debe responder a la evidencia del caso.

### ✅ Paso 5. Tomar una decisión para el MVP
Para el MVP, recomiendo elegir la alternativa que proteja primero esta idea de la fuente: La experiencia del usuario es una consecuencia del diseño arquitectónico.. Declara qué complejidad estás aceptando y qué señal te obligaría a cambiar la decisión.

### 🧪 Paso 6. Definir la verificación
Verificaremos la decisión con una evidencia relacionada directamente con el tema: una prueba, métrica, revisión de contrato, inspección de dependencias o demostración del flujo. El criterio debe responder: ¿cómo sabremos que la idea de la fuente está funcionando en nuestro sistema?

### 📦 Paso 7. Preparar la entrega
Guarda en GitHub el problema específico, las ideas de la fuente que aplicaste, la comparación, la decisión, los trade-offs y la evidencia. En el video de sustentación explícame qué entendiste, cómo lo aplicaste y qué riesgo aceptaste.


## 🚀 Preparación para la siguiente clase
Revisa la evidencia, registra los supuestos aún no validados y lleva una pregunta abierta sobre costo, calidad, dependencia o evolución. Cada clase debe agregar una pieza al expediente arquitectónico.
