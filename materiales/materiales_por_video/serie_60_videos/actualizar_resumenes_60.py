from pathlib import Path

ROOT = Path(r"C:\proj\itm\OPTATIVA_II\materiales\materiales_por_video\serie_60_videos")
ROOT.mkdir(parents=True, exist_ok=True)

FUNDAMENTOS = [
    "Decisiones de arquitectura y consecuencias reales",
    "Problema esencial y decisiones técnicas",
    "El arquitecto y la responsabilidad técnica",
    "Negocio, usuarios y contexto",
    "Requisitos funcionales y no funcionales",
    "Calidad observable: rendimiento, seguridad y disponibilidad",
    "Costos ocultos y deuda técnica",
    "Riesgos y supuestos en diseño",
    "Diagnóstico de contexto arquitectónico",
    "Estructura del sistema y estilos arquitectónicos",
    "Monolito modular: empezar bien sin cerrarse",
    "Capas, límites y dependencias",
    "Microservicios y organización por dominios",
    "APIs y contratos de integración",
    "Acoplamiento entre servicios y sistemas",
    "Infraestructura, despliegue y entorno de ejecución",
    "Observabilidad y monitoreo de sistemas",
    "Seguridad, datos sensibles y privacidad",
    "Testing y validación de arquitectura",
    "DevOps y automatización de entrega",
    "Evolución del sistema y mantenimiento",
    "Comunicar la arquitectura con claridad",
    "Documentar decisiones y mantener contexto",
    "Arquitectura como responsabilidad humana",
    "Escalabilidad, seguridad y ética",
    "Principios de diseño y fundamentos de estructura",
    "Acoplamiento, cohesión y calidad estructural",
    "Modelado de dominios y límites de contexto",
    "Cierre del curso de fundamentos",
]

APLICADA = [
    "Intuición vs método en arquitectura de software",
    "Cómo analizar una licitación real con IA",
    "Monorepos con Pantsbuild en proyectos reales",
    "Trunk Based Development y reglas de calidad",
    "Behavior Driven Development para alinear equipos",
    "Modelo C4 para diagramar arquitecturas",
    "Quarto como documentación viva",
    "Agentes de IA revisando código en GitHub",
    "Estructura del archivo Architecture.md",
    "Domain Driven Design para arquitectura limpia",
    "Técnicas pre-mortem para prevenir fallos",
    "Premortem como guía de pruebas de arquitectura",
    "Métricas cuantitativas para evaluar arquitecturas",
    "Strangler Fig para migraciones",
    "Migraciones de base de datos con Flyway",
    "API Gateway como capa de abstracción",
    "Bounded context y context maps",
    "Infraestructura como código en monorepos",
    "Mensajes vs eventos en microservicios",
    "Productor consumidor y fan-in/fan-out",
    "Dead Letter Queue en sistemas distribuidos",
    "Comparing consumers para procesamiento en tiempo real",
    "Process manager en flujos complejos",
    "Durable State vs Event Sourcing",
    "Máquinas de estado finito en el front-end",
    "SAST, DAST y pentesting",
    "Fitness functions para medir arquitectura",
    "OpenTelemetry e ingeniería del caos",
    "Sabiduría y criterio en arquitectura de software",
    "Riesgos, continuidad y decisiones bajo incertidumbre",
    "Calidad de servicio y experiencia de usuario",
]

TITLES = FUNDAMENTOS + APLICADA
assert len(TITLES) == 60

