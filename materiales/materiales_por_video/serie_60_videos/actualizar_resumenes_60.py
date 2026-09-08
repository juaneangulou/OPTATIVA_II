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
        f"- ¿Qué parte del problema pertenece realmente a {title.lower()}?",
        "- ¿Qué supuesto estamos haciendo y cómo podríamos comprobarlo?",
        "- ¿Qué costo aceptamos al elegir esta alternativa?",
        "- ¿Qué ocurriría si el volumen se multiplica o una dependencia deja de responder?",
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

## Ficha de la clase
- **Actividad relacionada:** {activity}
- **Duración sugerida:** 45 a 60 minutos
- **Modalidad:** explicación dialogada, ejemplo resuelto, taller y retroalimentación
- **Producto:** una evidencia que se incorpora al repositorio del proyecto

## Propósito de aprendizaje
Al finalizar esta clase, quiero que puedas {profile['purpose']} usando el caso de la plataforma logística. No quiero que memorices una definición para repetirla: quiero que aprendas a reconocer el problema, argumentar una decisión y anticipar sus consecuencias.

## Apertura: pensemos como arquitectos
Bienvenido a esta clase. Hoy no voy a pedirte que empieces por un diagrama ni por una tecnología. Quiero que empecemos por una situación que podría ocurrir en un sistema real.

{opening}

Mientras lees, imagina que estamos frente a una pizarra. Yo te pregunto: ¿qué está pasando?, ¿quién depende de que esto funcione?, ¿qué información nos falta? No respondas todavía con nombres de herramientas. Primero cuéntame qué problema ves.

Antes de continuar, detente un momento y responde: ¿quién usa el sistema?, ¿qué espera que ocurra?, ¿qué no puede fallar?, ¿qué cambio es probable durante la vida del producto? Yo prefiero que lleguemos a estas preguntas antes de mencionar un framework. Si todavía no podemos responderlas, no pasa nada: acabamos de descubrir qué necesitamos investigar antes de diseñar.

## Pregunta central
{central}

## Desarrollo de la clase
### 1. Describir el problema antes de diseñar
Ahora déjame mostrarte el primer movimiento. Cuando un equipo recibe una solicitud, suele saltar a la solución: "usemos microservicios", "hagamos una API" o "guardemos todo en una base de datos". Yo quiero que hoy invirtamos ese orden. Primero vamos a describir el comportamiento que el negocio necesita, las personas afectadas, las restricciones y los riesgos. Una decisión arquitectónica solo tiene sentido dentro de ese contexto.

Mira el caso logístico: asignar una ruta implica inventario, ubicación del repartidor, promesa de entrega, tráfico, costo operativo y comunicación. Si tratamos todo como una sola operación, luego será difícil saber qué probar, qué escalar y qué recuperar cuando ocurra un fallo. Aquí aparece la primera lección: antes de diseñar componentes, necesitamos entender las responsabilidades.

### 2. Separar hechos, supuestos y decisiones
Ahora hagamos una pausa. Un hecho es algo observable. Un supuesto es una afirmación que aún necesita validación. Una decisión es una elección entre alternativas. Por ejemplo, "tendremos 10 000 pedidos diarios" puede ser una estimación; "la API de mapas siempre responderá en menos de un segundo" es un supuesto; "aislaremos el proveedor mediante un adaptador" es una decisión. Cada elemento necesita una evidencia distinta. Si mezclamos estas tres cosas, terminaremos defendiendo opiniones como si fueran datos.

### 3. Hacer visibles las consecuencias
Llegamos al punto que más me interesa. No existe una alternativa gratuita. Una solución puede reducir el tiempo inicial y aumentar el costo de operación; otra puede mejorar la mantenibilidad y exigir más diseño; otra puede aumentar la disponibilidad y complicar la consistencia. Cuando yo te pida justificar una arquitectura, no quiero escuchar que una opción es "mejor". Quiero que me expliques qué gana, qué pierde y qué riesgo estamos aceptando.

{title} se entiende mejor cuando lo conectamos con esta secuencia: contexto, alternativas, decisión, consecuencias y evidencia. Si falta uno de esos pasos, la propuesta queda incompleta.

## Preguntas del profesor durante la explicación
{prompts}

No leas estas preguntas como un examen. Son las preguntas que yo usaría mientras conversamos frente a la pizarra. Si todavía no tienes una respuesta, anótala como una duda de diseño. Una duda bien formulada es más útil que una respuesta rápida y débil.

## Ideas esenciales
{ideas}
- El ejemplo debe documentarse con sus supuestos, trade-offs y evidencia de validación.

