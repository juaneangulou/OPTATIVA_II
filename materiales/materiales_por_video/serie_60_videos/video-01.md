# Video 1: Decisiones de arquitectura y consecuencias reales

## Título
Decisiones de arquitectura y consecuencias reales

## 🧭 Ficha de la clase
- **Actividad relacionada:** Actividad 1: diagnóstico y contexto arquitectónico
- **Duración sugerida:** 45 a 60 minutos
- **Modalidad:** explicación dialogada, ejemplo resuelto, taller y retroalimentación
- **Producto:** una evidencia que se incorpora al repositorio del proyecto

## 🔗 Continuidad de la ruta
Esta es la primera conversación del recorrido. Vamos a construir el punto de partida: mirar el sistema como una decisión que afecta a personas, negocio y operación.

Cuando terminemos, tendrás el contexto necesario para avanzar hacia problema esencial y decisiones técnicas.

## 🎥 Escena de hoy
Hoy te encuentras ante esta situación: Este video abre con una historia impactante: la tragedia del Boeing 737 MAX. La idea principal es que un fallo grave no siempre es un simple bug aislado, sino una mala decisión arquitectónica. Cuando se prioriza velocidad o costo por encima de seguridad, las consecuencias pueden ser humanas y devastadoras.

A partir de ese ejemplo, el curso presenta la arquitectura de software como una decisión con impacto real. No se trata solo de elegir tecnologías o dibujar diagramas; se trata de diseñar sistemas que sean seguros, confiables, sostenibles y responsables. Cada decisión técnica puede influir en escalabilidad, seguridad, privacidad, accesibilidad y ética. El equipo te pide una decisión sobre decisiones de arquitectura y consecuencias reales, pero todavía no existe una respuesta única. Tu primera pista es esta idea de la fuente: Las decisiones de software tienen consecuencias reales y humanas.

## 🧭 Reto de la clase
Tu reto consiste en convertir esa idea en una decisión concreta: qué harías, qué dejarías fuera del alcance y cómo demostrarías que funciona.

## 🎯 Propósito de aprendizaje
Cuando terminemos, quiero que puedas analizar un problema real antes de elegir una tecnología usando el caso de la plataforma logística. No te voy a pedir que repitas una definición. Te voy a pedir que mires una situación, me expliques qué está en juego, tomes una decisión y me digas qué consecuencias esperas.

## 🎬 Apertura: Decisiones de arquitectura y consecuencias reales
Hoy vamos a trabajar una situación concreta: Este video abre con una historia impactante: la tragedia del Boeing 737 MAX. La idea principal es que un fallo grave no siempre es un simple bug aislado, sino una mala decisión arquitectónica. Cuando se prioriza velocidad o costo por encima de seguridad, las consecuencias pueden ser humanas y devastadoras.

A partir de ese ejemplo, el curso presenta la arquitectura de software como una decisión con impacto real. No se trata solo de elegir tecnologías o dibujar diagramas; se trata de diseñar sistemas que sean seguros, confiables, sostenibles y responsables. Cada decisión técnica puede influir en escalabilidad, seguridad, privacidad, accesibilidad y ética. No quiero que empieces por un diagrama ni por una tecnología. Quiero que me expliques qué problema aparece aquí y por qué merece una decisión arquitectónica propia.

Imagina que una plataforma controla un proceso del que dependen personas, dinero o seguridad. Una decisión aparentemente pequeña puede ampliar un riesgo hasta convertirlo en un incidente. La fuente abre con el caso del Boeing 737 MAX y nos recuerda que no basta preguntar si el software funciona: debemos preguntar qué supuestos incorpora y qué ocurre cuando se equivoca. Este video abre con una historia impactante: la tragedia del Boeing 737 MAX. La idea principal es que un fallo grave no siempre es un simple bug aislado, sino una mala decisión arquitectónica. Cuando se prioriza velocidad o costo por encima de seguridad, las consecuencias pueden ser humanas y devastadoras.

