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


def video_three_material(source_items, source_links, navigation):
    first, second = source_items
    return f"""# Video 03: Documentación y decisiones explícitas

## Fuentes oficiales
{source_links}

## 🔗 Navegación
{navigation}

## Propósito
En esta clase vas a aprender a convertir una decisión que hoy está en la cabeza de una persona en un registro que el equipo pueda leer, discutir y revisar dentro de seis meses. No vamos a hablar de documentación como burocracia: vamos a usarla para evitar que el proyecto dependa de la memoria de quien escribió el código.

## Qué explican las fuentes
La primera fuente plantea que una decisión arquitectónica debe dejar claro el contexto, la intención, las restricciones, los riesgos y las alternativas descartadas. La segunda amplía la idea: documentar no es llenar páginas, sino registrar lo que permite a otra persona entender por qué el sistema se construyó de esa manera.

Las dos fuentes convergen en una regla: una decisión no está realmente tomada hasta que el equipo puede responder qué problema resolvía, qué opción eligió, qué costo aceptó y cuándo debería revisarla.

## Escena de la plataforma logística
El lunes, la arquitecta que definió la integración con el proveedor de mapas sale de vacaciones. El miércoles, el proveedor empieza a responder lento. El operador logístico informa que las rutas llegan tarde; soporte ve errores, pero nadie sabe por qué existe un timeout de dos segundos ni qué alternativa se descartó.

Aquí el actor principal no es el repartidor: es **el equipo de soporte y el nuevo desarrollador**. Ambos necesitan reconstruir una decisión sin depender de la memoria de la arquitecta. La regla que debemos proteger es: **toda integración crítica debe tener un registro visible de propósito, límite, timeout, alternativa y responsable**.

## La decisión que vamos a documentar
La plataforma debe consultar un proveedor externo de mapas para estimar rutas. Tenemos dos opciones:

### Opción A: llamar al proveedor desde el módulo de pedidos
Es rápida de implementar y parece suficiente para el MVP. El riesgo es que pedidos conozca detalles del proveedor, que el timeout esté repartido en varios lugares y que una caída del servicio bloquee la creación de pedidos.

### Opción B: crear un adaptador de rutas con un contrato explícito
El módulo de pedidos solicita una estimación mediante una interfaz. El adaptador contiene la URL, credenciales, timeout, reintentos y transformación de errores. El costo es crear una capa adicional, pero el proveedor puede cambiar sin contaminar la regla de negocio.

Para este caso elegiría la opción B. No porque “las capas sean mejores”, sino porque el proveedor es externo, puede fallar y soporte necesita saber dónde observar y cambiar el comportamiento.

## El ADR que construiríamos juntos
Un ADR puede ser breve. Para esta decisión, escribe lo siguiente:

```markdown
# ADR-001: Aislar la estimación de rutas detrás de un adaptador

## Contexto
El proveedor de mapas puede responder lento o no estar disponible.

## Decisión
El caso de uso de crear pedido dependerá de IRouteEstimator.
La infraestructura implementará ese contrato con el proveedor externo.

## Alternativas descartadas
Llamar la API de mapas directamente desde el módulo de pedidos.

## Consecuencias
Ganamos aislamiento y pruebas más simples. Aceptamos mantener un adaptador.

## Revisión
Revisar si el timeout supera 2 segundos en más del 5% de solicitudes.
```

## Preguntas y respuestas
### ¿Estoy escribiendo solo el resultado o también el razonamiento detrás de la solución?

No basta escribir “usamos un adaptador”. Debes registrar que el proveedor externo puede fallar, que pedidos no debe conocer su protocolo y que se descartó la llamada directa. Así, el nuevo desarrollador entiende el porqué y no elimina la capa pensando que es innecesaria.

### ¿Qué decisiones clave podrían perderse si se cambia de equipo?

Se pueden perder el timeout elegido, el motivo de los reintentos, qué error se muestra al operador y por qué la estimación de ruta no bloquea todo el pedido. El ADR conserva esas decisiones y asigna un responsable para revisarlas.

### ¿Estoy documentando solo la solución final o también el porqué?

Debes documentar ambos. La solución final es “usar IRouteEstimator”; el porqué es que una dependencia externa no debe controlar la creación de pedidos. Sin el porqué, nadie sabrá cuándo mantener, cambiar o eliminar la decisión.

## Actividad: documenta una decisión real

1. Elige una decisión de la plataforma: rutas, inventario, notificaciones o pagos.
2. Describe el contexto y el problema en máximo cinco líneas.
3. Escribe dos alternativas posibles.
4. Elige una y declara al menos un costo que aceptas.
5. Define una condición medible para revisar la decisión.
6. Crea un ADR en `docs/adr/ADR-00X.md`.
7. Pide a otra persona que lea el ADR y responda: “¿entiendo el porqué, la alternativa descartada y cuándo revisar la decisión?”. Si no puede responder, mejora el documento.

## Cómo comprobar que lo resolviste
Tu actividad está bien resuelta cuando un compañero que no participó en la decisión puede explicar: qué problema existía, qué alternativa se descartó, qué costo se aceptó y qué evento obligaría a revisar el ADR.

## Cierre
Documentar no significa escribir más; significa dejar menos espacio para que el equipo adivine. En el siguiente video vas a usar esta claridad para conectar responsabilidad técnica, escalabilidad, seguridad y ética.
"""


def dotnet_concepts(include_http=False):
    http_concepts = ""
    if include_http:
        http_concepts = """
### `[FromServices]`: no construyas dependencias dentro del controlador
`[FromServices] CreateOrderUseCase useCase` le pide a ASP.NET Core que entregue una instancia ya configurada del caso de uso. Esto es inyección de dependencias: el controlador no hace `new CreateOrderUseCase(...)`, porque no debería decidir qué repositorio, cliente HTTP o configuración usa la aplicación. Esas decisiones se registran al iniciar el programa, normalmente en `Program.cs`.

```csharp
builder.Services.AddScoped<CreateOrderUseCase>();
builder.Services.AddScoped<IRouteEstimator, MapsRouteEstimator>();
```

`AddScoped` significa que la instancia se comparte durante una solicitud HTTP y se descarta al terminar. El primer registro permite resolver el caso de uso; el segundo indica qué implementación concreta se entrega cuando el caso de uso pide `IRouteEstimator`.
"""