## Ejemplo resuelto
Voy a resolver una situación contigo. {worked}

Fíjate en el razonamiento: el problema no es elegir una arquitectura moderna. El problema es mantener la promesa de entrega, proteger la información del cliente y responder ante cambios sin detener la operación. Desde ahí comparamos alternativas y explicamos por qué una es adecuada para este momento. Si cambian los datos del contexto, también puede cambiar nuestra decisión; eso no es una contradicción, es buena arquitectura.

## Caso guiado: plataforma logística
Ahora te propongo que caminemos juntos por el flujo. En cada paso voy a pedirte que preguntes qué regla se protege, quién tiene la responsabilidad y qué pasa si falla:

1. Un cliente crea un pedido.
2. El sistema valida los datos y reserva inventario.
3. El módulo de ruteo propone una asignación.
4. La plataforma comunica el estado al cliente y al repartidor.
5. Un incidente puede exigir reintento, compensación o intervención humana.

Haz una pausa después de cada paso y escribe: ¿qué puede salir mal?, ¿qué componente debe enterarse?, ¿qué información cruza el límite?, ¿qué decisión evita que el error se propague? No avances hasta tener una hipótesis. En arquitectura aprendemos pensando sobre las consecuencias, no pasando rápidamente por los títulos.

## Taller de clase
Ahora te entrego la palabra. Entra en el papel de arquitecto o arquitecta. Parte del caso: {profile['case']}. No quiero una respuesta decorativa; quiero acompañarte mientras construyes el razonamiento. Trabaja así:

1. Redacta el problema en tres líneas, sin mencionar tecnologías.
2. Identifica tres actores y qué esperan del sistema.
3. Propón dos alternativas razonables.
4. Compáralas por costo inicial, calidad, riesgo y facilidad de cambio.
5. Elige una para el MVP y declara qué condición obligaría a revisarla.
6. Produce un diagrama, tabla, ADR o fragmento de código que haga visible la decisión.

Cuando termines, vuelve a leer tu propuesta como si fueras un compañero que llega hoy al proyecto. ¿Entendería por qué elegiste esa alternativa? ¿Sabría qué riesgo aceptaste? No busques "la respuesta que yo daría". Quiero que construyas una respuesta propia. Puede ser diferente y seguir siendo correcta si presenta evidencia, reconoce sus costos y explica sus límites. Yo revisaré tres cosas: que delimites el problema, que compares alternativas reales y que hagas visibles sus consecuencias.

### Retroalimentación esperada
Cuando revise tu trabajo, no buscaré una frase elegante ni un diagrama lleno de cajas. Buscaré una decisión que pueda seguirse. Una evidencia madura no dice "elegimos X porque es mejor". Dice: "elegimos X porque priorizamos A y B; aceptamos C; descartamos Y por el riesgo D; verificaremos mediante E". Esa forma de escribir convierte una conversación técnica en conocimiento reutilizable.

La evidencia mínima debe incluir contexto, decisión, alternativa descartada, dos consecuencias y una forma de verificación. Guárdala en la carpeta correspondiente a {activity}.

{code}

## Errores frecuentes
{mistakes}

## Cierre: lo que te llevas de esta clase
Hemos llegado al final. Antes de cerrar, imagina que yo te doy dos minutos frente al equipo. Quiero escucharte defender tu decisión: empieza por el problema, describe el contexto, compara las alternativas, explica tu elección y termina con el trade-off y la evidencia que la respalda. No intentes sonar complicado; intenta ser claro. Si otra persona puede entender tu decisión sin haber estado en esta conversación, has hecho un buen trabajo.

Quédate con esta idea: diseñar arquitectura no es adivinar el futuro ni encontrar una solución perfecta. Es tomar una decisión responsable con la información disponible, reconocer lo que todavía no sabemos y preparar el sistema para aprender y cambiar. Cada vez que documentas un supuesto, nombras un riesgo o explicas un costo, estás actuando como arquitecto.

Ahora mira tu propia propuesta y pregúntate: ¿qué parte defendería con confianza?, ¿qué parte necesita evidencia?, ¿qué cambiaría si el negocio creciera mañana? Esa pregunta es el puente hacia la siguiente clase.

## Comprobación de aprendizaje
- ¿Puedes explicarme el problema sin mencionar primero una tecnología?
- ¿Puedes defender la comparación entre dos alternativas con criterios concretos?
- ¿Puedes decirme qué cambiaría ante un nuevo requisito o un fallo?
- ¿Puedes mostrarme qué evidencia respaldaría o refutaría tu decisión?

## Preguntas para reflexión
{questions}

## Preparación para la siguiente clase
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
