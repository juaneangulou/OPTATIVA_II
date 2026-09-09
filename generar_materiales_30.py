from pathlib import Path
import re

BASE = Path(r"C:\proj\itm\OPTATIVA_II")
SOURCE = BASE / "materiales" / "material_cursos_raw_summary" / "cursos"
OUT = BASE / "materiales" / "materiales_por_video" / "serie_30_videos"
OUT.mkdir(parents=True, exist_ok=True)

FUNDAMENTOS = [
    "video-01-decisiones-de-arquitectura-y-consecuencias-reales.md",
    "video-02-por-que-importa-la-arquitectura.md",
    "video-03-rol-del-arquitecto-de-software.md",
    "video-04-comunicar-la-arquitectura.md",
    "video-05-documentar-decisiones-y-mantener-claridad.md",
    "video-06-arquitectura-como-responsabilidad-humana.md",
    "video-07-escalabilidad-seguridad-y-etica.md",
    "video-08-fundamentos-de-diseno-y-principios-de-arquitectura.md",
    "video-09-acoplamiento-cohesion-y-calidad-estructural.md",
    "video-10-modelado-de-dominios-y-limites-de-contexto.md",
    "video-11-monolito-vs-arquitectura-distribuida.md",
    "video-12-microservicios-y-organizacion-por-dominios.md",
    "video-13-apis-y-contratos-de-integracion.md",
    "video-14-infraestructura-despliegue-y-entorno-de-ejecucion.md",
    "video-15-observabilidad-y-monitoreo-de-sistemas.md",
    "video-16-seguridad-datos-sensibles-y-privacidad.md",
    "video-17-testing-y-validacion-de-arquitectura.md",
    "video-18-devops-y-automatizacion-de-entrega.md",
    "video-19-estructura-de-software-y-evolucion-del-sistema.md",
    "video-20-riesgos-costos-y-decisiones-bajo-incertidumbre.md",
    "video-21-estrategia-tecnologica-y-roadmap.md",
    "video-22-comunicacion-liderazgo-y-negociacion-tecnica.md",
    "video-23-arquitectura-con-impacto-social-y-valor-real.md",
    "video-24-cierre-del-curso.md",
]

APLICADA = [
    "video-01-intuicion-vs-metodo.md",
    "video-02.md",
    "video-03.md",
    "video-04-principios-calidad-y-tradeoffs.md",
    "video-05-ia-vision-y-liderazgo.md",
    "video-06-arquitectura-y-decisiones-de-diseno.md",
    "video-07-escalabilidad-y-rendimiento.md",
    "video-08-resiliencia-y-tolerancia-a-fallos.md",
    "video-09-seguridad-y-privacidad.md",
    "video-10-integracion-y-contratos-de-api.md",
    "video-11-microservicios-y-dominios.md",
    "video-12-datos-y-almacenamiento.md",
    "video-13-observabilidad-y-operabilidad.md",
    "video-14-devops-despliegue-y-automatizacion.md",
    "video-15-arquitectura-moderna-y-liderazgo.md",
    "video-16-documentacion-y-decisiones-explicitas.md",
    "video-17-cultura-de-arquitectura.md",
    "video-18-comunicacion-y-negociacion-tecnica.md",
    "video-19-madurez-arquitectonica.md",
    "video-20-cierre-del-curso.md",
    "video-21-diseno-para-cambio-y-evolucion.md",
    "video-22-calidad-de-servicio-y-experiencia-de-usuario.md",
    "video-23-estrategia-tecnologica-y-roadmap.md",
    "video-24-evaluacion-de-tecnologias-y-stack.md",
    "video-25-riesgos-costos-y-sostenibilidad-financiera.md",
    "video-26-arquitectura-para-equipos-distribuidos.md",
    "video-27-decisiones-bajo-incertidumbre.md",
    "video-28-arquitectura-con-impacto-social-y-etico.md",
    "video-29-cierre-profesional-y-legado-arquitectonico.md",
]