def dotnet_observability_concepts():
    return """## 🧩 Cómo leer el código de observabilidad en .NET

`logger` representa `ILogger<T>`, la abstracción de logging de .NET. La clase no decide si el registro termina en consola, Application Insights, OpenTelemetry o un archivo; esa configuración ocurre al iniciar la aplicación. Esto mantiene el código de negocio independiente del destino del log.

`LogInformation` registra un evento normal. Si hay una falla de Ruteo usaríamos `LogWarning` o `LogError` y pasaríamos la excepción para conservar el detalle técnico sin mostrarlo al cliente.

Los textos `{OrderId}`, `{Status}` y `{TraceId}` no son interpolación de cadenas. Son propiedades estructuradas: el sistema guarda cada valor con nombre. Por eso soporte puede buscar todos los registros de un pedido o construir una métrica por estado sin analizar texto libre.

`Activity.Current?.TraceId` obtiene el identificador de trazabilidad de la solicitud actual. El operador `?.` significa “si `Activity.Current` existe, toma su `TraceId`; si no existe, devuelve `null` sin lanzar una excepción”. Ese identificador conecta API, Inventario y Ruteo en una misma investigación.

Nunca coloques correo, dirección, token, contraseña o cuerpo HTTP completo dentro de las propiedades del log. Una traza debe explicar el comportamiento del sistema, no copiar datos privados del cliente.
"""
    return f"""## 🧩 Cómo leer este código C# y .NET

### `public`, `private` y modificadores de acceso
`public` significa que otro código puede usar ese tipo o miembro. Usamos `public interface IRouteEstimator` porque el caso de uso necesita conocer el contrato. `private` significa que solo la misma clase puede acceder al miembro. Por eso los campos como `_routes` son privados: nadie desde fuera debe reemplazarlos sin pasar por el constructor.

La idea no es ocultar por ocultar. Es proteger decisiones. Un controlador puede llamar al caso de uso; no debe cambiar directamente la conexión a base de datos ni el proveedor de rutas.

### `sealed`: esta clase no está diseñada para herencia
`sealed class CreateOrderUseCase` significa que ninguna otra clase puede heredar de `CreateOrderUseCase`. Lo usamos cuando una clase representa una pieza concreta de la aplicación y no queremos que alguien altere su comportamiento mediante herencia. En este curso preferimos extender el comportamiento con interfaces y composición, no con cadenas de clases hijas difíciles de seguir.

`sealed` no hace que la clase sea inmutable ni más segura por sí sola. Solo expresa una intención: esta implementación es final; si necesitas variar el comportamiento, crea otra implementación del contrato correspondiente.

### `record`: datos que viajan entre límites
Un `record` representa principalmente datos. `CreateOrderRequest`, `RouteRequest` y `RouteEstimate` son buenos candidatos porque describen información que cruza un límite: HTTP hacia aplicación, Pedidos hacia Ruteo, o una respuesta desde una dependencia. C# les da igualdad por valor: dos solicitudes con los mismos valores se consideran iguales.

### Interfaces: el contrato antes que la tecnología
`IRouteEstimator` define qué necesita el caso de uso: estimar una ruta. No dice si se usa Google Maps, otro proveedor, una fórmula local o una implementación falsa para pruebas. Esa separación permite cambiar infraestructura sin cambiar la regla de negocio.

### `private readonly`: dependencia estable después de construir la clase
`private readonly IRouteEstimator _routes;` declara un campo privado que solo puede asignarse en el constructor. `private` evita acceso externo; `readonly` evita que la clase cambie de proveedor a mitad de su vida. El constructor deja visibles las dependencias reales de la clase.
{http_concepts}
"""


def video_four_material(source_items, source_links, navigation):
    return f"""# Video 04: Responsabilidad, escalabilidad, seguridad y ética

## 📚 Lecturas de referencia: responsabilidad y seguridad
{source_links}

## 🔗 Continúa el recorrido
{navigation}

## 🎯 La decisión de esta clase
En esta clase vas a tomar una decisión incómoda: cómo usar datos de ubicación para mejorar una entrega sin convertir al repartidor ni al cliente en una fuente de vigilancia permanente. La arquitectura no se evalúa solo por velocidad; también se evalúa por las personas que quedan expuestas cuando el sistema toma una decisión.

## Las ideas que unimos
La primera fuente recuerda que el software puede afectar confianza, seguridad y bienestar. La segunda agrega que escalar no basta: un sistema que responde rápido pero expone datos, excluye usuarios o toma decisiones injustas sigue siendo una mala solución.

Juntas nos obligan a diseñar con cuatro preguntas: ¿qué valor entregamos?, ¿a quién protegemos?, ¿qué datos son necesarios?, ¿qué costo aceptamos para mantener el sistema confiable cuando crezca?

## Escena: la reasignación urgente
Es viernes a las 7:00 p. m. y una tormenta bloquea varias vías. La plataforma necesita reasignar 400 entregas. El área de operaciones pide ubicación GPS en tiempo real de todos los repartidores, historial completo de trayectos y acceso a esos datos para cualquier supervisor. El objetivo es reducir retrasos, pero la propuesta expone más información de la necesaria y puede afectar la seguridad personal de los repartidores.

Aquí aparecen dos actores centrales:

- **El cliente** necesita saber si su pedido llegará y recibir una explicación confiable si cambia la promesa.
- **El repartidor** necesita una ruta y una asignación justa, sin que su ubicación histórica se convierta en información disponible para personas que no la necesitan.

La regla que vamos a proteger es esta: **la plataforma solo puede usar y conservar la ubicación necesaria para coordinar una entrega activa, con acceso limitado y trazable**.

## Dos opciones reales
### Opción A: recopilar y compartir toda la ubicación disponible
Operaciones obtiene más datos de inmediato y puede reaccionar rápido. El costo oculto es alto: exceso de datos personales, mayor superficie de ataque, posibilidad de uso indebido y dificultad para explicar quién consultó la ubicación. Esta opción optimiza la urgencia, pero no protege al repartidor.

### Opción B: ubicación mínima, temporal y con acceso por rol
El sistema guarda la ubicación solo durante una entrega activa, redondea la precisión cuando no es necesaria, elimina o anonimiza el historial según la política definida y registra cada consulta. Operaciones conserva la información que necesita para reasignar; soporte puede auditar accesos; el repartidor no queda expuesto innecesariamente.

Para este caso elijo la opción B. Aceptamos más trabajo: control de roles, expiración de datos, auditoría y pruebas de autorización. Lo aceptamos porque el sistema no puede sacrificar privacidad y seguridad para ganar algunos segundos de coordinación.

## Cómo se diseña la solución
1. El módulo de asignación solicita la ubicación actual solo de repartidores candidatos a una entrega activa.
2. Un servicio de privacidad verifica que quien consulta tenga el rol correcto y una razón operacional válida.
3. La API devuelve la precisión mínima necesaria para decidir, no el historial completo.
4. Cada consulta genera una auditoría: quién consultó, para qué pedido, a qué hora y con qué resultado.
5. Un proceso de retención elimina la ubicación detallada cuando termina la ventana operativa acordada.
6. El cliente recibe una actualización de entrega sin conocer datos personales del repartidor.

## 💬 Preguntas que debemos resolver sobre datos y confianza
### ¿Qué impacto tiene el software que estoy diseñando?

El impacto es directo: una decisión sobre GPS puede mejorar la puntualidad del cliente, pero también puede poner en riesgo la privacidad y seguridad del repartidor. Por eso la arquitectura debe limitar datos, roles y tiempo de retención. La evidencia será una auditoría que muestre que ningún usuario sin autorización consultó ubicaciones.

### ¿Estoy asumiendo una responsabilidad real con las personas que usan el sistema?

Sí, cuando el diseño reconoce que el repartidor no es solo una coordenada en un mapa. La responsabilidad se traduce en reglas: propósito definido, acceso mínimo, consentimiento cuando corresponda y capacidad de revisar quién vio los datos. El costo es implementar controles; el beneficio es proteger confianza y reducir abuso.

### ¿Mi sistema considera seguridad y ética desde el inicio?

Lo hace si la seguridad aparece antes de desplegar: roles, cifrado, retención, auditoría y pruebas de acceso denegado son parte del diseño. No sirve agregar una política de privacidad después de almacenar todo el historial de rutas.

### ¿Qué pasa si el volumen se multiplica durante una emergencia?

No habilitamos acceso ilimitado a los datos. Escalamos el cálculo de candidatos, usamos colas para las reasignaciones y mantenemos el mismo control de autorización. El sistema debe crecer sin degradar las protecciones que justifican la confianza de quienes lo usan.

## Actividad: diseño responsable de reasignación

1. Dibuja el flujo de reasignación de una entrega retrasada.
2. Marca qué dato personal entra, quién lo usa y cuánto tiempo se conserva.
3. Escribe dos reglas de acceso y una regla de retención.
4. Compara la opción de datos completos con la de datos mínimos.
5. Elige una alternativa y redacta un ADR con el riesgo aceptado.
6. Define dos pruebas: una de acceso permitido para operaciones y otra de acceso denegado para un usuario sin rol.
7. Añade una métrica: porcentaje de consultas de ubicación auditadas y porcentaje de datos eliminados al finalizar la retención.

## Cómo comprobar que la actividad está resuelta
Tu propuesta está completa si puedes demostrar tres cosas: el cliente recibe una actualización útil, el operador puede reasignar una entrega y un usuario no autorizado no puede consultar ni reconstruir el historial de ubicación del repartidor.

## ✅ Cierre: velocidad sin daño innecesario
La escalabilidad tiene valor cuando mantiene el servicio bajo presión. La seguridad tiene valor cuando protege a las personas. La ética tiene valor cuando impide que una solución rápida normalice un daño innecesario. En el siguiente video vamos a bajar de estas decisiones al código: principios de diseño, acoplamiento y cohesión.
"""