A partir de ese ejemplo, el curso presenta la arquitectura de software como una decisión con impacto real. No se trata solo de elegir tecnologías o dibujar diagramas; se trata de diseñar sistemas que sean seguros, confiables, sostenibles y responsables. Cada decisión técnica puede influir en escalabilidad, seguridad, privacidad, accesibilidad y ética.

Imagina que estamos frente a una pizarra. Yo te miro y te pregunto: ¿qué está pasando en este caso?, ¿quién depende de que esto funcione?, ¿qué información nos falta? No me respondas todavía con nombres de herramientas. Primero cuéntame qué problema ves en decisiones de arquitectura y consecuencias reales. Esa primera respuesta me permite saber si estamos entendiendo el tema o si solo estamos repitiendo soluciones conocidas.

Antes de continuar, haz una pausa conmigo. ¿Quién usa el sistema? ¿Qué espera que ocurra? ¿Qué no puede fallar? ¿Qué cambio es probable durante la vida del producto? Te hago estas preguntas porque una arquitectura no se diseña en el vacío. Si todavía no puedes responderlas, no es un problema: acabamos de encontrar la información que necesitamos investigar antes de diseñar.

## 💬 La pregunta que vamos a resolver sobre decisiones de arquitectura y consecuencias reales
¿Qué consecuencias humanas y de negocio puede producir una decisión técnica que nadie examinó con suficiente rigor?

## 🧠 Entender decisiones de arquitectura y consecuencias reales desde el caso
### 📚 Lo que la fuente nos enseña sobre decisiones de arquitectura y consecuencias reales
La fuente describe este tema así: Este video abre con una historia impactante: la tragedia del Boeing 737 MAX. La idea principal es que un fallo grave no siempre es un simple bug aislado, sino una mala decisión arquitectónica. Cuando se prioriza velocidad o costo por encima de seguridad, las consecuencias pueden ser humanas y devastadoras.

A partir de ese ejemplo, el curso presenta la arquitectura de software como una decisión con impacto real. No se trata solo de elegir tecnologías o dibujar diagramas; se trata de diseñar sistemas que sean seguros, confiables, sostenibles y responsables. Cada decisión técnica puede influir en escalabilidad, seguridad, privacidad, accesibilidad y ética.

Yo voy a traducir esa idea a una situación de diseño. No quiero que la recibas como una definición cerrada; quiero que observes qué problema intenta resolver, qué decisiones implica y qué evidencia necesitaríamos para confiar en ella.

### 1. Escuchemos la fuente y llevémosla al sistema
Quiero que empecemos por la afirmación que trae la fuente: Las decisiones de software tienen consecuencias reales y humanas. Si la tomamos en serio, decisiones de arquitectura y consecuencias reales deja de ser una etiqueta y se convierte en una decisión que debemos observar en el sistema.

Ahora conectemos esa afirmación con la siguiente: No todo fallo es un bug aislado; a veces es un problema de diseño. Pregúntate qué componente, actor o regla del negocio queda afectado. No me interesa que repitas la frase; me interesa que puedas señalar dónde aparece en el caso logístico.

La tercera conversación es sobre las consecuencias: La arquitectura afecta seguridad, escalabilidad, privacidad y confiabilidad.. Aquí es donde una propuesta deja de ser teórica. Dime qué ganamos, qué sacrificamos y qué evidencia nos permitiría revisar la elección.

Finalmente, la fuente añade: Priorizar costos o velocidad sin analizar el impacto puede ser peligroso. Esta idea nos ayuda a completar el análisis y a evitar una solución parcial. Cuando terminemos, deberás poder relacionar este principio con una decisión concreta del proyecto.

Mientras avanzamos, separa tres cosas: lo que la fuente afirma, lo que el caso logístico necesita y lo que tú decides hacer. Esa separación evita que una explicación general se convierta en una receta automática.