PROFILES = {
    "contexto": {
        "purpose": "analizar un problema real antes de elegir una tecnología",
        "case": "la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad",
        "ideas": [
            "Una decisión arquitectónica nace de objetivos, actores, restricciones y riesgos concretos.",
            "Los hechos, supuestos y decisiones deben quedar separados y documentados.",
            "El costo de una decisión incluye operación, mantenimiento, cambios y consecuencias de una falla.",
        ],
        "questions": [
            "¿Qué evidencia del negocio justifica esta decisión?",
            "¿Qué supuesto todavía no ha sido validado?",
            "¿Qué consecuencia tendría equivocarse?",
        ],
    },
    "estructura": {
        "purpose": "comparar estructuras y justificar límites, responsabilidades y dependencias",
        "case": "pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna",
        "ideas": [
            "Una frontera útil define responsabilidad, contrato y propietario.",
            "La estructura debe ser proporcional al tamaño del equipo y al riesgo operativo.",
            "La dirección de las dependencias protege las reglas importantes frente a detalles externos.",
        ],
        "questions": [
            "¿Qué responsabilidad pertenece realmente a cada módulo?",
            "¿Qué dependencia sería más costosa de cambiar?",
            "¿La estructura resuelve un problema real o agrega complejidad?",
        ],
    },
    "dominio": {
        "purpose": "proteger las reglas del negocio dentro de un modelo claro y comprobable",
        "case": "una orden no puede marcarse como entregada si no existe una asignación válida y una evidencia de entrega",
        "ideas": [
            "Las entidades protegen identidad y comportamiento, no solo datos.",
            "Los objetos de valor expresan conceptos del negocio con validaciones propias.",
            "Los casos de uso coordinan acciones sin absorber responsabilidades de todas las capas.",
        ],
        "questions": [
            "¿Qué regla debe ser imposible de violar desde el código?",
            "¿Qué concepto merece una entidad u objeto de valor?",
            "¿Qué parte del modelo cambiaría si cambiara la base de datos?",
        ],
    },
    "implementacion": {
        "purpose": "construir un flujo ejecutable que conecte entrada, aplicación, dominio e infraestructura",
        "case": "un pedido entra por una API, ejecuta un caso de uso, persiste su estado y comunica el resultado",
        "ideas": [
            "Un flujo vertical conecta entrada, aplicación, dominio e infraestructura con límites visibles.",
            "Los adaptadores aíslan APIs, bases de datos, colas y herramientas de terceros.",
            "La automatización y la documentación reducen el costo de repetir y verificar el trabajo.",
        ],
        "questions": [
            "¿Dónde empieza y termina el caso de uso?",
            "¿Qué ocurre si la dependencia externa falla?",
            "¿Cómo se puede ejecutar y verificar el flujo en otro entorno?",
        ],
    },
    "operacion": {
        "purpose": "validar la arquitectura frente a fallos, métricas, operación y escenarios de cambio",
        "case": "durante una alta demanda, el sistema debe detectar latencia, recuperar mensajes fallidos y mantener una experiencia aceptable",
        "ideas": [
            "Una arquitectura saludable produce señales observables sobre rendimiento y fallos.",
            "Las pruebas deben comprobar reglas, contratos, integraciones y atributos de calidad.",
            "La evolución requiere priorizar riesgos y deuda técnica con datos, no solo intuición.",
        ],
        "questions": [
            "¿Qué métrica demostraría que la arquitectura cumple su objetivo?",
            "¿Cómo se detecta y recupera un fallo parcial?",
            "¿Qué riesgo debe atenderse antes de la siguiente versión?",
        ],
    },
}


def profile_for(number):
    if number <= 9:
        return PROFILES["contexto"]
    if number <= 16 or number in (26, 27, 28, 46):
        return PROFILES["estructura"]
    if number <= 29 or number in (39, 53, 54):
        return PROFILES["dominio"]
    if number <= 38 or number in (43, 44, 45, 47, 48, 49, 51, 52):
        return PROFILES["implementacion"]
    return PROFILES["operacion"]


def activity_for(number):
    if number <= 9:
        return "Actividad 1: diagnóstico y contexto arquitectónico"
    if number <= 16:
        return "Actividad 2: requisitos y decisión estructural"
    if number <= 29 or number in (39, 46):
        return "Actividad 3: diseño y dominio"
    if number <= 38 or number in (43, 44, 45, 47, 48, 49, 51, 52):
        return "Actividad 4: implementación e integración"
    return "Actividad 5: pruebas, operación y defensa final"


def code_example(number):
    examples = {
        13: """## Demostración en C#\n```csharp\npublic sealed record OrderId(Guid Value);\npublic sealed record Order(OrderId Id, decimal Total);\n```\n\nLa entidad expresa un concepto del dominio sin conocer una base de datos ni una API.""",
        14: """## Demostración en C#\n```csharp\npublic record CreateOrderRequest(string CustomerEmail, decimal Total);\npublic record OrderResponse(Guid Id, decimal Total, string Status);\n```\n\nEl contrato separa el formato de integración del modelo interno.""",
        27: """## Demostración en C#\n```csharp\npublic interface IOrderRepository\n{\n    Task SaveAsync(Order order);\n}\n```\n\nLa aplicación depende de un puerto; la infraestructura implementa el adaptador.""",
        28: """## Demostración en C#\n```csharp\npublic sealed class Order\n{\n    public bool IsPaid { get; private set; }\n    public void MarkAsPaid() => IsPaid = true;\n}\n```\n\nLa entidad protege una transición válida del negocio.""",
        39: """## Demostración en C#\n```csharp\npublic sealed class PlaceOrderUseCase\n{\n    private readonly IOrderRepository _repository;\n    public PlaceOrderUseCase(IOrderRepository repository) => _repository = repository;\n}\n```\n\nEl caso de uso recibe sus dependencias desde el borde.""",
    }
    return examples.get(number, "")