def video_five_material(source_items, source_links, navigation):
    return f"""# Video 05: Principios de diseño, acoplamiento y cohesión

## 📚 Lecturas de referencia: diseño y calidad estructural
{source_links}

## 🔗 Del caso de privacidad al código
{navigation}

## 🎯 El objetivo del refactor
En esta clase vamos a dejar de hablar de “código limpio” como una frase bonita. Vas a ver una clase que intenta hacer demasiado, identificarás por qué es frágil y la convertirás en componentes que cambian por razones distintas. El objetivo no es tener más archivos: es lograr que una regla de rutas no obligue a modificar pagos, notificaciones y acceso a datos al mismo tiempo.

## El problema: una clase que conoce todo
En la plataforma logística, alguien creó `OrderService`. Con el tiempo le agregaron validación de pedidos, cálculo de rutas, descuento de inventario, guardado en base de datos y envío de correos. La clase funciona hoy, pero cada cambio se vuelve riesgoso: una modificación en la ruta puede romper una notificación; una falla de correo puede impedir que se guarde el pedido.

Esto es baja cohesión: una clase contiene responsabilidades que no pertenecen juntas. También es alto acoplamiento: la lógica de negocio conoce detalles de mapas, base de datos y correo. Las fuentes nos dan dos criterios para corregirlo: separar responsabilidades y reducir dependencias innecesarias.

## Antes del refactor
```csharp
public class OrderService
{{
    public void Create(string customerEmail, decimal total, string address)
    {{
        if (total <= 0) throw new ArgumentException("Total inválido");

        var route = new MapsClient().Calculate(address);
        new SqlOrderRepository().Save(customerEmail, total, route.Distance);
        new EmailSender().Send(customerEmail, "Pedido creado");
    }}
}}
```

Te pregunto: ¿cuántas razones tiene esta clase para cambiar? Si cambia la regla de total, el proveedor de mapas, la base de datos o el correo, debemos modificarla. Ese es el síntoma; no necesitamos medirlo con una fórmula para reconocer el peligro.

## Dos formas de resolverlo
### Opción A: mantener `OrderService` y agregar más condiciones
Es la solución rápida. Podemos agregar `if`, `try/catch` y más métodos privados. El costo es que la clase seguirá teniendo muchas responsabilidades y cada prueba necesitará infraestructura real o mocks complejos.

### Opción B: separar el caso de uso de sus dependencias
El caso de uso conserva la regla de crear un pedido. Un puerto calcula rutas, otro guarda pedidos y otro notifica. Cada componente tiene una razón clara para cambiar.

```csharp
public interface IRouteEstimator
{{
    Task<RouteEstimate> EstimateAsync(string address);
}}

public interface IOrderRepository
{{
    Task SaveAsync(Order order);
}}

public interface IOrderNotifier
{{
    Task NotifyCreatedAsync(Order order);
}}

public sealed class CreateOrderUseCase
{{
    private readonly IRouteEstimator _routes;
    private readonly IOrderRepository _orders;
    private readonly IOrderNotifier _notifier;

    public CreateOrderUseCase(
        IRouteEstimator routes,
        IOrderRepository orders,
        IOrderNotifier notifier)
    {{
        _routes = routes;
        _orders = orders;
        _notifier = notifier;
    }}

    public async Task ExecuteAsync(string email, decimal total, string address)
    {{
        var order = Order.Create(email, total);
        order.AssignRoute(await _routes.EstimateAsync(address));
        await _orders.SaveAsync(order);
        await _notifier.NotifyCreatedAsync(order);
    }}
}}
```

## Qué mejoró y qué costo aceptamos
- **Cohesión:** `CreateOrderUseCase` solo coordina la creación del pedido.
- **Acoplamiento:** los detalles de mapas, SQL y correo quedan detrás de interfaces.
- **Pruebas:** podemos probar la regla del pedido con adaptadores falsos.
- **Costo:** hay más contratos y debemos mantener la composición de dependencias.

Elijo la opción B porque el flujo de pedidos cambiará por varias razones durante el proyecto. No separo para impresionar con patrones; separo porque los cambios ya tienen causas distintas.

## 💬 Respuestas sobre cohesión y dependencias
### ¿Qué parte de mi sistema tiene responsabilidades mezcladas?

`OrderService` mezcla una regla de negocio, una consulta a mapas, persistencia y notificación. La corrección es mover cada detalle a un puerto y dejar en el caso de uso solo la coordinación del flujo. Lo verifico cambiando el proveedor de mapas: si `CreateOrderUseCase` no cambia, reduje el acoplamiento.

### ¿Qué principio arquitectónico me está faltando aplicar?

Falta separación de responsabilidades e inversión de dependencias. El caso de uso debe depender de `IRouteEstimator`, no de `MapsClient`; así la regla de crear pedido no queda atada a un proveedor concreto.

### ¿Qué tan acoplado está mi sistema?

Está demasiado acoplado si una prueba de creación de pedido necesita una base de datos, una API de mapas y un servidor de correo. Después del refactor, una prueba puede usar implementaciones falsas y concentrarse en la regla: un pedido con total positivo se guarda y se notifica.

### ¿Qué módulos tienen demasiadas responsabilidades mezcladas?

Busca módulos que mezclen dominio, infraestructura y presentación. En este caso, `OrderService` era el problema. También revisaría controladores que validan reglas de negocio o repositorios que calculan rutas; ambos indican que la cohesión se está perdiendo.

## Actividad: refactor guiado

1. Crea una versión inicial de `OrderService` con al menos tres responsabilidades mezcladas.
2. Marca con colores o comentarios qué parte es dominio, infraestructura y notificación.
3. Extrae tres interfaces: `IRouteEstimator`, `IOrderRepository` e `IOrderNotifier`.
4. Crea `CreateOrderUseCase` y mueve allí solo la coordinación.
5. Escribe una prueba que use implementaciones falsas y compruebe que un pedido válido se guarda.
6. Cambia la implementación del estimador de rutas sin modificar el caso de uso.
7. Documenta en un ADR por qué aceptaste el costo de las interfaces.

## Cómo comprobar que terminaste
El refactor está bien si puedes responder sí a estas preguntas: ¿puedo cambiar el proveedor de mapas sin cambiar el caso de uso?, ¿puedo probar la creación de pedido sin abrir una base de datos?, ¿cada clase tiene una razón principal para cambiar? Si alguna respuesta es no, todavía hay acoplamiento que revisar.

## ✅ Cierre: cada cambio debe tener su lugar
La cohesión no significa que todas las clases sean pequeñas. Significa que cada una tiene un propósito claro. El bajo acoplamiento no significa que los módulos no se hablen; significa que se relacionan mediante contratos que permiten cambiar sin romper todo. En el siguiente video llevaremos esta separación a un nivel mayor: dominios y límites de contexto.
"""


