from pathlib import Path
import re
import unicodedata

ROOT = Path(r"C:\proj\itm\OPTATIVA_II\materiales\materiales_por_video\serie_60_videos")
ROOT.mkdir(parents=True, exist_ok=True)
SOURCE_ROOT = ROOT.parents[1] / "material_cursos_raw_summary" / "cursos"

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


def normalize(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return set(re.findall(r"[a-z0-9]{4,}", value))


def source_section(text, name):
    match = re.search(rf"^##\s+{re.escape(name)}\s*$\n(.*?)(?=^##\s+|\Z)", text, re.M | re.S)
    return match.group(1).strip() if match else ""


def load_source_documents():
    documents = []
    for path in sorted(SOURCE_ROOT.glob("**/videos/*.md")):
        text = path.read_text(encoding="utf-8")
        heading = re.search(r"^#\s+.*?:?\s*(.*)$", text, re.M)
        title = heading.group(1).strip() if heading else path.stem
        summary = source_section(text, "Resumen")
        ideas = [line[2:].strip() for line in source_section(text, "Ideas principales").splitlines() if line.strip().startswith("- ")]
        questions = [line[2:].strip() for line in source_section(text, "Preguntas para reflexión").splitlines() if line.strip().startswith("- ")]
        conclusion = source_section(text, "Conclusión")
        documents.append({"path": path, "title": title, "text": text, "summary": summary, "ideas": ideas, "questions": questions, "conclusion": conclusion})
    return documents


SOURCE_DOCUMENTS = load_source_documents()


USED_SOURCE_PATHS = set()
SOURCE_HINTS = {
    1: "video-01-decisiones-de-arquitectura-y-consecuencias-reales.md",
    2: "video-02-por-que-importa-la-arquitectura.md",
    3: "video-03-rol-del-arquitecto-de-software.md",
    4: "video-04-comunicar-la-arquitectura.md",
    6: "video-07-escalabilidad-y-rendimiento.md",
    14: "video-13-apis-y-contratos-de-integracion.md",
    16: "video-14-infraestructura-despliegue-y-entorno-de-ejecucion.md",
    17: "video-15-observabilidad-y-monitoreo-de-sistemas.md",
    18: "video-16-seguridad-datos-sensibles-y-privacidad.md",
    19: "video-17-testing-y-validacion-de-arquitectura.md",
    20: "video-18-devops-y-automatizacion-de-entrega.md",
    21: "video-21-diseno-para-cambio-y-evolucion.md",
    22: "video-22-comunicacion-liderazgo-y-negociacion-tecnica.md",
    23: "video-05-documentar-decisiones-y-mantener-claridad.md",
    25: "video-07-escalabilidad-seguridad-y-etica.md",
    26: "video-08-fundamentos-de-diseno-y-principios-de-arquitectura.md",
    27: "video-09-acoplamiento-cohesion-y-calidad-estructural.md",
    28: "video-10-modelado-de-dominios-y-limites-de-contexto.md",
    39: "video-11-microservicios-y-dominios.md",
    46: "video-11-microservicios-y-dominios.md",
}


def source_for(number, title):
    hint = SOURCE_HINTS.get(number)
    if hint:
        matches = [document for document in SOURCE_DOCUMENTS if document["path"].name == hint]
        if matches:
            USED_SOURCE_PATHS.add(matches[0]["path"])
            return matches[0]

    special_source_numbers = {39: 11, 46: 11}

    def source_number(document):
        match = re.search(r"video-(\d+)", document["path"].name)
        return int(match.group(1)) if match else 0

    if number in special_source_numbers:
        candidates = [
            document for document in SOURCE_DOCUMENTS
            if "arquitectura-software-aplicada" in str(document["path"])
            and source_number(document) == special_source_numbers[number]
        ]
        if candidates:
            USED_SOURCE_PATHS.add(candidates[0]["path"])
            return candidates[0]

    target = normalize(title)
    preferred = "fundamentos-arquitectura-software" if number <= 29 else "arquitectura-software-aplicada"
    ranked = []
    for document in SOURCE_DOCUMENTS:
        title_tokens = normalize(document["title"])
        file_tokens = normalize(document["path"].stem)
        score = len(target & title_tokens) * 8 + len(target & file_tokens) * 3
        if preferred in str(document["path"]):
            score += 2
        if title_tokens and title_tokens.issubset(target):
            score += 20
        ranked.append((score, document))
    ranked.sort(key=lambda item: item[0], reverse=True)
    unused = [document for _, document in ranked if document["path"] not in USED_SOURCE_PATHS]
    chosen = unused[0] if unused else ranked[0][1]
    USED_SOURCE_PATHS.add(chosen["path"])
    return chosen


def topic_lesson(title, source):
    ideas = source["ideas"][:4]
    if not ideas:
        ideas = [source["summary"] or title]
    paragraphs = [
        f"Quiero que empecemos por la afirmación que trae la fuente: {ideas[0]} Si la tomamos en serio, {title.lower()} deja de ser una etiqueta y se convierte en una decisión que debemos observar en el sistema.",
        f"Ahora conectemos esa afirmación con la siguiente: {ideas[1] if len(ideas) > 1 else ideas[0]} Pregúntate qué componente, actor o regla del negocio queda afectado. No me interesa que repitas la frase; me interesa que puedas señalar dónde aparece en el caso logístico.",
        f"La tercera conversación es sobre las consecuencias: {ideas[2] if len(ideas) > 2 else 'una decisión técnica siempre produce beneficios y costos'}. Aquí es donde una propuesta deja de ser teórica. Dime qué ganamos, qué sacrificamos y qué evidencia nos permitiría revisar la elección.",
    ]
    if len(ideas) > 3:
        paragraphs.append(f"Finalmente, la fuente añade: {ideas[3]} Esta idea nos ayuda a completar el análisis y a evitar una solución parcial. Cuando terminemos, deberás poder relacionar este principio con una decisión concreta del proyecto.")
    return "\n\n".join(paragraphs)


def class_scene(number, title, source):
    idea = (source["ideas"] or ["la decisión debe poder justificarse con evidencia"])[0]
    summary = source["summary"] or "el sistema debe responder a una necesidad real del negocio"
    return (
        f"Hoy te encuentras ante esta situación: {summary} "
        f"El equipo te pide una decisión sobre {title.lower()}, pero todavía no existe una respuesta única. "
        f"Tu primera pista es esta idea de la fuente: {idea}",
        f"Tu reto consiste en convertir esa idea en una decisión concreta: qué harías, qué dejarías fuera del alcance y cómo demostrarías que funciona."
    )


def source_case_questions(source, profile):
    questions = source["questions"][:4] or profile["questions"]
    return "\n".join(
        f"{index}. Detente en esta pregunta de la fuente: {question} Después de responderla, señala qué decisión cambia en la plataforma logística."
        for index, question in enumerate(questions, start=1)
    )


def explain_source_idea(index, idea, title, profile):
    lower = idea.lower()
    short_case = "la plataforma logística"
    if any(word in lower for word in ("seguridad", "privacidad", "ética", "impacto", "responsabilidad")):
        return f"Aquí quiero que mires el riesgo humano de esta idea. {idea} Pregúntate quién podría quedar expuesto si la ignoramos y qué control de diseño reduciría ese riesgo en {short_case}."
    if any(word in lower for word in ("escalabilidad", "rendimiento", "carga", "crecer", "estabilidad")):
        return f"Ahora llévala a un escenario de crecimiento. {idea} Imagina que aumenta el tráfico: identifica el primer cuello de botella y decide qué medirías antes de añadir infraestructura."
    if any(word in lower for word in ("api", "contrato", "integración", "comunicación", "servicio")):
        return f"En esta idea nos interesa el límite entre componentes. {idea} Dibuja quién consume la información, qué contrato necesita y qué cambio podría romper al consumidor."
    if any(word in lower for word in ("dominio", "entidad", "regla", "responsabilidad", "módulo")):
        return f"Aquí vamos a buscar la regla del negocio. {idea} Escribe qué objeto o módulo debería protegerla y qué error queremos impedir aunque cambie la base de datos o la interfaz."
    if any(word in lower for word in ("prueba", "testing", "validar", "métrica", "observable")):
        return f"Esta idea solo queda completa cuando podemos comprobarla. {idea} Elige una prueba o métrica y explica qué resultado confirmaría o cuestionaría nuestra decisión sobre {title.lower()}."
    return f"Detente en la consecuencia de esta idea: {idea} Relaciónala con una decisión concreta del proyecto, señala qué alternativa descartarías y explícame por qué."


def decision_options(number, title, profile, source):
    if number == 2:
        return """## 🔀 Las dos opciones que vamos a comparar

### Opción A: resolver solo la necesidad inmediata
Construimos una solución que funcione para el volumen actual, concentramos varias responsabilidades y priorizamos entregar rápido. Tiene una ventaja clara: menor costo inicial y menos decisiones que coordinar. Su riesgo es que el sistema quede frágil cuando aumenten usuarios, reglas o integraciones.

### Opción B: construir una base preparada para evolucionar
Separamos las responsabilidades que probablemente cambien, protegemos los datos sensibles y dejamos contratos claros entre módulos. Tiene un costo inicial mayor, pero reduce el costo de cambiar y facilita comprobar seguridad, rendimiento y mantenibilidad.

### Cómo decidir entre A y B
No elijas B solo porque suena más profesional. Compara volumen esperado, criticidad, crecimiento, equipo disponible y costo de operación. Para este caso, recomiendo un monolito modular: entregar rápido, pero con límites internos claros, pruebas de las reglas críticas y adaptadores para las dependencias externas. Así no confundimos sencillez con desorden ni evolución con sobreingeniería."""
    return f"""## 🔀 Opciones para resolver {title.lower()}

- **Opción A:** aplicar una solución sencilla dentro de la estructura actual, documentando sus límites.
- **Opción B:** introducir una separación o mecanismo especializado para proteger el riesgo principal de la fuente.

Compara ambas por costo inicial, calidad, operación, facilidad de cambio y evidencia disponible. Elige una solo después de explicar qué problema resuelve y qué costo aceptas."""


def specific_solution_steps(number, title, profile, source):
    if number == 2:
        return """## 🛠️ Resolución paso a paso del video 2

1. **Define el problema esencial.** La plataforma debe seguir funcionando cuando aumenten pedidos, usuarios e integraciones; no basta con que responda correctamente hoy.
2. **Separa el problema de la tecnología.** El problema es sostenibilidad, no “elegir microservicios” ni “usar una base de datos específica”.
3. **Compara las opciones.** La opción A entrega rápido, pero mezcla responsabilidades y encarece los cambios. La opción B protege la evolución, pero requiere más diseño y disciplina.
4. **Elige una solución proporcional.** Para el MVP, usa un monolito modular con módulos de pedidos, inventario, ruteo y notificaciones, contratos internos y reglas de negocio protegidas.
5. **Define qué no harás todavía.** No separarás servicios ni introducirás infraestructura distribuida hasta contar con evidencia de volumen, autonomía de equipos o necesidad de escalar por separado.
6. **Comprueba la decisión.** Ejecuta una prueba de cambio: modifica una regla de ruteo y verifica que no tengas que modificar pagos ni notificaciones. Mide también tiempo de respuesta y facilidad de despliegue.
7. **Documenta el resultado.** Escribe un ADR con contexto, opciones, decisión, trade-offs y condición de revisión. Esa es la evidencia que demuestra que entendiste la fuente y no solo repetiste su definición."""
    return f"""## 🛠️ Resolución paso a paso

1. Define el problema que la fuente ayuda a resolver.
2. Identifica a los actores y el riesgo principal.
3. Compara dos opciones concretas.
4. Elige una solución proporcional al MVP.
5. Declara qué queda fuera y cuándo revisarás la decisión.
6. Define una prueba, métrica o evidencia.
7. Documenta la decisión y sus trade-offs en GitHub."""


def section_titles(title, source):
    topic = title.rstrip(".")
    first_idea = (source["ideas"] or ["el problema real del sistema"])[0].rstrip(".")
    return {
        "opening": f"🎬 Apertura: {topic}",
        "question": f"💬 La pregunta que vamos a resolver sobre {topic.lower()}",
        "development": f"🧠 Entender {topic.lower()} desde el caso",
        "example": f"🏗️ Cómo resolver {topic.lower()} en la práctica",
        "case": f"🧩 {topic}: caso de la plataforma logística",
        "workshop": f"✍️ Tu reto: aplicar {topic.lower()}",
        "ideas": f"💡 Lo esencial sobre {topic}",
        "source": f"📚 Lo que la fuente nos enseña sobre {topic.lower()}",
        "teacher_questions": f"❓ Preguntas para pensar en {topic.lower()}",
        "teacher_reading": f"🔎 Mi lectura de {topic.lower()} como profesor",
    }

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


def guided_answers(title, profile, source):
    source_ideas = source["ideas"][:4] or profile["ideas"]
    source_questions = source["questions"][:3] or profile["questions"]
    specific_answers = "\n".join(
        f"{index}. **Cuando te preguntes: {question}** Mi respuesta de partida sería: relaciona esta pregunta con la idea de que {source_ideas[index - 1] if index <= len(source_ideas) else source_ideas[0]} Después busca una evidencia en el caso, no una opinión."
        for index, question in enumerate(source_questions, start=1)
    )
    return f"""## 🗣️ Respuestas orientadoras

Ahora vamos a responder las preguntas que aparecieron durante la clase. No quiero que memorices una respuesta exacta. Quiero que compares mi razonamiento con el tuyo. Si llegaste a otra conclusión, puede ser válida si puedes explicarme el contexto, el costo y la evidencia que la sostiene.

La fuente de este video plantea: {source['summary'] or profile['case']}

Fíjate en algo importante: ninguna respuesta depende de pronunciar el nombre de una tecnología. Lo que importa es que puedas unir cuatro cosas: el problema que observaste, la decisión que tomaste, la consecuencia que aceptaste y la evidencia que te permitirá comprobarla. Así quiero que pienses durante todo el curso.

### Cómo responder este tema concreto
{specific_answers}

## 🛠️ Solución modelo de la actividad

Esta es una resolución de referencia para que puedas comparar tu trabajo.

### 🔹 Paso 1. Delimitar el problema
El tema de esta clase se concreta así: {source['summary'] or profile['case']} En el proyecto, el riesgo consiste en aplicar esa idea de forma superficial y terminar con una decisión que no protege el objetivo real. Por eso debemos establecer límites antes de implementar.

### 👥 Paso 2. Identificar actores y necesidades
- **Cliente:** espera crear el pedido y recibir estados confiables.
- **Operador logístico:** necesita visualizar incidentes y corregir asignaciones.
- **Repartidor:** necesita una ruta actualizada y una instrucción clara.
- **Equipo de desarrollo y operación:** necesita modificar, probar y observar el sistema sin afectar todo el flujo.

### 🔀 Paso 3. Proponer alternativas
- **Alternativa A:** resolver el problema dentro de la estructura actual con una regla, módulo, prueba o contrato explícito.
- **Alternativa B:** introducir una separación o mecanismo especializado que atienda el riesgo señalado por la fuente.

### ⚖️ Paso 4. Comparar consecuencias
La alternativa A reduce el costo inicial y conserva simplicidad, pero puede dejar expuesto el riesgo principal de {title.lower()}. La alternativa B ofrece una protección más explícita, pero agrega trabajo, dependencias o complejidad operativa. No conviene elegir B solo porque suena más moderna; debe responder a la evidencia del caso.

### ✅ Paso 5. Tomar una decisión para el MVP
Para el MVP, recomiendo elegir la alternativa que proteja primero esta idea de la fuente: {source_ideas[0]}. Declara qué complejidad estás aceptando y qué señal te obligaría a cambiar la decisión.

### 🧪 Paso 6. Definir la verificación
Verificaremos la decisión con una evidencia relacionada directamente con el tema: una prueba, métrica, revisión de contrato, inspección de dependencias o demostración del flujo. El criterio debe responder: ¿cómo sabremos que la idea de la fuente está funcionando en nuestro sistema?

### 📦 Paso 7. Preparar la entrega
Guarda en GitHub el problema específico, las ideas de la fuente que aplicaste, la comparación, la decisión, los trade-offs y la evidencia. En el video de sustentación explícame qué entendiste, cómo lo aplicaste y qué riesgo aceptaste.
"""


def continuity(number, title):
    previous = TITLES[number - 2] if number > 1 else "la situación inicial del proyecto y sus actores"
    following = TITLES[number] if number < len(TITLES) else "la defensa final de la arquitectura evolutiva"
    if number == 1:
        return (
            "Esta es la primera conversación del recorrido. Vamos a construir el punto de partida: mirar el sistema como una decisión que afecta a personas, negocio y operación.",
            f"Cuando terminemos, tendrás el contexto necesario para avanzar hacia {following.lower()}."
        )
    if number == len(TITLES):
        return (
            f"Llegas a esta clase después de trabajar {previous.lower()}. Ahora reuniremos esas decisiones para mirar la arquitectura como una práctica completa.",
            "Esta clase cierra el recorrido y te prepara para defender tu expediente arquitectónico con criterio propio."
        )
    return (
        f"Vienes de trabajar {previous.lower()}. No vamos a repetirlo: lo usaremos como punto de partida para estudiar {title.lower()} y añadir una decisión nueva al expediente.",
        f"Lo que construyas aquí será la base para la próxima conversación: {following.lower()}."
    )


def navigation(number):
    links = []
    if number > 1:
        previous_title = TITLES[number - 2]
        links.append(f"[⬅️ Video anterior: {previous_title}](video-{number - 1:02d}.md)")
    if number < len(TITLES):
        next_title = TITLES[number]
        links.append(f"[➡️ Video siguiente: {next_title}](video-{number + 1:02d}.md)")
    return "\n\n".join(links)


def build_class_legacy(number, title):
    profile = profile_for(number)
    source = source_for(number, title)
    source_summary = source["summary"] or profile["case"]
    source_ideas = source["ideas"][:6] or profile["ideas"]
    source_questions = source["questions"][:4] or profile["questions"]
    source_conclusion = source["conclusion"] or "La decisión debe poder explicarse y verificarse en el contexto real del sistema."
    ideas = "\n".join(f"- {item}" for item in source_ideas + profile["ideas"][:1])
    questions = "\n".join(f"- {item}" for item in source_questions)
    lesson = topic_lesson(title, source)
    continuity_start, continuity_end = continuity(number, title)
    scene, challenge = class_scene(number, title, source)
    case_questions = source_case_questions(source, profile)
    source_goal = (source_summary.split(".")[0] or title).strip()
    sections = section_titles(title, source)
    activity = activity_for(number)
    code = code_example(number)

    if number == 1:
        opening = "Imagina que una plataforma controla un proceso del que dependen personas, dinero o seguridad. Una decisión aparentemente pequeña puede ampliar un riesgo hasta convertirlo en un incidente. Quiero que mires el caso con una pregunta: ¿qué responsabilidad aparece cuando el diseño puede afectar a personas?"
        central = "¿Qué consecuencias humanas y de negocio puede producir una decisión técnica que nadie examinó con suficiente rigor?"
        worked = "Para la plataforma logística, compare centralizar toda la asignación de rutas en un único componente con separar asignación, validación y gestión de incidentes. La primera opción puede ser rápida; la segunda puede evolucionar mejor, pero exige contratos y monitoreo. La decisión se justifica con volumen, criticidad, capacidad del equipo y consecuencias de una falla."
    elif number == 2:
        opening = "Que el software funcione hoy no significa que sea una solución sostenible. Hoy quiero que distingas entre entregar una funcionalidad y construir una base que el equipo pueda mantener cuando aparezcan nuevas reglas, usuarios o integraciones."
        central = "¿Qué diferencia existe entre entregar una funcionalidad y construir una solución que el equipo pueda sostener?"
        worked = "Suponga que la plataforma guarda pedidos, rutas y pagos en una sola clase. La primera versión puede funcionar, pero un cambio en la política de rutas obligaría a tocar pagos y notificaciones. Separar responsabilidades no es crear capas por moda: es proteger partes que cambian por razones diferentes."
    else:
        opening = f"Antes de entrar en {title.lower()}, quiero que identifiquemos qué cambia realmente en el sistema cuando aplicamos este concepto. No aprenderemos una palabra para repetirla en un diagrama: seguiremos sus consecuencias hasta llegar a una decisión defendible."
        central = f"¿Qué problema real resuelve {title.lower()} y cómo demostraríamos que la solución es adecuada?"
        worked = f"La fuente plantea lo siguiente: {source_summary} Ahora llévalo a la plataforma logística: {profile['case']}. Pregúntate qué parte del sistema conoce esa regla, qué información necesita y qué ocurriría si aumenta la carga, falla una dependencia o cambia la política del negocio."

    prompts = "\n".join([
        f"- **Te pregunto:** {source_questions[0] if source_questions else f'¿qué parte del problema pertenece realmente a {title.lower()}?'} **La razón:** así conectamos el tema con el problema real en lugar de aplicarlo por moda.",
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

## 🔗 Continuidad de la ruta
{continuity_start}

{continuity_end}

## 🎥 Escena de hoy
{scene}

## 🧭 Reto de la clase
{challenge}

## 🎯 Propósito de aprendizaje
Cuando terminemos, quiero que puedas explicar y aplicar esta idea de la fuente: {source_goal}. No te voy a pedir que repitas una definición. Te voy a pedir que la conectes con una situación, tomes una decisión y me digas qué consecuencias esperas.

## {sections['opening']}
Hoy vamos a trabajar una situación concreta: {source_summary} No quiero que empieces por un diagrama ni por una tecnología. Quiero que me expliques qué problema aparece aquí y por qué merece una decisión arquitectónica propia.

{opening}

Imagina que estamos frente a una pizarra. Yo te miro y te pregunto: ¿qué está pasando en este caso?, ¿quién depende de que esto funcione?, ¿qué información nos falta? No me respondas todavía con nombres de herramientas. Primero cuéntame qué problema ves en {title.lower()}. Esa primera respuesta me permite saber si estamos entendiendo el tema o si solo estamos repitiendo soluciones conocidas.

Antes de continuar, haz una pausa conmigo. ¿Quién usa el sistema? ¿Qué espera que ocurra? ¿Qué no puede fallar? ¿Qué cambio es probable durante la vida del producto? Te hago estas preguntas porque una arquitectura no se diseña en el vacío. Si todavía no puedes responderlas, no es un problema: acabamos de encontrar la información que necesitamos investigar antes de diseñar.

## {sections['question']}
{central}

## {sections['development']}
### {sections['source']}
La fuente describe este tema así: {source_summary}

Yo voy a traducir esa idea a una situación de diseño. No quiero que la recibas como una definición cerrada; quiero que observes qué problema intenta resolver, qué decisiones implica y qué evidencia necesitaríamos para confiar en ella.

### 1. Escuchemos la fuente y llevémosla al sistema
{lesson}

Mientras avanzamos, separa tres cosas: lo que la fuente afirma, lo que el caso logístico necesita y lo que tú decides hacer. Esa separación evita que una explicación general se convierta en una receta automática.

## {sections['teacher_questions']}
{prompts}

Estas no son preguntas para atraparte ni para calificarte de inmediato. Son las preguntas que te haría mientras conversamos frente a la pizarra. Si no tienes una respuesta todavía, dime qué dato te falta. En arquitectura, reconocer una duda y saber cómo investigarla demuestra más criterio que responder con seguridad algo que no podemos justificar.

## {sections['ideas']}
{ideas}
- El ejemplo debe documentarse con sus supuestos, trade-offs y evidencia de validación.

### {sections['teacher_reading']}
{source_conclusion}

Cuando conectamos esta conclusión con el proyecto, la pregunta deja de ser "¿conozco el concepto?" y pasa a ser "¿puedo usarlo para tomar una decisión concreta y explicar sus consecuencias?".

## {sections['example']}
Voy a resolver una situación contigo. {worked}

Fíjate en el razonamiento: el problema no es elegir una arquitectura moderna. El problema es mantener la promesa de entrega, proteger la información del cliente y responder ante cambios sin detener la operación. Desde ahí comparamos alternativas y explicamos por qué una es adecuada para este momento. Si cambian los datos del contexto, también puede cambiar nuestra decisión; eso no es una contradicción, es buena arquitectura.

## {sections['case']}
Ahora vamos a abandonar la explicación general y a trabajar las preguntas que trae esta fuente. No quiero que las respondas en abstracto: después de cada respuesta, dime qué cambia en la plataforma logística.

{case_questions}

Al terminar este recorrido tendrás una cadena de razonamiento propia del tema: idea de la fuente, situación afectada, decisión posible, costo aceptado y evidencia para comprobarla.

## {sections['workshop']}
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

{guided_answers(title, profile, source)}

## 🚀 Preparación para la siguiente clase
Revisa la evidencia, registra los supuestos aún no validados y lleva una pregunta abierta sobre costo, calidad, dependencia o evolución. Cada clase debe agregar una pieza al expediente arquitectónico.
"""


def build_class(number, title):
    profile = profile_for(number)
    source = source_for(number, title)
    summary = source["summary"] or profile["case"]
    ideas = source["ideas"][:6] or profile["ideas"]
    questions = source["questions"][:5] or profile["questions"]
    conclusion = source["conclusion"] or "La decisión debe poder explicarse y verificarse en el contexto real del sistema."
    previous, following = continuity(number, title)
    next_title = TITLES[number] if number < len(TITLES) else "la defensa final de la arquitectura evolutiva"
    video_navigation = navigation(number)
    source_title = source["title"]
    topic = title.lower()
    options = decision_options(number, title, profile, source)
    solution_steps = specific_solution_steps(number, title, profile, source)

    idea_walkthrough = "\n\n".join(
        f"### {index}. {idea}\n\n{explain_source_idea(index, idea, title, profile)}"
        for index, idea in enumerate(ideas, start=1)
    )
    source_questions = "\n".join(
        f"- **Te pregunto:** {question} **Lo que busco:** que relaciones la respuesta con una decisión observable del sistema."
        for question in questions
    )
    answer_lines = "\n".join(
        f"{index}. **{question}** Mi respuesta de partida es: {idea} En el proyecto, esto se comprueba con una evidencia concreta y no solamente con una opinión."
        for index, (question, idea) in enumerate(zip(questions, ideas), start=1)
    )
    evidence_steps = "\n".join([
        f"1. Escribe qué significa {topic} en tus propias palabras y relaciónalo con esta fuente: {summary.split('.')[0]}.",
        "2. Describe la situación del proyecto que puede verse afectada y quién recibe el impacto.",
        "3. Elige una decisión concreta; no escribas todavía una solución completa.",
        "4. Explica qué alternativa descartas y qué costo aceptas al elegir.",
        "5. Define una prueba, métrica, contrato, diagrama o registro que permita verificar la decisión.",
        "6. Guarda la evidencia, solicita una revisión de un compañero y registra qué cambiarías después de recibirla.",
    ])
    scene = f"La fuente consultada para esta clase es '{source_title}'. En nuestro recorrido la conectamos con el tema '{title}' porque queremos estudiar {topic} desde un problema real. La fuente plantea: {summary} En la plataforma logística, esto aparece cuando {profile['case']}. Primero entenderemos la fuente y después construiremos la decisión."

    return f"""# Video {number}: {title}

## Título
{title}

## 🧭 Punto de partida
{previous}

Al terminar esta conversación, tendrás una decisión nueva que enlaza con {next_title.lower()}.

## 🧭 Navegar por la ruta
{video_navigation}

## 🎥 La situación que vamos a resolver
{scene}

## 🎯 Lo que quiero que puedas hacer
Cuando terminemos, quiero que puedas explicar {topic} con tus propias palabras, reconocer cuándo es relevante, tomar una decisión razonada y mostrarme cómo comprobarías que funciona. Si solo puedes repetir una definición, todavía no hemos terminado la clase.

## 🎬 Entramos en la conversación
Te planteo el problema directamente: {summary.split('.')[0]}.

Ahora voy a separar contigo tres niveles: lo que la fuente afirma, el problema esencial que debemos resolver y las decisiones técnicas que podríamos tomar después. Si confundimos esos niveles, terminaremos usando una tecnología como respuesta a un problema que todavía no hemos definido.

Antes de mencionar herramientas, dime qué ves. ¿Cuál es la tensión principal? ¿Qué parte es un hecho y qué parte es una suposición? ¿Quién tendría problemas si esta decisión se toma mal? Tómate un momento. No estoy buscando una respuesta rápida; estoy buscando que aprendas a mirar el sistema antes de intervenirlo.

Ahora relaciónala con el proyecto: {profile['case']}. Aquí aparece el verdadero trabajo arquitectónico. No basta con nombrar un patrón o una tecnología; necesitas explicar qué problema resuelve, qué costo introduce y qué señal nos dirá si debemos cambiar de rumbo.

## 🧠 Desarrollo: sigamos las ideas de la fuente
La fuente no presenta {topic} como una receta universal. Presenta un conjunto de ideas que debemos convertir en decisiones. Vamos a recorrerlas una por una.

{idea_walkthrough}

Mientras avanzamos, yo te voy a interrumpir con una pregunta sencilla: “¿dónde se ve esto en el sistema?”. Si no puedes señalar un actor, una regla, un límite, un flujo, una dependencia o una evidencia, probablemente todavía estás hablando del concepto en abstracto.

## ❓ Preguntas que te haría durante la clase
{source_questions}

No quiero que respondas estas preguntas con una frase bonita. Para cada una, dime qué cambiarías en el diseño, qué riesgo estás aceptando y cómo podrías comprobar que tu respuesta es adecuada. Esa explicación es la parte que convierte una opinión en criterio arquitectónico.

{options}

## 🏗️ Un ejemplo trabajado contigo
Voy a tomar una situación del proyecto: {profile['case']}. La fuente afirma que {ideas[0]}. Entonces la primera decisión no es comprar una herramienta; es decidir qué responsabilidad debe quedar explícita y qué información necesitamos observar.

Si eliges una solución sencilla, debes decir qué límite estás protegiendo y qué crecimiento podría dejarla corta. Si eliges una solución más compleja, debes justificar quién la operará, qué problema adicional resuelve y qué evidencia evita que se convierta en complejidad innecesaria. En ambos casos, yo esperaría que documentaras la alternativa descartada y la condición que te haría revisar la decisión.

La conclusión de la fuente es clara: {conclusion} Mi pregunta para ti es: ¿qué parte de esa conclusión cambia la forma en que estás diseñando la plataforma?

## ✍️ Tu trabajo durante la clase
Ahora construye tu propia respuesta. No copies el ejemplo anterior; cambia el contexto, el actor afectado o la restricción y comprueba si tu decisión sigue siendo válida.

{evidence_steps}

Tu entrega debe contener una explicación breve, un artefacto visible y una justificación. El artefacto puede ser un diagrama, una tabla de decisión, un ADR, un contrato, una prueba, una métrica, un fragmento C# o una evidencia de ejecución, según el tema de esta clase.

{solution_steps}

## 🗣️ Comprobemos juntos tus respuestas
Estas son respuestas orientadoras, no una clave para copiar:

{answer_lines}

La respuesta será sólida cuando conecte tres niveles: lo que dice la fuente, lo que necesita el caso y lo que decidiste implementar. Si falta uno de ellos, vuelve a revisar tu razonamiento.

## ⚠️ Lo que suele salir mal
- Repetir la definición sin mostrar dónde aparece en el sistema.
- Elegir una tecnología antes de explicar el riesgo que se quiere controlar.
- Ocultar el costo de la alternativa elegida.
- Entregar un diagrama o código sin explicar qué decisión representa.
- Declarar que la solución funciona sin definir cómo se comprobará.

## ✅ Cierre de nuestra conversación
Quiero que cierres esta clase diciéndome, con tus palabras, qué cambió en tu forma de mirar el sistema. Después resume tu decisión en este orden: problema, evidencia de la fuente, alternativa, elección, costo aceptado y verificación.

La idea que debes llevarte no es “aprendí otro término”. Es esta: ahora puedes mirar {topic}, relacionarlo con un problema real y defender una decisión sin esconder sus límites. Esa capacidad será necesaria cuando avancemos hacia {next_title.lower()}.

## 🤔 Para pensar antes de continuar
{chr(10).join(f"- {question}" for question in questions)}

## 📦 Evidencia para el repositorio
Guarda el resultado en la carpeta de {activity_for(number)}. Incluye el contexto, la decisión, la alternativa descartada, los trade-offs, el artefacto producido y la forma de verificación. En tu video de sustentación, explica qué entendiste de la fuente y cómo lo convertiste en una decisión propia.
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