## ❓ Preguntas para pensar en decisiones de arquitectura y consecuencias reales
- **Te pregunto:** ¿Qué decisiones técnicas están afectando la seguridad o confiabilidad de mis sistemas? **La razón:** así conectamos el tema con el problema real en lugar de aplicarlo por moda.
- **Te pregunto:** ¿qué supuesto estamos haciendo y cómo podríamos comprobarlo? **La razón:** una decisión basada en una suposición no validada puede fallar en producción.
- **Te pregunto:** ¿qué costo aceptamos al elegir esta alternativa? **La razón:** toda arquitectura gana algo y renuncia a otra cosa.
- **Te pregunto:** ¿qué ocurriría si el volumen se multiplica o una dependencia deja de responder? **La razón:** una solución se demuestra cuando conocemos sus límites.

Estas no son preguntas para atraparte ni para calificarte de inmediato. Son las preguntas que te haría mientras conversamos frente a la pizarra. Si no tienes una respuesta todavía, dime qué dato te falta. En arquitectura, reconocer una duda y saber cómo investigarla demuestra más criterio que responder con seguridad algo que no podemos justificar.

## 💡 Lo esencial sobre Decisiones de arquitectura y consecuencias reales
- Las decisiones de software tienen consecuencias reales y humanas.
- No todo fallo es un bug aislado; a veces es un problema de diseño.
- La arquitectura afecta seguridad, escalabilidad, privacidad y confiabilidad.
- Priorizar costos o velocidad sin analizar el impacto puede ser peligroso.
- El arquitecto debe pensar más allá del código y en el contexto real del sistema.
- La responsabilidad técnica es parte esencial del diseño.
- Una decisión arquitectónica nace de objetivos, actores, restricciones y riesgos concretos.
- El ejemplo debe documentarse con sus supuestos, trade-offs y evidencia de validación.

### 🔎 Mi lectura de decisiones de arquitectura y consecuencias reales como profesor
La arquitectura de software no es solo una disciplina técnica; es una responsabilidad. Cada decisión define no solo cómo funciona el sistema, sino también su impacto en personas, negocios y sociedad.

Cuando conectamos esta conclusión con el proyecto, la pregunta deja de ser "¿conozco el concepto?" y pasa a ser "¿puedo usarlo para tomar una decisión concreta y explicar sus consecuencias?".

## 🏗️ Cómo resolver decisiones de arquitectura y consecuencias reales en la práctica
Voy a resolver una situación contigo. Para la plataforma logística, compare centralizar toda la asignación de rutas en un único componente con separar asignación, validación y gestión de incidentes. La primera opción puede ser rápida; la segunda puede evolucionar mejor, pero exige contratos y monitoreo. La decisión se justifica con volumen, criticidad, capacidad del equipo y consecuencias de una falla.

Fíjate en el razonamiento: el problema no es elegir una arquitectura moderna. El problema es mantener la promesa de entrega, proteger la información del cliente y responder ante cambios sin detener la operación. Desde ahí comparamos alternativas y explicamos por qué una es adecuada para este momento. Si cambian los datos del contexto, también puede cambiar nuestra decisión; eso no es una contradicción, es buena arquitectura.

## 🧩 Decisiones de arquitectura y consecuencias reales: caso de la plataforma logística
Ahora caminemos juntos por el flujo. Yo voy a detenerme en cada paso y te voy a pedir que mires tres cosas: qué regla estamos protegiendo, quién tiene la responsabilidad y qué ocurre si algo falla:

1. Un cliente crea un pedido.
2. El sistema valida los datos y reserva inventario.
3. El módulo de ruteo propone una asignación.
4. La plataforma comunica el estado al cliente y al repartidor.
5. Un incidente puede exigir reintento, compensación o intervención humana.

Después de cada paso, respóndeme: ¿qué puede salir mal?, ¿qué componente debe enterarse?, ¿qué información cruza el límite?, ¿qué decisión evita que el error se propague? No avances deprisa. Quiero que construyas una hipótesis y me expliques por qué la sostienes. Así pasamos de leer arquitectura a practicarla.