def video_six_material(source_items, source_links, navigation):
    return f"""# Video 06: Dominios y límites de contexto

## 📚 Lecturas de referencia: dominio y evolución
{source_links}

## 🔗 Del refactor a los límites del negocio
{navigation}

## 🎯 La pregunta de esta clase
Después de separar una clase demasiado grande, aparece una pregunta más profunda: ¿cómo sabemos dónde termina una responsabilidad de negocio y dónde comienza otra? Hoy no vamos a dividir por carpetas ni por tecnologías. Vamos a separar el lenguaje y las reglas de la plataforma logística.

## Escena: la palabra “disponible” significa cosas distintas
El equipo recibe una solicitud: “muestren si un pedido está disponible para entrega”. Parece una frase sencilla, pero cuatro personas la entienden de manera diferente:

- Para **Inventario**, disponible significa que existe stock reservable en una bodega.
- Para **Ruteo**, disponible significa que existe capacidad y una ruta viable.
- Para **Entregas**, disponible significa que un repartidor puede recibir una asignación.
- Para **Pedidos**, disponible significa que el cliente puede confirmar la compra.

Si guardamos esos cuatro significados en una sola propiedad llamada `IsAvailable`, vamos a crear reglas contradictorias. El cliente podría confirmar un pedido porque hay stock, aunque no exista ruta ni capacidad de entrega. Ese es el problema que resuelve un límite de contexto: una palabra puede existir en varios lugares, pero no significa lo mismo en todos.

## Los cuatro contextos que vamos a separar

| Contexto | Pregunta que responde | Regla que protege | Responsable |
|---|---|---|---|
| Pedidos | ¿El cliente puede confirmar la compra? | Un pedido confirmado tiene datos de cliente y artículos válidos. | Equipo de pedidos |
| Inventario | ¿Hay unidades reservables? | No se reserva más cantidad de la disponible. | Equipo de inventario |
| Ruteo | ¿La dirección tiene una ruta viable? | Una estimación debe indicar origen, destino y vigencia. | Equipo de ruteo |
| Entregas | ¿Quién ejecuta el traslado? | Una entrega activa tiene un solo repartidor asignado. | Operación logística |

Fíjate en que todos participan en la misma experiencia del cliente, pero ninguno debe conocer las reglas internas de los demás. Pedidos no calcula distancias; Inventario no decide qué repartidor acepta una ruta; Entregas no modifica el precio del pedido.

## Dos opciones de diseño
### Opción A: un modelo único para todo
Crear una entidad `Order` con stock, rutas, ubicación del repartidor, precio y estados de entrega. Al principio parece cómodo: todo está disponible en un solo lugar. El costo es que una regla de inventario puede romper entregas y que cualquier equipo necesite entender un modelo que no le pertenece.

### Opción B: contextos separados con contratos explícitos
Cada contexto tiene su modelo y su vocabulario. Cuando Pedidos necesita saber si puede confirmar, consulta un contrato de Inventario y solicita una estimación a Ruteo. Cuando se confirma, Entregas recibe un evento o comando con la información que necesita, no la entidad completa de Pedidos.

Para el MVP elegiría la opción B dentro de un monolito modular. No necesitamos cuatro microservicios todavía; necesitamos cuatro límites claros. Aceptamos mantener contratos internos porque reducen el costo de cambiar cada área después.

## Ejemplo en C#: el mismo concepto no viaja como el mismo objeto
```csharp
public sealed record ReservationRequest(Guid ProductId, int Quantity);
public sealed record RouteRequest(string DeliveryAddress);

public interface IInventoryAvailability
{{
    Task<bool> CanReserveAsync(ReservationRequest request);
}}

public interface IRoutePlanning
{{
    Task<RouteEstimate> EstimateAsync(RouteRequest request);
}}

public sealed class ConfirmOrderUseCase
{{
    private readonly IInventoryAvailability _inventory;
    private readonly IRoutePlanning _routes;

    public ConfirmOrderUseCase(IInventoryAvailability inventory, IRoutePlanning routes)
    {{
        _inventory = inventory;
        _routes = routes;
    }}

    public async Task ConfirmAsync(Order order)
    {{
        var hasStock = await _inventory.CanReserveAsync(
            new ReservationRequest(order.ProductId, order.Quantity));
        var route = await _routes.EstimateAsync(new RouteRequest(order.DeliveryAddress));

        if (!hasStock || !route.IsViable)
            throw new InvalidOperationException("El pedido no puede confirmarse todavía.");

        order.Confirm();
    }}
}}
```

El caso de uso de Pedidos no recibe una entidad `Inventory` ni modifica una entidad `Route`. Solo conoce los contratos que necesita para aplicar su propia regla: confirmar únicamente cuando hay stock y ruta viable.

## Preguntas y respuestas
### ¿Mi sistema mezcla conceptos de diferentes dominios?

Sí, si una misma propiedad intenta decidir stock, capacidad de ruta y disponibilidad del repartidor. La corrección es crear modelos separados y nombrarlos según el contexto. `StockAvailable` pertenece a Inventario; `IsViable` pertenece a Ruteo; `AssignedCourierId` pertenece a Entregas.

### ¿Dónde está el límite claro entre áreas funcionales?

El límite aparece donde cambia la pregunta del negocio y el responsable de la regla. Inventario responde por unidades; Ruteo responde por viabilidad de la ruta; Entregas responde por la asignación; Pedidos responde por la confirmación del cliente. Si una regla cambia sin que el otro equipo deba cambiar su modelo, el límite está funcionando.

### ¿Qué partes son difíciles de cambiar?

Las partes difíciles son las que comparten tablas, entidades o reglas sin contrato. Si un cambio de inventario obliga a modificar la pantalla de entregas, existe acoplamiento entre contextos. Lo comprobaría cambiando la política de reserva y verificando que el módulo de ruteo no se modifica ni vuelve a desplegarse.

## Actividad: dibuja y prueba los límites

1. Dibuja cuatro cajas: Pedidos, Inventario, Ruteo y Entregas.
2. Escribe dentro de cada caja una pregunta de negocio, una regla y un responsable.
3. Marca con flechas los contratos que cruzan los límites; no dibujes acceso directo a tablas ajenas.
4. Elige el flujo “confirmar pedido” y escribe qué datos viajan de un contexto a otro.
5. Crea interfaces C# similares a `IInventoryAvailability` e `IRoutePlanning`.
6. Cambia una regla de Inventario, por ejemplo la cantidad máxima reservable, y demuestra que `ConfirmOrderUseCase` conserva su responsabilidad.
7. Documenta la decisión en un ADR: monolito modular con contextos separados antes de considerar microservicios.

## Cómo comprobar que la actividad está bien resuelta
Pide a un compañero que responda estas tres preguntas mirando tu diagrama y tu código: ¿qué significa “disponible” en cada contexto?, ¿qué regla protege cada módulo?, ¿qué contrato usa Pedidos para confirmar? Si puede responder sin abrir una tabla compartida ni leer una clase gigante, tus límites son claros.

## Cierre
Un límite de contexto no es una pared que impide colaborar. Es una forma de permitir colaboración sin confusión. En el siguiente video compararemos qué ocurre cuando esos módulos permanecen en un monolito y qué cambia cuando intentamos distribuirlos.
"""