def guided_answers(title, profile):
    return f"""## 🗣️ Respuestas orientadoras

Ahora vamos a responder las preguntas que aparecieron durante la clase. No quiero que memorices una respuesta exacta. Quiero que compares mi razonamiento con el tuyo. Si llegaste a otra conclusión, puede ser válida si puedes explicarme el contexto, el costo y la evidencia que la sostiene.

1. **¿Qué problema resuelve esta clase?**  En este caso, {profile['case']}. El problema arquitectónico consiste en organizar responsabilidades y decisiones para que ese resultado sea posible sin perder calidad, trazabilidad ni capacidad de cambio.
2. **¿Qué supuesto debemos comprobar?**  Debemos comprobar los datos que condicionan la decisión: volumen, tiempos de respuesta, disponibilidad de dependencias, reglas del negocio y capacidad real del equipo. No debemos tratar una estimación como un hecho.
3. **¿Qué costo aceptamos?**  La alternativa elegida siempre sacrifica algo. Podemos aceptar más trabajo inicial para ganar mantenibilidad, o aceptar una solución más sencilla para reducir el costo del MVP. Lo importante es declarar el intercambio y ponerle una condición de revisión.
4. **¿Qué pasa si falla una dependencia?**  El sistema debe tener una respuesta definida: timeout, reintento controlado, degradación, compensación, cola de mensajes o intervención humana. Decir solamente “el sistema falla” no es una estrategia arquitectónica.
5. **¿Qué evidencia demostraría que la decisión funciona?**  Depende del tema: una métrica, una prueba, un contrato, un diagrama revisado, un registro de ejecución o una demostración del flujo. La evidencia debe corresponder al riesgo que queremos controlar.

Fíjate en algo importante: ninguna respuesta depende de pronunciar el nombre de una tecnología. Lo que importa es que puedas unir cuatro cosas: el problema que observaste, la decisión que tomaste, la consecuencia que aceptaste y la evidencia que te permitirá comprobarla. Así quiero que pienses durante todo el curso.

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
"""