GROUPS = [
    ("Qué es la arquitectura y por qué importa", [1, 2]),
    ("Rol del arquitecto y comunicación", [3, 4]),
    ("Documentación y decisiones explícitas", [5, 23]),
    ("Responsabilidad, escalabilidad, seguridad y ética", [6, 7]),
    ("Principios de diseño, acoplamiento y cohesión", [8, 9]),
    ("Dominios y límites de contexto", [10, 12]),
    ("Monolitos, sistemas distribuidos y microservicios", [11, 12]),
    ("APIs, contratos e infraestructura", [13, 14]),
    ("Observabilidad, seguridad y privacidad", [15, 16]),
    ("Testing, DevOps y entrega continua", [17, 18]),
    ("Evolución, riesgos y costos", [19, 20]),
    ("Estrategia tecnológica y roadmap", [21, 21]),
    ("Liderazgo, negociación e impacto social", [22, 23]),
    ("Cierre de fundamentos y transición", [24, 24]),
    ("Método arquitectónico e inteligencia artificial", [25, 26]),
    ("Monorepos, trunk-based development y calidad", [27, 28]),
    ("BDD y modelo C4", [29, 30]),
    ("Documentación viva y revisión con IA", [31, 32]),
    ("Architecture.md y Domain Driven Design", [33, 34]),
    ("Premortem y pruebas de arquitectura", [35, 36]),
    ("Métricas y migración Strangler Fig", [37, 38]),
    ("Bases de datos y API Gateway", [39, 40]),
    ("Bounded Context e infraestructura como código", [41, 42]),
    ("Mensajes, eventos y productor-consumidor", [43, 44]),
    ("Dead Letter Queue y consumidores en tiempo real", [45, 46]),
    ("Process Manager, Durable State y Event Sourcing", [47, 48]),
    ("Máquinas de estado y seguridad de aplicaciones", [49, 50]),
    ("Fitness Functions, OpenTelemetry y caos", [51, 52]),
    ("Criterio, liderazgo y arquitectura responsable", [53, 53]),
    ("Cierre y defensa de la arquitectura", [53]),
]

# Correct the two intentional cross-course groupings and keep 30 outputs.
GROUPS[2] = ("Documentación y decisiones explícitas", [5, 40])
GROUPS[5] = ("Dominios y límites de contexto", [10, 45])

PLATZI_FUND = "https://platzi.com/cursos/fundamentos-arquitectura-software/"
PLATZI_APP = "https://platzi.com/cursos/software-avanzado/"
FUND_URLS = [
    "decisiones-de-arquitectura-de-software-y/", "ia-en-arquitectura-herramienta-o-amenaza/", "78360-que-hace-un-arquitecto-de-software/", "problemas-esenciales-vs-accidentales-en/", "malas-practicas-de-arquitectura-y-como-e/", "espacio-de-problema-vs-solucion-en-arqui/", "requisitos-funcionales-y-no-funcionales/", "costo-total-de-operacion-en-arquitectura/", "alineacion-de-arquitectura-de-software-c/", "mindset-del-arquitecto-que-abraza-el-cam/", "como-elegir-un-estilo-arquitectonico-sin/", "arquitectura-cliente-servidor-fundamento/", "que-son-las-arquitecturas-monoliticas-y/", "arquitecturas-orientadas-a-servicios-con/", "como-funcionan-los-eventos-en-sistemas-d/", "costos-ocultos-de-los-microservicios/", "paradigmas-y-principios-solid-explicados/", "que-hace-limpia-a-una-arquitectura-de-so/", "patrones-de-software-para-arquitectos/", "arquitectura-mvp-de-telegram-a-remarkabl/", "evolucionar-un-mvp-sin-rearquitectar-des/", "evolucion-del-software-personal-hacia-el/", "preguntas-clave-que-todo-arquitecto-de-s/", "consejos-para-desarrollar-carrera-como-a/",
]
APP_URLS = [
    "intuicion-vs-metodo-en-arquitectura-de-s/", "como-analizar-una-licitacion-real-con-ia/", "monorepos-con-pantsbuild-en-proyectos-re/", "trunk-based-development-con-rulesets-en/", "behavior-driven-development-para-alinear/", "modelo-c4-para-diagramar-arquitecturas/", "quarto-como-sitio-de-documentacion-viva/", "agentes-de-ia-que-revisan-tu-codigo-en-g/", "estructura-del-archivo-architecture-md-p/", "domain-driven-design-para-arquitectura-l/", "tecnicas-pre-mortem-y-cinco-why-para-pre/", "como-el-premortem-guia-tus-tests-de-arqu/", "metricas-cuantitativas-para-evaluar-arqu/", "strangler-fig-para-migrar-arquitecturas/", "migraciones-de-base-de-datos-con-flyway/", "api-gateway-como-capa-de-abstraccion-en/", "bounded-context-y-context-maps-en-micros/", "infraestructura-como-codigo-en-monorepos/", "mensajes-vs-eventos-en-microservicios/", "patron-productor-consumidor-vs-fan-in-y/", "dead-letter-queue-en-productor-consumido/", "patron-comparing-consumers-para-procesam/", "que-es-el-patron-process-manager/", "durable-state-vs-event-sourcing-en-siste/", "maquinas-de-estado-finito-en-el-front-en/", "tecnicas-sast-dast-y-pen-testing-para-se/", "fitness-functions-para-medir-tu-arquitec/", "observabilidad-en-sistemas-con-opentelem/", "sabiduria-y-criterio-en-arquitectura-de/",
]