def video_seven_material(source_items, source_links, navigation):
    return f"""# Video 07: Monolitos, sistemas distribuidos y microservicios

## 📚 Lecturas de referencia: elegir la estructura correcta
{source_links}

## 🔗 De límites de contexto a decisiones de despliegue
{navigation}

## 🎯 El problema que vamos a decidir
Ya definimos Pedidos, Inventario, Ruteo y Entregas como contextos distintos. Ahora viene una pregunta que muchos equipos contestan demasiado pronto: ¿debemos convertir cada contexto en un microservicio? La respuesta no es automática. Un límite de dominio no obliga a tener un despliegue independiente.

## Escena: la campaña de viernes negro
La plataforma anuncia entregas en menos de dos horas. Durante la campaña, el tráfico de consultas de rutas se multiplica por veinte, pero la creación de pedidos y la reserva de inventario siguen dentro de su volumen normal. El equipo observa que el cálculo de rutas consume CPU y demora las confirmaciones de pedido.

El director de tecnología propone: “separemos todo en microservicios este fin de semana”. El equipo debe frenar y preguntar: ¿qué problema queremos resolver exactamente?, ¿qué módulo necesita escalar?, ¿tenemos monitoreo, despliegue automático y contratos estables para operar servicios separados?

## Opción A: monolito modular bien protegido
Pedidos, Inventario, Ruteo y Entregas siguen desplegándose juntos, pero cada módulo conserva sus contratos internos y dependencias controladas. Para la campaña, se optimiza el cálculo de rutas con caché y una cola de solicitudes. Esta opción mantiene un solo despliegue, una base operativa más simple y menos fallos de red.

**Cuándo es suficiente:** cuando el equipo es pequeño, los módulos cambian juntos, el volumen todavía cabe en una aplicación escalada horizontalmente y no hay evidencia de que otro módulo necesite autonomía real.

## Opción B: extraer Ruteo como servicio independiente
Ruteo se convierte en un servicio porque tiene un perfil de carga distinto, puede escalar por separado y usa un proveedor externo de mapas. Pedidos conserva un contrato `IRouteEstimator`; la comunicación se protege con timeout, reintentos y observabilidad. Esta opción evita que una campaña de rutas degrade la confirmación de pedidos, pero agrega despliegues, fallos de red, monitoreo distribuido y gobierno de contratos.

**Cuándo vale la pena:** cuando la métrica confirma que Ruteo es el cuello de botella, un equipo puede mantenerlo, existe automatización de entrega y la separación reduce un riesgo mayor que el costo operativo que introduce.

## La decisión para este caso
No separaría los cuatro contextos. Extraería solamente Ruteo de forma gradual si se cumplen tres señales durante dos campañas:

1. El percentil 95 de cálculo de rutas supera el objetivo acordado y bloquea la confirmación de pedidos.
2. Ruteo necesita desplegar cambios con una frecuencia distinta a Pedidos e Inventario.
3. El equipo ya puede observar trazas, errores, reintentos y despliegues de un servicio sin depender de intervención manual.

Hasta que esas señales existan, elegiría monolito modular, caché para rutas y una cola de trabajo. Esta no es una decisión conservadora por miedo: es una decisión proporcional al problema actual.

## Un contrato que permite extraer Ruteo después
```csharp
public interface IRouteEstimator
{{
    Task<RouteEstimate> EstimateAsync(RouteRequest request, CancellationToken cancellationToken);
}}

public sealed record RouteRequest(string Origin, string Destination);
public sealed record RouteEstimate(decimal DistanceKm, TimeSpan Eta, bool IsViable);
```

Mientras la interfaz se mantenga estable, hoy puede implementarla un módulo interno y mañana un cliente HTTP hacia un servicio de Ruteo. El caso de uso de Pedidos no necesita saber cuándo ocurre esa extracción.

## Preguntas y respuestas
### ¿Mi sistema necesita más desacople o más simplicidad?

Hoy necesita simplicidad con límites claros. Pedidos e Inventario cambian juntos y no presentan saturación; separarlos agregaría llamadas remotas y coordinación sin resolver un cuello de botella. Ruteo, en cambio, es candidato a aislamiento porque su carga y dependencia externa son distintas.

### ¿Estoy adoptando microservicios por moda o por necesidad real?

Es necesidad real solo cuando puedes señalar una métrica, un equipo responsable y un ciclo de despliegue que mejoran con la separación. Decir “Netflix usa microservicios” no responde a la campaña de nuestra plataforma ni cubre el costo de operar fallos distribuidos.

### ¿La separación refleja el dominio del negocio?

Sí, si Ruteo conserva su lenguaje, reglas y responsabilidad: estimar viabilidad, distancia y tiempo. No sería una buena separación crear un servicio “utilidades” o dividir por tablas de base de datos; eso transfiere el acoplamiento de código a la red.

### ¿Qué costo operativo aceptamos al extraer Ruteo?

Aceptamos monitorear latencia entre servicios, versionar contratos, tratar timeouts, reintentos y fallos parciales. Lo aceptamos solo si la degradación actual de pedidos durante la campaña cuesta más que operar esas capacidades.

## Actividad: decide si extraerías Ruteo

1. Dibuja el monolito modular actual con Pedidos, Inventario, Ruteo y Entregas.
2. Registra tres métricas hipotéticas de campaña: solicitudes por minuto, percentil 95 de Ruteo y errores de confirmación de pedido.
3. Define un objetivo: por ejemplo, confirmar el 95% de pedidos en menos de dos segundos.
4. Explica qué dato demostraría que Ruteo debe escalar de forma independiente.
5. Diseña el contrato `IRouteEstimator` y define timeout, reintento y respuesta cuando Ruteo no esté disponible.
6. Escribe un ADR: mantener monolito modular ahora o extraer Ruteo; incluye la condición de revisión.
7. Presenta el costo operativo de ambas opciones: despliegue, observabilidad, incidentes y coordinación de equipos.

## Cómo comprobar que la actividad está resuelta
Tu decisión es defendible si otra persona puede identificar el cuello de botella, leer la métrica que justifica la separación, entender el contrato y saber qué ocurrirá cuando Ruteo falle. Si la única razón para separar es “queremos microservicios”, la actividad aún no está resuelta.

## Cierre
Los microservicios no son el siguiente nivel natural de un monolito. Son una herramienta costosa para problemas concretos de autonomía, escala y organización. En el siguiente video trabajaremos contratos e infraestructura para que, cuando una separación sea necesaria, no rompa a quienes dependen del sistema.
"""