def build_class(number, title):
    profile = profile_for(number)
    ideas = "\n".join(f"- {item}" for item in profile["ideas"])
    questions = "\n".join(f"- {item}" for item in profile["questions"])
    activity = activity_for(number)
    code = code_example(number)

    if number == 1:
        opening = "Imagina que una plataforma controla un proceso del que dependen personas, dinero o seguridad. Una decisión aparentemente pequeña puede ampliar un riesgo hasta convertirlo en un incidente. El caso del Boeing 737 MAX nos recuerda que no basta preguntar si el software funciona: debemos preguntar qué supuestos incorpora y qué ocurre cuando se equivoca."
        central = "¿Qué consecuencias humanas y de negocio puede producir una decisión técnica que nadie examinó con suficiente rigor?"
        worked = "Para la plataforma logística, compare centralizar toda la asignación de rutas en un único componente con separar asignación, validación y gestión de incidentes. La primera opción puede ser rápida; la segunda puede evolucionar mejor, pero exige contratos y monitoreo. La decisión se justifica con volumen, criticidad, capacidad del equipo y consecuencias de una falla."
    elif number == 2:
        opening = "Que el software funcione hoy no significa que sea una solución sostenible. Un sistema puede responder correctamente a diez pedidos y volverse imposible de cambiar cuando aparecen nuevas reglas, usuarios o integraciones. La arquitectura importa porque determina cuánto costará modificarlo mañana."
        central = "¿Qué diferencia existe entre entregar una funcionalidad y construir una solución que el equipo pueda sostener?"
        worked = "Suponga que la plataforma guarda pedidos, rutas y pagos en una sola clase. La primera versión puede funcionar, pero un cambio en la política de rutas obligaría a tocar pagos y notificaciones. Separar responsabilidades no es crear capas por moda: es proteger partes que cambian por razones diferentes."
    else:
        opening = f"Antes de entrar en {title.lower()}, deténgase en el problema que lo hace necesario. En arquitectura no aprendemos una palabra para repetirla en un diagrama; aprendemos a reconocer una situación, analizar alternativas y tomar una decisión defendible."
        central = f"¿Qué problema real resuelve {title.lower()} y cómo demostraríamos que la solución es adecuada?"
        worked = f"En la plataforma logística, {profile['case']}. Observe qué parte del sistema conoce esa regla, qué información necesita y qué ocurriría si aumenta la carga, falla una dependencia o cambia la política del negocio."

    prompts = "\n".join([
        f"- **Te pregunto:** ¿qué parte del problema pertenece realmente a {title.lower()}? **La razón:** así evitamos aplicar el concepto donde no aporta valor.",
        "- **Te pregunto:** ¿qué supuesto estamos haciendo y cómo podríamos comprobarlo? **La razón:** una decisión basada en una suposición no validada puede fallar en producción.",
        "- **Te pregunto:** ¿qué costo aceptamos al elegir esta alternativa? **La razón:** toda arquitectura gana algo y renuncia a otra cosa.",
        "- **Te pregunto:** ¿qué ocurriría si el volumen se multiplica o una dependencia deja de responder? **La razón:** una solución se demuestra cuando conocemos sus límites.",
    ])
    mistakes = "\n".join([
        f"- Confundir el nombre del tema con una explicación de cómo {title.lower()} afecta el sistema.",
        "- Elegir una herramienta antes de describir el problema y sus restricciones.",
        "- Presentar una solución como universal sin explicar cuándo dejaría de ser adecuada.",
        "- Omitir la evidencia, prueba o métrica que permitiría revisar la decisión.",
    ])

    return f"""# Video {number}: {title}

## Título
{title}

## 🧭 Ficha de la clase
- **Actividad relacionada:** {activity}
- **Duración sugerida:** 45 a 60 minutos
- **Modalidad:** explicación dialogada, ejemplo resuelto, taller y retroalimentación
- **Producto:** una evidencia que se incorpora al repositorio del proyecto

## 🎯 Propósito de aprendizaje
Cuando terminemos, quiero que puedas {profile['purpose']} usando el caso de la plataforma logística. No te voy a pedir que repitas una definición. Te voy a pedir que mires una situación, me expliques qué está en juego, tomes una decisión y me digas qué consecuencias esperas.

## 🎬 Apertura: pensemos como arquitectos
Bienvenido a esta clase. Hoy no voy a pedirte que empieces por un diagrama ni por una tecnología. Quiero que empecemos por una situación que podría ocurrir en un sistema real.

{opening}

Imagina que estamos frente a una pizarra. Yo te miro y te pregunto: ¿qué está pasando?, ¿quién depende de que esto funcione?, ¿qué información nos falta? No me respondas todavía con nombres de herramientas. Primero cuéntame qué problema ves. Esa primera respuesta me permite saber si estamos entendiendo el sistema o si solo estamos repitiendo soluciones conocidas.

Antes de continuar, haz una pausa conmigo. ¿Quién usa el sistema? ¿Qué espera que ocurra? ¿Qué no puede fallar? ¿Qué cambio es probable durante la vida del producto? Te hago estas preguntas porque una arquitectura no se diseña en el vacío. Si todavía no puedes responderlas, no es un problema: acabamos de encontrar la información que necesitamos investigar antes de diseñar.

## 💬 Pregunta central
{central}

## 🧠 Desarrollo de la clase
### 1. Describir el problema antes de diseñar
Ahora déjame mostrarte el primer movimiento. Cuando un equipo recibe una solicitud, suele saltar a la solución: "usemos microservicios", "hagamos una API" o "guardemos todo en una base de datos". Yo quiero que hoy invirtamos ese orden. Primero vamos a describir el comportamiento que el negocio necesita, las personas afectadas, las restricciones y los riesgos. Una decisión arquitectónica solo tiene sentido dentro de ese contexto.

Mira el caso logístico: asignar una ruta implica inventario, ubicación del repartidor, promesa de entrega, tráfico, costo operativo y comunicación. Si tratamos todo como una sola operación, luego será difícil saber qué probar, qué escalar y qué recuperar cuando ocurra un fallo. Aquí aparece la primera lección: antes de diseñar componentes, necesitamos entender las responsabilidades.

### 2. Separar hechos, supuestos y decisiones
Ahora hagamos una pausa. Un hecho es algo observable. Un supuesto es una afirmación que aún necesita validación. Una decisión es una elección entre alternativas. Por ejemplo, "tendremos 10 000 pedidos diarios" puede ser una estimación; "la API de mapas siempre responderá en menos de un segundo" es un supuesto; "aislaremos el proveedor mediante un adaptador" es una decisión. Cada elemento necesita una evidencia distinta. Si mezclamos estas tres cosas, terminaremos defendiendo opiniones como si fueran datos.

### 3. Hacer visibles las consecuencias
Llegamos al punto que más me interesa. No existe una alternativa gratuita. Una solución puede reducir el tiempo inicial y aumentar el costo de operación; otra puede mejorar la mantenibilidad y exigir más diseño; otra puede aumentar la disponibilidad y complicar la consistencia. Cuando yo te pida justificar una arquitectura, no quiero escuchar que una opción es "mejor". Quiero que me expliques qué gana, qué pierde y qué riesgo estamos aceptando.

{title} se entiende mejor cuando lo conectamos con esta secuencia: contexto, alternativas, decisión, consecuencias y evidencia. Si falta uno de esos pasos, la propuesta queda incompleta.

## ❓ Preguntas del profesor durante la explicación
{prompts}

Estas no son preguntas para atraparte ni para calificarte de inmediato. Son las preguntas que te haría mientras conversamos frente a la pizarra. Si no tienes una respuesta todavía, dime qué dato te falta. En arquitectura, reconocer una duda y saber cómo investigarla demuestra más criterio que responder con seguridad algo que no podemos justificar.

## 💡 Ideas esenciales
{ideas}
- El ejemplo debe documentarse con sus supuestos, trade-offs y evidencia de validación.

## 🏗️ Ejemplo resuelto
Voy a resolver una situación contigo. {worked}

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
Ahora te entrego la palabra. Entra en el papel de arquitecto o arquitecta. Parte del caso: {profile['case']}. No quiero una respuesta decorativa; quiero acompañarte mientras construyes el razonamiento. Trabaja así:

1. Redacta el problema en tres líneas, sin mencionar tecnologías.
2. Identifica tres actores y qué esperan del sistema.
3. Propón dos alternativas razonables.
4. Compáralas por costo inicial, calidad, riesgo y facilidad de cambio.
5. Elige una para el MVP y declara qué condición obligaría a revisarla.
6. Produce un diagrama, tabla, ADR o fragmento de código que haga visible la decisión.

Cuando termines, vuelve a leer tu propuesta como si fueras un compañero que llega hoy al proyecto. ¿Entendería por qué elegiste esa alternativa? ¿Sabría qué riesgo aceptaste? No busques adivinar "la respuesta que yo daría". Quiero que construyas una respuesta propia y que me la puedas defender. Puede ser diferente y seguir siendo correcta si presenta evidencia, reconoce sus costos y explica sus límites. Cuando la revisemos juntos, miraré tres cosas: que hayas delimitado el problema, que compares alternativas reales y que hagas visibles sus consecuencias.

### 🔎 Retroalimentación esperada
Cuando revise tu trabajo, no buscaré una frase elegante ni un diagrama lleno de cajas. Buscaré una decisión que pueda seguirse. Una evidencia madura no dice "elegimos X porque es mejor". Dice: "elegimos X porque priorizamos A y B; aceptamos C; descartamos Y por el riesgo D; verificaremos mediante E". Esa forma de escribir convierte una conversación técnica en conocimiento reutilizable.

Cuando termines, guarda en la carpeta correspondiente a {activity} el contexto, la decisión, la alternativa descartada, dos consecuencias y una forma de verificación. No lo guardes como un trámite: este documento será la memoria de por qué decidiste construir así el sistema.

{code}

## ⚠️ Errores frecuentes
{mistakes}

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
{questions}

{guided_answers(title, profile)}

## 🚀 Preparación para la siguiente clase
Revisa la evidencia, registra los supuestos aún no validados y lleva una pregunta abierta sobre costo, calidad, dependencia o evolución. Cada clase debe agregar una pieza al expediente arquitectónico.
"""


for extra in ROOT.glob("video-61.md"):
    extra.unlink()

readme = [
    "# Ruta de 60 clases de la materia",
    "",
    "Esta carpeta contiene clases completas para leer, explicar y trabajar con estudiantes. Cada clase se conecta con la siguiente mediante una evidencia del proyecto.",
    "",
    "## Curso 1: Fundamentos de Arquitectura de Software",
    "",
]
for index, title in enumerate(FUNDAMENTOS, start=1):
    readme.append(f"- [Video {index}: {title}](video-{index:02d}.md)")
readme.extend(["", "## Curso 2: Arquitectura de Software Aplicada", ""])
for index, title in enumerate(APLICADA, start=30):
    readme.append(f"- [Video {index}: {title}](video-{index:02d}.md)")
(ROOT / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")

for number, title in enumerate(TITLES, start=1):
    (ROOT / f"video-{number:02d}.md").write_text(build_class(number, title), encoding="utf-8")

print(f"Regeneradas {len(TITLES)} clases Markdown en {ROOT}")
