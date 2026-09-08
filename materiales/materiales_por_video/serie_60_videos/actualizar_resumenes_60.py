from pathlib import Path

root = Path(r"C:\proj\itm\OPTATIVA_II\materiales\materiales_por_video\serie_60_videos")
root.mkdir(parents=True, exist_ok=True)

fundamentos = [
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

aplicada = [
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

titles = fundamentos + aplicada
assert len(titles) == 60, f"Se esperaban 60 videos, pero hay {len(titles)}"


profiles = {
    "fundamentos": {
        "purpose": "convertir una necesidad del negocio en una decisión arquitectónica explícita y verificable",
        "case": "la plataforma logística debe recibir pedidos, asignar rutas y responder ante retrasos sin perder trazabilidad",
        "ideas": [
            "La decisión debe partir del problema, los usuarios y las restricciones, no de una tecnología preferida.",
            "Cada alternativa debe compararse por valor, costo, riesgo y capacidad de evolución.",
            "Los supuestos deben quedar escritos para poder validarlos con evidencia.",
        ],
        "questions": [
            "¿Qué evidencia del negocio justifica esta decisión?",
            "¿Qué alternativa se descartó y por qué?",
            "¿Qué cambio futuro podría obligar a revisar la solución?",
        ],
    },
    "estructura": {
        "purpose": "organizar responsabilidades y dependencias para que el sistema pueda crecer sin propagar cambios",
        "case": "pedidos, inventario, rutas y notificaciones deben colaborar sin compartir toda su lógica interna",
        "ideas": [
            "Una frontera útil define responsabilidad, contrato y propietario.",
            "La estructura elegida debe ser proporcional al tamaño del equipo y al riesgo operativo.",
            "La dirección de las dependencias protege las reglas importantes frente a detalles externos.",
        ],
        "questions": [
            "¿Qué responsabilidad pertenece realmente a cada módulo?",
            "¿Qué dependencia sería más costosa de cambiar?",
            "¿La estructura propuesta resuelve un problema real o agrega complejidad?",
        ],
    },
    "dominio": {
        "purpose": "proteger las reglas del negocio dentro de un modelo claro, comprobable y separado de la infraestructura",
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
    "aplicacion": {
        "purpose": "llevar una decisión arquitectónica a un flujo ejecutable, documentado y mantenible",
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
        "purpose": "evaluar el sistema en ejecución y prepararlo para fallos, cambios, ataques y crecimiento",
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


def get_profile(n: int):
    if n <= 9:
        return profiles["fundamentos"]
    if n <= 16 or n in (26, 27, 28, 46):
        return profiles["estructura"]
    if n <= 29 or n in (39, 53, 54):
        return profiles["dominio"]
    if n <= 38 or n in (43, 44, 45, 47, 48, 49, 51, 52):
        return profiles["aplicacion"]
    return profiles["operacion"]


def build_template(n: int, title: str) -> str:
    profile = get_profile(n)
    idea_lines = "\n".join(f"- {idea}" for idea in profile["ideas"])
    question_lines = "\n".join(f"- {question}" for question in profile["questions"])
    technical_example = ""
    if n == 13:
        technical_example = '''\n## Ejemplo en C#\n```csharp\npublic sealed record OrderId(Guid Value);\npublic sealed record Order(OrderId Id, decimal Total);\n```\n\nEl dominio expresa identidad y reglas sin depender de una base de datos o de una API.\n'''
    elif n == 14:
        technical_example = '''\n## Ejemplo en C#\n```csharp\npublic record CreateOrderRequest(string CustomerEmail, decimal Total);\npublic record OrderResponse(Guid Id, decimal Total, string Status);\n```\n\nEl contrato de integración define entradas y salidas estables para los consumidores.\n'''
    elif n == 27:
        technical_example = '''\n## Ejemplo en C#\n```csharp\npublic interface IOrderRepository\n{\n    Task SaveAsync(Order order);\n}\n```\n\nLa aplicación depende de una abstracción y la infraestructura implementa el adaptador.\n'''
    elif n == 28:
        technical_example = '''\n## Ejemplo en C#\n```csharp\npublic sealed class Order\n{\n    public bool IsPaid { get; private set; }\n\n    public void MarkAsPaid() => IsPaid = true;\n}\n```\n\nLa entidad protege una transición válida del negocio.\n'''
    elif n == 39:
        technical_example = '''\n## Ejemplo en C#\n```csharp\npublic sealed class PlaceOrderUseCase\n{\n    private readonly IOrderRepository _repository;\n\n    public PlaceOrderUseCase(IOrderRepository repository) => _repository = repository;\n}\n```\n\nEl caso de uso coordina el flujo y recibe sus dependencias desde el borde.\n'''

    return f'''# Video {n}: {title}

## Título
{title}

## Resumen
Este video estudia {title.lower()} con el objetivo de {profile["purpose"]}. El tema se conecta con el proyecto de la plataforma logística porque {profile["case"]}. La discusión no se limita a nombrar un patrón o una herramienta: exige identificar el problema, establecer criterios y anticipar las consecuencias de la decisión.

En la práctica, el equipo debe explicar qué cambia en el diseño, qué costo introduce y cómo comprobará que la solución funciona. Una decisión útil es la que puede comunicarse, implementarse gradualmente y revisarse cuando aparezca nueva evidencia.

## Ideas principales
{idea_lines}
- El ejemplo debe documentarse junto con sus supuestos, trade-offs y evidencia de validación.
{technical_example}
## Conclusión
{title} aporta una forma concreta de trabajar sobre la arquitectura del sistema. Su valor aparece cuando conecta el contexto del negocio con una estructura implementable, medible y capaz de evolucionar. Para el caso logístico, la decisión debe dejar claro qué comportamiento se protege, qué dependencias se aceptan y cómo se responderá ante cambios o fallos.

## Preguntas para reflexión
{question_lines}
'''

# Limpiar archivos sobrantes
for extra in root.glob("video-61.md"):
    extra.unlink()

# Generar README
readme_lines = [
    "# Ruta de 60 videos de la materia",
    "",
    "## Curso 1: Fundamentos de Arquitectura de Software",
    ""
]
for i, title in enumerate(fundamentos, start=1):
    readme_lines.append(f"- [Video {i}: {title}](video-{i:02d}.md)")

readme_lines.extend(["", "## Curso 2: Arquitectura de Software Aplicada", ""])
for i, title in enumerate(aplicada, start=1):
    real_index = i + len(fundamentos)
    readme_lines.append(f"- [Video {real_index}: {title}](video-{real_index:02d}.md)")

readme_lines.extend([
    "",
    "## Nota",
    "Esta ruta organiza la materia en 60 materiales de estudio, con un nivel más detallado y práctico para clase. La estructura mantiene la lógica de la fuente documental base y mejora la profundidad de cada resumen, explicando además ejemplos, implicaciones y reflexiones con mayor rigor académico.",
])
(root / "README.md").write_text("\n".join(readme_lines) + "\n", encoding="utf-8")

# Generar videos
for i, title in enumerate(titles, start=1):
    (root / f"video-{i:02d}.md").write_text(build_template(i, title), encoding="utf-8")

print(f"Regenerados {len(titles)} videos y README en {root}")