def video_eight_material(source_items, source_links, navigation):
    return f"""# Video 08: APIs, contratos e infraestructura

## 📚 Lecturas de referencia: contratos y despliegue
{source_links}

## 🔗 De microservicios a una integración segura
{navigation}

## 🎯 La decisión de esta clase
Hoy vamos a construir el borde de la plataforma: el punto donde una aplicación externa o una interfaz web solicita crear un pedido. La pregunta no es solamente “¿qué endpoint hacemos?”. La pregunta es qué contrato prometemos, cómo evitamos romper a quienes lo consumen y dónde dejamos los detalles de infraestructura.

## Escena: una aplicación móvil ya usa tu API
El equipo móvil consume `POST /api/orders`. La próxima semana, negocio pide agregar un campo de ventana de entrega. Alguien propone cambiar `address` por un objeto complejo y renombrar `total` por `amount`. La aplicación móvil publicada no se actualizará de inmediato. Si rompemos el contrato, el cliente no podrá crear pedidos aunque el servidor funcione.

El actor principal es **la aplicación móvil del cliente**. Necesita enviar una solicitud estable y recibir un error comprensible. La regla que protegemos es: **un cambio compatible agrega información opcional; un cambio incompatible se publica como una versión nueva del contrato**.

## Contrato de entrada
```csharp
public sealed record CreateOrderRequest(
    string CustomerEmail,
    string DeliveryAddress,
    decimal Total,
    string? DeliveryWindow);

public sealed record CreateOrderResponse(
    Guid OrderId,
    string Status,
    DateTimeOffset CreatedAt);
```

`DeliveryWindow` es opcional. Una aplicación antigua puede no enviarlo y el servidor puede aplicar una regla por defecto. Si necesitáramos cambiar el significado de `Total`, no modificaríamos silenciosamente el contrato: publicaríamos `/api/v2/orders` y mantendríamos la versión anterior durante una ventana acordada.

## El controlador no contiene la regla de negocio
```csharp
[ApiController]
[Route("api/orders")]
public sealed class OrdersController : ControllerBase
{{
    [HttpPost]
    public async Task<ActionResult<CreateOrderResponse>> Create(
        CreateOrderRequest request,
        [FromServices] CreateOrderUseCase useCase,
        CancellationToken cancellationToken)
    {{
        var result = await useCase.ExecuteAsync(request, cancellationToken);
        return Created($"/api/orders/{{result.OrderId}}", result);
    }}
}}
```

El controlador recibe HTTP y devuelve HTTP. La validación de formato puede estar aquí; la regla “un pedido se confirma solo si hay inventario y ruta viable” vive en el caso de uso y el dominio. Así podemos cambiar ASP.NET, la aplicación móvil o un proveedor externo sin mover la regla principal.

{dotnet_concepts(include_http=True)}

## Infraestructura reproducible
Para que el contrato funcione fuera de tu computador, necesitas un entorno repetible. Define variables para conexión, proveedor de rutas, timeout y ambiente. El despliegue debe ejecutar pruebas, crear la configuración y publicar la misma versión que fue validada. No dependas de cambios manuales que nadie pueda reconstruir.

## Dos alternativas
### Opción A: controlador conectado directamente a SQL y al proveedor de mapas
Se construye rápido, pero el endpoint conoce contraseñas, queries, URL de mapas y lógica de negocio. Probarlo exige infraestructura real y cualquier cambio externo obliga a modificar la API.

### Opción B: contrato estable, caso de uso y adaptadores
El controlador llama a `CreateOrderUseCase`; el caso de uso depende de puertos para persistencia y rutas; infraestructura implementa esos puertos. Cuesta crear contratos y configuración, pero cada borde tiene una responsabilidad clara.

Elijo B. El contrato debe sobrevivir a cambios de interfaz y los detalles de infraestructura deben poder reemplazarse sin tocar la creación de pedidos.

## Preguntas y respuestas
### ¿Qué pasa si una aplicación usa una versión anterior?

La versión anterior debe continuar aceptando su formato durante el periodo anunciado. Agregar `DeliveryWindow` como opcional no rompe al cliente; cambiar el significado de un campo sí requiere versión nueva. Lo verifico con pruebas de contrato que ejecuten la misma solicitud de una aplicación antigua y una nueva.

### ¿Mis interfaces están documentadas?

Están documentadas si alguien puede saber qué campos son obligatorios, qué errores recibe, qué significa cada estado y cómo evoluciona la versión. Publicaría OpenAPI, ejemplos de solicitudes y respuestas, y códigos de error como `inventory_unavailable` o `route_not_viable`.

### ¿El entorno es reproducible?

Lo es si otro integrante puede levantar la API con las mismas variables, ejecutar pruebas y obtener el mismo comportamiento sin configurar valores manualmente. La evidencia será un archivo de configuración por ambiente y una ejecución de despliegue automatizada.

## Actividad: crea el borde del pedido

1. Define `CreateOrderRequest` y `CreateOrderResponse`.
2. Escribe tres reglas del contrato: campos obligatorios, error de inventario y compatibilidad de versiones.
3. Implementa un controlador que solo traduzca HTTP a la llamada del caso de uso.
4. Declara los puertos `IOrderRepository` e `IRouteEstimator`.
5. Agrega una prueba de contrato para una solicitud sin `DeliveryWindow`.
6. Documenta en un ADR por qué eliges agregar un campo opcional en lugar de cambiar el formato existente.
7. Escribe las variables de entorno que el adaptador de rutas necesita para ejecutarse.

## Cómo comprobar que terminaste
La actividad está bien resuelta si puedes cambiar el proveedor de rutas sin cambiar el controlador, ejecutar una solicitud de una versión anterior sin error y levantar el proyecto en otro equipo sin pasos secretos.

## Cierre
Una API es una promesa. La infraestructura es el lugar donde esa promesa se ejecuta. En el siguiente video veremos cómo saber qué ocurrió cuando esa promesa falla, sin convertir los logs en una fuga de datos.
"""