## ✍️ Tu reto: aplicar decisiones de arquitectura y consecuencias reales
Ahora te entrego la palabra. Entra en el papel de arquitecto o arquitecta. Parte del caso: la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad. No quiero una respuesta decorativa; quiero acompañarte mientras construyes el razonamiento. Trabaja así:

1. Redacta el problema en tres líneas, sin mencionar tecnologías.
2. Identifica tres actores y qué esperan del sistema.
3. Propón dos alternativas razonables.
4. Compáralas por costo inicial, calidad, riesgo y facilidad de cambio.
5. Elige una para el MVP y declara qué condición obligaría a revisarla.
6. Produce un diagrama, tabla, ADR o fragmento de código que haga visible la decisión.

Cuando termines, vuelve a leer tu propuesta como si fueras un compañero que llega hoy al proyecto. ¿Entendería por qué elegiste esa alternativa? ¿Sabría qué riesgo aceptaste? No busques adivinar "la respuesta que yo daría". Quiero que construyas una respuesta propia y que me la puedas defender. Puede ser diferente y seguir siendo correcta si presenta evidencia, reconoce sus costos y explica sus límites. Cuando la revisemos juntos, miraré tres cosas: que hayas delimitado el problema, que compares alternativas reales y que hagas visibles sus consecuencias.

### 🔎 Retroalimentación esperada
Cuando revise tu trabajo, no buscaré una frase elegante ni un diagrama lleno de cajas. Buscaré una decisión que pueda seguirse. Una evidencia madura no dice "elegimos X porque es mejor". Dice: "elegimos X porque priorizamos A y B; aceptamos C; descartamos Y por el riesgo D; verificaremos mediante E". Esa forma de escribir convierte una conversación técnica en conocimiento reutilizable.

Cuando termines, guarda en la carpeta correspondiente a Actividad 1: diagnóstico y contexto arquitectónico el contexto, la decisión, la alternativa descartada, dos consecuencias y una forma de verificación. No lo guardes como un trámite: este documento será la memoria de por qué decidiste construir así el sistema.



## ⚠️ Errores frecuentes
- Confundir el nombre del tema con una explicación de cómo decisiones de arquitectura y consecuencias reales afecta el sistema.
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
- ¿Qué decisiones técnicas están afectando la seguridad o confiabilidad de mis sistemas?
- ¿Estoy priorizando velocidad por encima de calidad y sostenibilidad?
- ¿Qué consecuencias reales puede tener un diseño débil en producción?

## 🗣️ Respuestas orientadoras

Ahora vamos a responder las preguntas que aparecieron durante la clase. No quiero que memorices una respuesta exacta. Quiero que compares mi razonamiento con el tuyo. Si llegaste a otra conclusión, puede ser válida si puedes explicarme el contexto, el costo y la evidencia que la sostiene.

La fuente de este video plantea: Este video abre con una historia impactante: la tragedia del Boeing 737 MAX. La idea principal es que un fallo grave no siempre es un simple bug aislado, sino una mala decisión arquitectónica. Cuando se prioriza velocidad o costo por encima de seguridad, las consecuencias pueden ser humanas y devastadoras.

A partir de ese ejemplo, el curso presenta la arquitectura de software como una decisión con impacto real. No se trata solo de elegir tecnologías o dibujar diagramas; se trata de diseñar sistemas que sean seguros, confiables, sostenibles y responsables. Cada decisión técnica puede influir en escalabilidad, seguridad, privacidad, accesibilidad y ética.

Fíjate en algo importante: ninguna respuesta depende de pronunciar el nombre de una tecnología. Lo que importa es que puedas unir cuatro cosas: el problema que observaste, la decisión que tomaste, la consecuencia que aceptaste y la evidencia que te permitirá comprobarla. Así quiero que pienses durante todo el curso.