def section(text, name):
    match = re.search(rf"^##\s+{re.escape(name)}\s*$\n(.*?)(?=^##\s+|\Z)", text, re.M | re.S)
    return match.group(1).strip() if match else ""


def parse(path):
    text = path.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+.*?:\s*(.*)$", text, re.M)
    title = title_match.group(1).strip() if title_match else path.stem
    ideas = [line[2:].strip() for line in section(text, "Ideas principales").splitlines() if line.startswith("- ")]
    questions = [line[2:].strip() for line in section(text, "Preguntas para reflexión").splitlines() if line.startswith("- ")]
    return {
        "title": title,
        "summary": section(text, "Resumen"),
        "ideas": ideas,
        "conclusion": section(text, "Conclusión"),
        "questions": questions,
        "path": path,
    }


def load_sources():
    sources = []
    for filename in FUNDAMENTOS:
        sources.append(parse(SOURCE / "fundamentos-arquitectura-software" / "videos" / filename))
    for filename in APLICADA:
        sources.append(parse(SOURCE / "arquitectura-software-aplicada" / "videos" / filename))
    return sources


def source_url(source):
    if "fundamentos" in str(source["path"]):
        number = FUNDAMENTOS.index(source["path"].name)
        return PLATZI_FUND + FUND_URLS[number]
    number = APLICADA.index(source["path"].name)
    return PLATZI_APP + APP_URLS[number]


def logistics_application(title, ideas, number):
    focus = ideas[0] if ideas else title
    return f"""Para estudiar **{title.lower()}**, vamos a seguir el recorrido de una operación logística y detenernos en el punto donde este tema cambia la decisión. La plataforma recibe un pedido, coordina inventario, propone una ruta y comunica el resultado; el foco de hoy es: {focus}

1. **Situación propia del tema:** identifica qué puede fallar cuando aplicamos {title.lower()} al flujo.
    2. **Actor prioritario de {title.lower()}:** decide si la consecuencia principal la recibe el cliente, el operador, el repartidor, soporte o el equipo técnico.
    3. **Regla o calidad protegida en {title.lower()}:** escribe la condición que debe permanecer verdadera y relaciónala con {focus.lower()}.
    4. **Punto de decisión para {title.lower()}:** delimita qué queda dentro del módulo responsable, qué cruza a otro componente y qué se delega a una dependencia.
    5. **Evidencia de {title.lower()}:** elige el artefacto que mejor pruebe esta decisión: diagrama, ADR, contrato, código, prueba, métrica, registro o experimento.

Para resolver el caso de **{title.lower()}**, empieza por el flujo que mejor represente el tema. Señala el componente responsable, la dependencia que puede fallar y el resultado que espera el actor prioritario. Después compara una solución sencilla para el MVP con otra más robusta. Tu elección debe explicar qué gana, qué sacrifica y cuándo tendría que revisarse.
"""