def video_nine_material(source_items, source_links, navigation):
    return f"""# Video 09: Observabilidad, seguridad y privacidad

## 📚 Lecturas de referencia: detectar sin exponer
{source_links}

## 🔗 Del contrato de API a la operación responsable
{navigation}

## 🎯 El incidente que vamos a investigar
Un cliente informa que su pedido aparece como “en preparación” desde hace cuarenta minutos. Operaciones no sabe si falló inventario, ruteo, notificación o la API. Un desarrollador propone registrar el correo, la dirección completa y el token de acceso en cada log “para investigar más rápido”. Esa solución puede resolver un incidente y crear otro: exponer datos sensibles.

Hoy diseñaremos una observabilidad útil: suficiente para reconstruir el flujo, limitada para no revelar información que soporte no necesita ver.

## El flujo y sus señales
Cuando llega `POST /api/orders`, el sistema crea un `traceId`. Ese identificador acompaña la reserva de inventario, la estimación de ruta y la notificación. Soporte puede buscar el `traceId` y entender dónde se detuvo el pedido sin ver el correo ni la dirección exacta del cliente.

```csharp
logger.LogInformation(
    "Order {{OrderId}} moved to {{Status}}. Trace {{TraceId}}",
    order.Id,
    order.Status,
    Activity.Current?.TraceId);
```

{dotnet_observability_concepts()}

El actor principal es **el equipo de soporte**. Necesita responder al cliente con información confiable. La regla es: **los registros deben permitir reconstruir el flujo sin almacenar secretos, tokens, direcciones completas ni datos personales innecesarios**.

## Qué observamos

| Señal | Pregunta que responde | Ejemplo |
|---|---|---|
| Log estructurado | ¿Qué transición ocurrió? | pedido confirmado, reserva rechazada |
| Métrica | ¿Con qué frecuencia ocurre? | porcentaje de rutas fallidas |
| Traza | ¿Dónde se demoró el flujo? | API -> Inventario -> Ruteo |
| Alerta | ¿Cuándo debemos intervenir? | p95 de ruteo supera 2 segundos |
| Auditoría | ¿Quién consultó datos sensibles? | operador consultó detalle de entrega |

## Dos opciones
### Opción A: registrar todo para depurar
Incluye cuerpos HTTP, correos, direcciones, tokens y respuestas externas. La investigación parece rápida, pero aumenta riesgo de fuga, incumplimiento y acceso innecesario.

### Opción B: observabilidad estructurada y minimizada
Usa `orderId`, `traceId`, tipo de error, duración, estado y dependencia afectada. Protege atributos sensibles con enmascaramiento y limita la auditoría a roles autorizados. Es más trabajo inicial, pero soporte obtiene señales útiles sin usar datos personales como herramienta de depuración.

Elijo B. Una traza útil no necesita conocer la vida privada del cliente.

## Preguntas y respuestas
### ¿Qué tan claro es el estado del sistema en producción?

Es claro si soporte puede seguir un pedido por `traceId` y ver en qué paso se detuvo. Si solo existen mensajes libres como “error inesperado”, el sistema no es observable. Lo comprobaría simulando una caída del proveedor de rutas y verificando que la traza muestra el error, la duración y el estado final.

### ¿Estoy monitoreando lo que importa?

Para este flujo, mediría confirmaciones exitosas, latencia p95 de Inventario y Ruteo, número de reintentos y pedidos estancados por más de diez minutos. No mediría solamente uso de CPU; esa métrica no le dice a operaciones si el cliente está esperando una entrega sin respuesta.

### ¿Qué datos sensibles maneja el sistema?

Correo, dirección, teléfono, ubicación y tokens de sesión. Cada uno necesita un propósito, un rol de acceso y una política de retención. En los logs usaría `orderId` y `traceId`; la consulta del detalle personal ocurre solo en el sistema autorizado y queda auditada.

### ¿Cómo reduzco exposición innecesaria?

No escribas cuerpos completos de solicitud en logs. Enmascara campos, elimina tokens, cifra datos en tránsito y restringe paneles de observabilidad por rol. Lo verifico con una prueba que revise los logs de un pedido y confirme que no contienen correo, dirección ni token.

## Actividad: investiga un pedido sin mirar datos privados

1. Define una secuencia de estados: `Created`, `InventoryReserved`, `RouteEstimated`, `Assigned`, `Failed`.
2. Agrega `traceId`, `orderId`, estado, duración y tipo de error a cada log.
3. Define tres métricas: porcentaje de pedidos confirmados, p95 de ruteo y pedidos estancados.
4. Crea una alerta cuando un pedido lleve más de diez minutos sin transición.
5. Escribe una lista de datos que no deben aparecer en logs: correo, dirección, teléfono, token y ubicación precisa.
6. Simula que Ruteo responde con timeout y documenta qué verá soporte.
7. Agrega una prueba automatizada que falle si un correo o token aparece en el registro.
8. Agrega una prueba de acceso denegado para comprobar que un usuario sin rol de soporte no puede abrir la traza detallada.

## Cómo comprobar que terminaste
Entrega una traza de ejemplo donde soporte identifica un timeout de Ruteo usando `traceId`. Entrega también el log enmascarado y la prueba que demuestra que los datos privados no están allí. Si puedes diagnosticar el incidente sin abrir información personal, la solución es correcta.

## Cierre
Observar no significa guardar todo. Significa tener las señales necesarias para actuar con rapidez y proteger a las personas mientras lo hacemos. En el siguiente video llevaremos esta disciplina a pruebas automatizadas, despliegue y entrega continua.
"""