### Cómo responder este tema concreto
1. **Cuando te preguntes: ¿Qué decisiones técnicas están afectando la seguridad o confiabilidad de mis sistemas?** Mi respuesta de partida sería: relaciona esta pregunta con la idea de que Las decisiones de software tienen consecuencias reales y humanas. Después busca una evidencia en el caso, no una opinión.
2. **Cuando te preguntes: ¿Estoy priorizando velocidad por encima de calidad y sostenibilidad?** Mi respuesta de partida sería: relaciona esta pregunta con la idea de que No todo fallo es un bug aislado; a veces es un problema de diseño. Después busca una evidencia en el caso, no una opinión.
3. **Cuando te preguntes: ¿Qué consecuencias reales puede tener un diseño débil en producción?** Mi respuesta de partida sería: relaciona esta pregunta con la idea de que La arquitectura afecta seguridad, escalabilidad, privacidad y confiabilidad. Después busca una evidencia en el caso, no una opinión.

## 🛠️ Solución modelo de la actividad

Esta es una resolución de referencia para que puedas comparar tu trabajo.

### 🔹 Paso 1. Delimitar el problema
El tema de esta clase se concreta así: Este video abre con una historia impactante: la tragedia del Boeing 737 MAX. La idea principal es que un fallo grave no siempre es un simple bug aislado, sino una mala decisión arquitectónica. Cuando se prioriza velocidad o costo por encima de seguridad, las consecuencias pueden ser humanas y devastadoras.

A partir de ese ejemplo, el curso presenta la arquitectura de software como una decisión con impacto real. No se trata solo de elegir tecnologías o dibujar diagramas; se trata de diseñar sistemas que sean seguros, confiables, sostenibles y responsables. Cada decisión técnica puede influir en escalabilidad, seguridad, privacidad, accesibilidad y ética. En el proyecto, el riesgo consiste en aplicar esa idea de forma superficial y terminar con una decisión que no protege el objetivo real. Por eso debemos establecer límites antes de implementar.

### 👥 Paso 2. Identificar actores y necesidades
- **Cliente:** espera crear el pedido y recibir estados confiables.
- **Operador logístico:** necesita visualizar incidentes y corregir asignaciones.
- **Repartidor:** necesita una ruta actualizada y una instrucción clara.
- **Equipo de desarrollo y operación:** necesita modificar, probar y observar el sistema sin afectar todo el flujo.

### 🔀 Paso 3. Proponer alternativas
- **Alternativa A:** resolver el problema dentro de la estructura actual con una regla, módulo, prueba o contrato explícito.
- **Alternativa B:** introducir una separación o mecanismo especializado que atienda el riesgo señalado por la fuente.

### ⚖️ Paso 4. Comparar consecuencias
La alternativa A reduce el costo inicial y conserva simplicidad, pero puede dejar expuesto el riesgo principal de decisiones de arquitectura y consecuencias reales. La alternativa B ofrece una protección más explícita, pero agrega trabajo, dependencias o complejidad operativa. No conviene elegir B solo porque suena más moderna; debe responder a la evidencia del caso.

### ✅ Paso 5. Tomar una decisión para el MVP
Para el MVP, recomiendo elegir la alternativa que proteja primero esta idea de la fuente: Las decisiones de software tienen consecuencias reales y humanas.. Declara qué complejidad estás aceptando y qué señal te obligaría a cambiar la decisión.

### 🧪 Paso 6. Definir la verificación
Verificaremos la decisión con una evidencia relacionada directamente con el tema: una prueba, métrica, revisión de contrato, inspección de dependencias o demostración del flujo. El criterio debe responder: ¿cómo sabremos que la idea de la fuente está funcionando en nuestro sistema?

### 📦 Paso 7. Preparar la entrega
Guarda en GitHub el problema específico, las ideas de la fuente que aplicaste, la comparación, la decisión, los trade-offs y la evidencia. En el video de sustentación explícame qué entendiste, cómo lo aplicaste y qué riesgo aceptaste.


## 🚀 Preparación para la siguiente clase
Revisa la evidencia, registra los supuestos aún no validados y lleva una pregunta abierta sobre costo, calidad, dependencia o evolución. Cada clase debe agregar una pieza al expediente arquitectónico.