def answer_for_question(question, idea, title, actor, need, rule):
    q = question.lower()
    if any(word in q for word in ("impacto", "consecuencia", "afectar", "responsabilidad")):
        return f"La decisión sobre {title.lower()} afecta directamente a {actor}: necesita {need}. Por eso protegería esta regla: {rule}. En la arquitectura cambiaría la responsabilidad para que el componente que conoce esa regla la valide antes de comunicar el resultado. Acepto el costo de agregar una validación y una prueba porque el riesgo de afectar a {actor} es mayor. Lo verificaría simulando el caso y comprobando el resultado observable para ese actor."
    if any(word in q for word in ("fragil", "frágil", "diseño", "debil", "débil")):
        return f"La parte frágil de {title.lower()} es la que permite que {actor} reciba un resultado incorrecto: {need}. La corregiría colocando la regla '{rule}' en un límite explícito, en lugar de dejarla repartida entre la interfaz y la infraestructura. El costo será reorganizar el flujo y agregar pruebas; la evidencia será un cambio aislado que no rompa los demás módulos."
    if any(word in q for word in ("crecimiento", "crecer", "futuro", "escalabilidad", "mañana")):
        return f"Si el sistema crece en el tema de {title.lower()}, {actor} seguirá necesitando {need}. No elegiría una solución distribuida automáticamente; primero mediría carga, latencia y errores. Mantendría la regla '{rule}' en un módulo claro y escalaría solo el punto que demuestre saturación. La decisión se verifica con una prueba de carga y una métrica acordada."
    if any(word in q for word in ("seguridad", "privacidad", "datos", "ética", "ético")):
        return f"La prioridad de {title.lower()} es proteger a {actor}, porque {need}. Aplicaría un control que impida violar la regla '{rule}', limitaría el acceso a los datos necesarios y registraría los intentos rechazados. El costo es mayor complejidad de autorización y auditoría; lo comprobaría con pruebas de acceso permitido y denegado."
    if any(word in q for word in ("costo", "opción", "alternativa", "decisión")):
        return f"Para {title.lower()}, elegiría la alternativa que garantice que {actor} pueda {need}. La opción sencilla reduce el costo inicial, pero puede dejar débil la regla '{rule}'; la opción más estructurada cuesta más, pero facilita probarla y cambiarla. Para el MVP escogería la segunda solo si el riesgo es crítico y documentaría la condición de revisión."
    return f"Para {title.lower()}, {actor} necesita {need}. La respuesta concreta es proteger la regla '{rule}' dentro del componente responsable, documentar la decisión y comprobarla con una prueba o evidencia observable. No basta relacionar la pregunta con el diseño: debemos mostrar qué cambia en el sistema y qué resultado esperamos."


def answered_questions(source_items, ideas, title):
    actors = [
        ("el cliente", "recibir un estado de entrega confiable", "no mostrar una entrega como completada sin evidencia válida"),
        ("el operador logístico", "reasignar una ruta sin perder el historial del pedido", "conservar trazabilidad de cada cambio"),
        ("el repartidor", "recibir una instrucción vigente y consistente", "evitar dos asignaciones activas para la misma entrega"),
        ("el equipo de soporte", "reconstruir qué ocurrió durante un incidente", "tener eventos, errores y estados observables"),
        ("el equipo técnico", "modificar una parte sin romper las demás", "mantener contratos y pruebas del flujo crítico"),
    ]
    pairs = []
    idea_index = 0
    for item in source_items:
        for question in item["questions"][:2]:
            idea = ideas[idea_index % len(ideas)] if ideas else "la decisión arquitectónica del tema"
            clean_idea = idea.rstrip(".!? ").lower()
            actor, need, rule = actors[idea_index % len(actors)]
            answer = answer_for_question(question, clean_idea, title, actor, need, rule)
            pairs.append(f"### ❓ {question}\n\n**Respuesta concreta:** {answer}")
            idea_index += 1
    return "\n\n".join(pairs)


def activity_solution(title, ideas):
    main_idea = (ideas[0] if ideas else title).rstrip(".!? ")
    return f"""## 🛠️ Cómo resolver la actividad

1. **Comprende el tema:** explica con tus palabras qué significa {title.lower()} y qué idea principal de las fuentes lo justifica.
    2. **Delimita el caso de {title.lower()}:** describe qué ocurre en la plataforma logística, qué actor recibe el impacto y qué regla o atributo de calidad está en riesgo.
    3. **Formula dos opciones para {title.lower()}:** Opción A, una solución sencilla para el MVP; Opción B, una solución con mayor separación, automatización o control.
    4. **Compara las opciones de {title.lower()}:** analiza costo inicial, complejidad operativa, seguridad, rendimiento, mantenibilidad y facilidad de cambio.
5. **Decide:** elige la opción que proteja primero esta idea: {main_idea}. Declara qué sacrificas y qué condición obligaría a revisar la decisión.
6. **Construye la evidencia:** produce el artefacto que mejor responda a {title.lower()}: ADR, diagrama, contrato, fragmento C#, prueba, métrica o plan de evolución.
7. **Comprueba y sustenta:** ejecuta la prueba o revisión de {title.lower()}, registra el resultado y explica en tu video qué tomaste de cada fuente y cómo lo aplicaste.

**Respuesta modelo para {title}:** una solución no se justifica diciendo “es mejor”. Se justifica explicando el problema, comparando alternativas, mostrando el costo aceptado y presentando evidencia observable.
"""