def video_ten_material(source_items, source_links, navigation):
        return f"""# Video 10: Testing, DevOps y entrega continua

## 📚 Lecturas de referencia: comprobar y entregar con confianza
{source_links}

## 🔗 De observar incidentes a prevenirlos
{navigation}

## 🎯 El cambio que no debe romper una entrega
El equipo modifica la regla de confirmación: ahora un pedido solo puede confirmarse si tiene inventario reservado y una ruta viable. En el computador de quien programó funciona. Sin embargo, nadie ejecutó pruebas en otro entorno y el viernes el despliegue manual publica una versión que permite confirmar pedidos sin ruta.

El actor más afectado es **el cliente**, porque puede recibir una promesa de entrega que la operación no puede cumplir. El segundo actor es **el equipo de operación**, porque debe corregir pedidos ya confirmados. La regla que protegemos es: **un pedido no puede pasar a Confirmed si Inventario o Ruteo informan que el flujo no es viable**.

## La prueba que protege la regla
```csharp
public sealed class ConfirmOrderUseCaseTests
{{
        [Fact]
        public async Task Does_not_confirm_when_route_is_not_viable()
        {{
                var inventory = new FakeInventoryAvailability(hasStock: true);
                var routes = new FakeRoutePlanning(isViable: false);
                var useCase = new ConfirmOrderUseCase(inventory, routes);
                var order = Order.Create("cliente@correo.com", 150_000m);

                await Assert.ThrowsAsync<InvalidOperationException>(
                        () => useCase.ConfirmAsync(order));

                Assert.Equal(OrderStatus.Pending, order.Status);
        }}
}}
```

Esta prueba no comprueba que un método privado fue llamado ni que un mock recibió una llamada exacta. Comprueba comportamiento: cuando Ruteo no ofrece una ruta viable, el pedido sigue pendiente. Ese es el tipo de prueba que protege una decisión arquitectónica.

## 🧩 Cómo leer esta prueba en .NET
`public sealed class ConfirmOrderUseCaseTests` es una clase de pruebas. `sealed` indica que no se diseñó para herencia; cada prueba debe ser simple e independiente. `[Fact]` es un atributo de xUnit que marca un método como caso de prueba sin parámetros.

`async Task` permite esperar operaciones asíncronas. `await Assert.ThrowsAsync<InvalidOperationException>(...)` verifica que el caso de uso rechaza el pedido. `Assert.Equal` compara el estado final. Los nombres `FakeInventoryAvailability` y `FakeRoutePlanning` indican implementaciones controladas para pruebas: no abren una base de datos ni llaman una API real.

El modificador `public` permite que xUnit descubra la prueba. Las variables `var inventory` y `var routes` son locales al método: viven solo durante esa prueba. En producción, las mismas interfaces reciben adaptadores reales mediante inyección de dependencias; en la prueba reciben falsos controlados.

## Dos estrategias de entrega
### Opción A: probar y desplegar manualmente
Cada desarrollador ejecuta lo que recuerda en su máquina y alguien publica archivos en producción. Es rápida al inicio, pero no garantiza que se ejecuten pruebas, que la configuración sea correcta ni que el artefacto desplegado sea el que se revisó.

### Opción B: pipeline que valida antes de publicar
Cada cambio ejecuta restauración, compilación, pruebas y análisis. Solo si esas etapas pasan se crea un artefacto versionado y se despliega. La entrega tarda unos minutos más, pero elimina pasos manuales y deja evidencia de qué versión superó las pruebas.

Para la plataforma elijo B. No significa que el pipeline reemplace el criterio humano; significa que los controles repetibles no dependen de que alguien los recuerde bajo presión.

## Pipeline mínimo
```yaml
name: verify-order-flow
on: [pull_request]

jobs:
    test:
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v4
            - uses: actions/setup-dotnet@v4
                with:
                    dotnet-version: 8.0.x
            - run: dotnet restore
            - run: dotnet build --configuration Release --no-restore
            - run: dotnet test --configuration Release --no-build
```

Este flujo se ejecuta en cada pull request. `dotnet restore` descarga dependencias; `dotnet build` compila; `dotnet test` ejecuta los casos de prueba. `--no-restore` y `--no-build` evitan repetir trabajo en las últimas etapas porque ya se hicieron antes. Si falla una prueba, el cambio no debería fusionarse hasta entender la causa.

## Preguntas y respuestas
### ¿Qué tan bien validamos la estructura del sistema?

La validamos cuando una prueba comprueba una regla relevante y una revisión confirma que Pedidos depende de contratos, no de infraestructura concreta. En este caso, la prueba demuestra que una ruta inviable no confirma el pedido; una prueba de integración puede demostrar después que el adaptador de rutas traduce correctamente la respuesta externa.

### ¿Qué tan fácil es detectar un problema antes de producción?

Debe detectarse en el pull request. Si el cambio rompe la regla de confirmación, `dotnet test` falla antes de crear un artefacto. Si el pipeline solo se ejecuta después de desplegar, el control llega demasiado tarde.

### ¿Qué tan automatizado está el proceso de entrega?

Está automatizado cuando restaurar, compilar, probar y generar el artefacto ocurren con el mismo pipeline para todos. Una lista de pasos en un documento no es automatización; es una tarea manual que puede olvidarse.

## Actividad: protege un cambio con una prueba y un pipeline

1. Implementa la regla de confirmación en `ConfirmOrderUseCase`.
2. Crea dos falsos: uno con inventario disponible y otro con ruta inviable.
3. Escribe una prueba que confirme que el pedido sigue `Pending` cuando falle Ruteo.
4. Escribe una segunda prueba de caso feliz con inventario y ruta viable.
5. Crea `.github/workflows/verify-order-flow.yml` con `restore`, `build` y `test`.
6. Introduce temporalmente un error en la regla y observa que la prueba falla.
7. Corrige el error, ejecuta el pipeline y guarda el enlace o captura de la ejecución exitosa.

## Cómo comprobar que terminaste
Tu solución está completa si puedes mostrar una prueba que falla cuando la regla se rompe, una prueba que pasa cuando el flujo es válido y una ejecución de GitHub Actions que impide integrar el cambio defectuoso.

## Cierre
Probar no es confirmar que el código compila. Entregar continuamente no es desplegar muchas veces. Ambas prácticas construyen una barrera confiable entre una idea y un cambio que llega a producción. En el siguiente video estudiaremos cómo estimar el costo y el riesgo de evolucionar esa arquitectura.
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
    if number == 3:
        return video_three_material(source_items, source_links, " | ".join(navigation))
    if number == 4:
        return video_four_material(source_items, source_links, " | ".join(navigation))
    if number == 5:
        return video_five_material(source_items, source_links, " | ".join(navigation))
    if number == 6:
        return video_six_material(source_items, source_links, " | ".join(navigation))
    if number == 7:
        return video_seven_material(source_items, source_links, " | ".join(navigation))
    if number == 8:
        return video_eight_material(source_items, source_links, " | ".join(navigation))
    if number == 9:
        return video_nine_material(source_items, source_links, " | ".join(navigation))
    if number == 10:
        return video_ten_material(source_items, source_links, " | ".join(navigation))
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
