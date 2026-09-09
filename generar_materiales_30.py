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
    source_links = "\n".join(f"- [Platzi: {item['title']}]({source_url(item)})" for item in source_items)
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
Esta clase combina las fuentes anteriores en una sola explicación para el proyecto de la plataforma logística. El objetivo es comprender qué ideas comparten, qué diferencias tienen y qué decisión arquitectónica permiten tomar.

## Resumen integrado
{summaries}

## Ideas que debes conservar
{idea_text}

## Cómo se conectan las fuentes
Lee las fuentes como partes de una misma conversación. Identifica qué problema presenta cada una, qué concepto agrega y qué consecuencia aparece cuando se aplica al sistema. No copies las conclusiones por separado: construye una explicación que muestre la relación entre ellas.

## Aplicación al caso logístico
Analiza cómo este tema afecta pedidos, inventario, ruteo, entregas, notificaciones, incidentes y operación. Elige un flujo concreto y explica qué responsabilidad, dependencia o atributo de calidad queda protegido.

## Actividad de construcción
1. Resume en tus palabras la idea central de cada fuente.
2. Combina esas ideas en un problema arquitectónico único.
3. Propón dos alternativas de solución.
4. Compara costo inicial, calidad, riesgo, operación y facilidad de cambio.
5. Elige una alternativa para el MVP y declara qué condición obligaría a revisarla.
6. Produce una evidencia: ADR, diagrama, contrato, código C#, prueba, métrica o plan de evolución.

## Respuesta orientadora
Una respuesta sólida conecta las fuentes con el caso. No basta decir que una tecnología es mejor: debes explicar qué problema resuelve, qué costo introduce, qué alternativa descartas y cómo comprobarás la decisión.

## Conclusiones de las fuentes
{conclusions}

## Preguntas para preparar la grabación
{question_text}

## Evidencia para el repositorio
Guarda la explicación integrada, la comparación de alternativas, la decisión tomada, los trade-offs y el artefacto producido. El video que grabes debe explicar qué tomaste de cada fuente y cómo lo convertiste en una decisión propia para el proyecto.
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