def make_material(number, title, source_items):
    summaries = "\n\n".join(f"**Fuente {i}: {item['title']}**\n{item['summary']}" for i, item in enumerate(source_items, 1))
    ideas = []
    for item in source_items:
        ideas.extend(item["ideas"][:4])
    ideas = list(dict.fromkeys(ideas))
    idea_text = "\n".join(f"- {idea}" for idea in ideas)
    conclusions = "\n\n".join(item["conclusion"] for item in source_items if item["conclusion"])
    questions = []
    for item in source_items:
        questions.extend(item["questions"][:2])
    question_text = "\n".join(f"- {question}" for question in list(dict.fromkeys(questions)))
    application = logistics_application(title, ideas, number)
    answers = answered_questions(source_items, ideas, title)
    solution = activity_solution(title, ideas)
    focus = (ideas[0] if ideas else title).rstrip(".!? ")
    activity_steps = "\n".join([
        f"1. Explica con tus palabras qué significa {title.lower()} y qué fuente respalda esa interpretación.",
        f"2. Describe una situación de la plataforma logística donde aparezca: {focus.lower()}.",
        f"3. Identifica el actor que recibe el impacto de {title.lower()} y la regla que no puede romperse.",
        f"4. Propón una solución mínima y otra más robusta para {title.lower()}; compara sus costos y riesgos.",
        f"5. Elige una opción para {title.lower()}, declara qué sacrificas y define la condición que obligaría a revisarla.",
        f"6. Produce la evidencia propia de este tema: {title.lower()} debe quedar visible en un diagrama, ADR, contrato, código, prueba o métrica.",
    ])
    evidence_text = f"Guarda la explicación de {title.lower()}, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. En la grabación explica qué tomaste de cada fuente y cómo esa idea cambia el diseño de la plataforma logística."
    source_links = "\n".join(f"- [{item['title']}]({source_url(item)})" for item in source_items)
    previous = f"video-{number - 1:02d}.md" if number > 1 else None
    following = f"video-{number + 1:02d}.md" if number < 30 else None
    navigation = []
    if previous:
        navigation.append(f"[⬅️ Video anterior]({previous})")
    if following:
        navigation.append(f"[➡️ Video siguiente]({following})")
    return f"""# Video {number:02d}: {title}

## Fuentes oficiales
{source_links}

## 🔗 Navegación
{' | '.join(navigation)}

## Propósito
Esta clase combina las fuentes anteriores para resolver un problema específico: {title.lower()}. El objetivo es mostrar qué idea aporta cada fuente, cómo se complementan y qué decisión concreta permiten tomar en la plataforma logística.

## Resumen integrado
{summaries}

## Ideas que debes conservar
{idea_text}

## Cómo se conectan las fuentes
La primera fuente aporta el punto de partida y la segunda amplía o contrasta ese punto. Compáralas desde este tema: {title.lower()}. Pregúntate qué problema resuelve cada una, dónde coinciden y qué decisión nueva aparece cuando se leen juntas.

## Aplicación al caso logístico
{application}

## Actividad de construcción
{activity_steps}

## Respuestas a las preguntas
{answers}

{solution}

## Conclusiones de las fuentes
{conclusions}

## Preguntas para preparar la grabación
{question_text}

## Evidencia para el repositorio
{evidence_text}
"""


def main():
    sources = load_sources()
    assert len(sources) == 53
    for index, (title, ranges) in enumerate(GROUPS, start=1):
        selected = []
        for ref in ranges:
            selected.append(sources[ref - 1])
        (OUT / f"video-{index:02d}.md").write_text(make_material(index, title, selected), encoding="utf-8")
    readme = ["# Serie de 30 videos combinados", "", "Cada material combina resúmenes de los cursos oficiales de Platzi en orden pedagógico.", ""]
    readme.extend(f"- [Video {i:02d}: {title}](video-{i:02d}.md)" for i, (title, _) in enumerate(GROUPS, 1))
    (OUT / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")
    print(f"Generados {len(GROUPS)} materiales en {OUT}")


if __name__ == "__main__":
    main()
