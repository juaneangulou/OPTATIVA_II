from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


BASE = Path(r"c:\proj\itm\OPTATIVA_II")
OUT = BASE / "presentacion_temas_transversales_arquitectura_30_slides.pptx"

NAVY = RGBColor(18, 43, 72)
TEAL = RGBColor(20, 126, 126)
GOLD = RGBColor(220, 170, 65)
INK = RGBColor(35, 47, 60)
MUTED = RGBColor(91, 105, 119)
PALE = RGBColor(244, 247, 249)
WHITE = RGBColor(255, 255, 255)
LINE = RGBColor(210, 219, 227)


SLIDES = [
    ("Gobierno tecnico sin burocracia", "Hacer visible quien decide, con que evidencia y cuando revisar", [
        "Definir foros, niveles de decision y responsables por dominio.",
        "Usar ADR, principios y excepciones como memoria operativa.",
        "Medir el valor del gobierno por decisiones mas rapidas y reversibles.",
    ]),
    ("Arquitectura y estrategia de producto", "La estructura tecnica debe proteger una apuesta de negocio concreta", [
        "Traducir objetivos de producto en capacidades y restricciones tecnicas.",
        "Priorizar arquitectura junto al roadmap, no despues de las funcionalidades.",
        "Revisar si cada iniciativa aumenta valor, aprendizaje o capacidad de cambio.",
    ]),
    ("Portafolio y racionalizacion de aplicaciones", "No todo sistema merece crecer, migrarse o mantenerse igual", [
        "Clasificar aplicaciones por valor, riesgo, costo y salud tecnica.",
        "Elegir entre invertir, modernizar, reemplazar, consolidar o retirar.",
        "Evitar duplicar capacidades solo porque cada equipo optimiza localmente.",
    ]),
    ("Arquitectura empresarial ligera", "Conectar capacidades, procesos, datos y tecnologia sin crear mapas inmantenibles", [
        "Usar mapas de capacidades para conversar con negocio.",
        "Relacionar capacidades con aplicaciones, equipos y riesgos.",
        "Mantener el nivel de detalle que habilita decisiones reales.",
    ]),
    ("FinOps y costo como atributo de calidad", "El costo operativo tambien tiene umbrales y escenarios", [
        "Asignar costo por producto, dominio, ambiente o unidad de negocio.",
        "Observar costo por transaccion, usuario, pedido o evento.",
        "Comparar elasticidad, rendimiento y resiliencia contra gasto sostenible.",
    ]),
    ("Sostenibilidad del software", "La arquitectura puede reducir consumo sin sacrificar el servicio", [
        "Medir computo, almacenamiento, transferencia y tiempo de ejecucion.",
        "Preferir componentes eficientes y apagado de recursos no utilizados.",
        "Incluir huella ambiental junto con costo y rendimiento en la decision.",
    ]),
    ("Accesibilidad desde la arquitectura", "La inclusion no debe depender de una correccion al final", [
        "Incluir necesidades de personas con distintas capacidades en requisitos.",
        "Proteger teclado, contraste, semantica, lectura y alternativas de contenido.",
        "Validar accesibilidad con pruebas automatizadas y personas usuarias.",
    ]),
    ("Privacidad por diseno", "Minimizar datos es una decision estructural, no solo legal", [
        "Recolectar solo lo necesario para una finalidad explicita.",
        "Separar identidad, datos operativos y datos de analitica cuando corresponda.",
        "Definir retencion, borrado, acceso y trazabilidad desde el modelo de datos.",
    ]),
    ("Cumplimiento y evidencia auditable", "Una regla que no puede demostrarse depende de la memoria", [
        "Traducir obligaciones regulatorias en controles verificables.",
        "Conservar evidencia de accesos, cambios, aprobaciones y excepciones.",
        "Diseñar auditoria proporcional al riesgo, no registros indiscriminados.",
    ]),
    ("Amenazas de la cadena de suministro", "El sistema tambien depende de paquetes, imagenes y proveedores", [
        "Mantener inventario de componentes y versiones utilizadas.",
        "Verificar origen, integridad, licencias y vulnerabilidades.",
        "Preparar reemplazo o aislamiento para dependencias comprometidas.",
    ]),
    ("Identidad, acceso y confianza", "La frontera real del sistema incluye personas, servicios y dispositivos", [
        "Aplicar minimo privilegio y separar funciones sensibles.",
        "Preferir identidad verificable de servicio a secretos compartidos.",
        "Revisar permisos como parte del ciclo de vida, no solo al alta.",
    ]),
    ("Gobierno de datos", "Los datos necesitan propietarios, definiciones y reglas de calidad", [
        "Asignar ownership y custodios para datos criticos.",
        "Definir significado, linaje, calidad y nivel de sensibilidad.",
        "Resolver conflictos de definicion antes de construir integraciones.",
    ]),
    ("Arquitectura analitica y operacional", "Consultar historicos no debe degradar el camino transaccional", [
        "Separar cargas de lectura intensiva de operaciones criticas.",
        "Elegir frescura, consistencia y latencia segun la decision que se necesita.",
        "Documentar origen y transformaciones para que el indicador sea confiable.",
    ]),
    ("Calidad de decisiones con datos", "Un tablero no corrige una metrica mal definida", [
        "Acordar definiciones, unidad, ventana temporal y poblacion.",
        "Distinguir metrica de vanidad, indicador operativo y resultado de negocio.",
        "Validar que la medicion cambie una decision o comportamiento.",
    ]),
    ("Experiencia de usuario y arquitectura", "La latencia y la incertidumbre se sienten como parte del producto", [
        "Diseñar estados de carga, error, reintento y trabajo offline cuando aplique.",
        "Proteger los caminos criticos que afectan confianza y conversion.",
        "Usar investigacion de usuarios para descubrir costos tecnicos invisibles.",
    ]),
    ("Diseno de servicios internos", "La arquitectura tambien debe cuidar a sus consumidores tecnicos", [
        "Tratar APIs internas, librerias y plataformas como productos.",
        "Publicar contratos, ejemplos, limites, soporte y ciclo de vida.",
        "Medir adopcion, friccion y tiempo de integracion de los equipos.",
    ]),
    ("Plataforma interna y golden paths", "Estandarizar lo repetitivo libera energia para el problema de negocio", [
        "Ofrecer caminos recomendados para desplegar, observar y asegurar servicios.",
        "Permitir excepciones explicitas cuando el contexto las justifique.",
        "Medir si la plataforma reduce carga cognitiva y tiempo de entrega.",
    ]),
    ("Arquitectura y equipos: ley de Conway", "Las comunicaciones de la organizacion aparecen en el sistema", [
        "Alinear limites de equipos con responsabilidades de dominio.",
        "Reducir dependencias entre equipos que deben entregar con frecuencia.",
        "Usar cambios organizacionales y tecnicos de forma coordinada.",
    ]),
    ("Team Topologies aplicado", "La forma de colaborar condiciona el flujo de cambio", [
        "Distinguir equipos stream-aligned, plataforma y habilitadores.",
        "Diseñar interacciones temporales y limites claros de responsabilidad.",
        "Evitar plataformas que se convierten en cuellos de botella centrales.",
    ]),
    ("Conocimiento y bus factor", "Una arquitectura robusta no depende de una sola persona", [
        "Distribuir conocimiento mediante revisiones, pairing y documentacion breve.",
        "Identificar componentes cuyo mantenimiento depende de un unico experto.",
        "Practicar rotacion y simulaciones de ausencia en areas criticas.",
    ]),
    ("Arquitectura para adquisiciones y licitaciones", "Comprar tecnologia tambien es tomar decisiones de arquitectura", [
        "Convertir necesidades en capacidades, criterios y escenarios verificables.",
        "Evitar especificaciones que nombren una solucion antes del problema.",
        "Evaluar salida, portabilidad, datos, soporte y costo de cambio.",
    ]),
    ("Vendor lock-in consciente", "La dependencia puede ser una estrategia valida si se hace explicita", [
        "Distinguir lock-in accidental de una eleccion con valor medible.",
        "Definir que capacidades deben ser portables y cuales no.",
        "Mantener datos, contratos y procesos de salida documentados.",
    ]),
    ("Interoperabilidad y estandares", "Los estandares reducen friccion cuando las fronteras son numerosas", [
        "Elegir formatos y protocolos por contexto, madurez y ecosistema.",
        "Definir semantica comun, no solo una sintaxis compatible.",
        "Probar interoperabilidad con consumidores reales y versiones reales.",
    ]),
    ("Migraciones sin detener el negocio", "Cambiar una arquitectura es gestionar estados intermedios", [
        "Separar estado actual, estado objetivo y pasos verificables.",
        "Mantener compatibilidad temporal y una estrategia de retiro.",
        "Definir criterios para avanzar, pausar o revertir cada etapa.",
    ]),
    ("Continuidad de negocio", "Disponibilidad no es lo mismo que capacidad de recuperacion", [
        "Identificar procesos criticos, dependencias y tiempos tolerables.",
        "Definir RTO, RPO y procedimientos que una persona pueda ejecutar.",
        "Probar recuperacion con escenarios y no solo con documentos.",
    ]),
    ("Gestion de incidentes y aprendizaje", "Un incidente debe mejorar el sistema, no solo cerrarse", [
        "Separar respuesta urgente de analisis posterior sin culpabilizar.",
        "Conservar linea de tiempo, impacto, deteccion y decisiones tomadas.",
        "Convertir hallazgos en cambios de arquitectura, pruebas o controles.",
    ]),
    ("Etica de automatizacion e inteligencia artificial", "Automatizar no elimina sesgos, responsabilidad ni necesidad de supervision", [
        "Definir usos permitidos, limites y casos que requieren revision humana.",
        "Evaluar calidad, sesgo, explicabilidad, privacidad y seguridad del modelo.",
        "Registrar datos, versiones y criterios para poder cuestionar el resultado.",
    ]),
    ("Arquitectura para trabajo remoto y asincrono", "La informacion debe viajar sin depender de reuniones constantes", [
        "Preferir decisiones escritas, contexto accesible y acuerdos visibles.",
        "Diseñar flujos de revision que toleren zonas horarias y pausas.",
        "Medir tiempos de espera y cantidad de dependencias entre equipos.",
    ]),
    ("Madurez arquitectonica", "Madurar no es agregar ceremonias: es decidir mejor con menos sorpresa", [
        "Evaluar practica, evidencia y resultados, no cantidad de documentos.",
        "Empezar por los riesgos que mas afectan al producto y a sus usuarios.",
        "Revisar periodicamente si el nivel de control sigue siendo proporcional.",
    ]),
    ("Cierre: una arquitectura que conecta", "Los temas transversales convierten tecnicas sueltas en responsabilidad sistemica", [
        "Toda decision tecnica tiene efectos en personas, negocio y operacion.",
        "La calidad se sostiene con evidencia, ownership y capacidad de aprendizaje.",
        "La pregunta final: que riesgo estamos aceptando y como sabremos si cambio?",
    ]),
]


DEFINITIONS = {
    "Gobierno tecnico sin burocracia": "Es el conjunto de reglas, responsables y espacios para tomar y revisar decisiones tecnicas.",
    "Arquitectura y estrategia de producto": "Es conectar las decisiones de software con el valor, los usuarios y los objetivos del producto.",
    "Portafolio y racionalizacion de aplicaciones": "Es evaluar todas las aplicaciones para decidir en cuales invertir, cambiar, consolidar o retirar.",
    "Arquitectura empresarial ligera": "Es una vista de alto nivel que relaciona capacidades del negocio, procesos, datos, aplicaciones y tecnologia.",
    "FinOps y costo como atributo de calidad": "FinOps es la practica de gestionar el costo de tecnologia con colaboracion entre negocio, ingenieria y finanzas.",
    "Sostenibilidad del software": "Es disenar y operar software usando menos energia y recursos durante todo su ciclo de vida.",
    "Accesibilidad desde la arquitectura": "Es lograr que personas con distintas capacidades puedan usar el sistema y sus contenidos.",
    "Privacidad por diseno": "Es incorporar proteccion y minimizacion de datos desde el diseno, no como correccion posterior.",
    "Cumplimiento y evidencia auditable": "Es convertir leyes, politicas y normas en controles cuya ejecucion pueda demostrarse.",
    "Amenazas de la cadena de suministro": "Son riesgos introducidos por dependencias externas, paquetes, imagenes, herramientas o proveedores.",
    "Identidad, acceso y confianza": "Es comprobar quien solicita una accion y autorizar solo lo que necesita para realizarla.",
    "Gobierno de datos": "Es definir quien es responsable de los datos, que significan, como se protegen y como se comprueba su calidad.",
    "Arquitectura analitica y operacional": "Es separar o coordinar el procesamiento de operaciones del negocio y el analisis historico.",
    "Calidad de decisiones con datos": "Es usar mediciones definidas y confiables para elegir acciones, no solo para llenar tableros.",
    "Experiencia de usuario y arquitectura": "Es considerar como latencia, errores, disponibilidad y estados del sistema afectan a quien lo usa.",
    "Diseno de servicios internos": "Es tratar APIs, librerias y plataformas para otros equipos como productos con usuarios y soporte.",
    "Plataforma interna y golden paths": "Una plataforma interna ofrece capacidades comunes; un golden path es el camino recomendado para usarlas.",
    "Arquitectura y equipos: ley de Conway": "La ley de Conway dice que los sistemas tienden a reflejar las estructuras de comunicacion de sus organizaciones.",
    "Team Topologies aplicado": "Es un modelo para organizar equipos y sus interacciones de modo que el trabajo fluya con menos dependencias.",
    "Conocimiento y bus factor": "Bus factor es cuantas personas podrian ausentarse antes de que un componente quede sin conocimiento operativo suficiente.",
    "Arquitectura para adquisiciones y licitaciones": "Es definir necesidades y criterios tecnicos para comprar soluciones comparables y verificables.",
    "Vendor lock-in consciente": "Es quedar dependiente de un proveedor; puede aceptarse si el beneficio, el costo y la salida estan explicitados.",
    "Interoperabilidad y estandares": "Interoperabilidad es que sistemas diferentes puedan intercambiar datos y usarlos con el mismo significado.",
    "Migraciones sin detener el negocio": "Es cambiar una arquitectura gradualmente mientras la version actual y la nueva conviven de forma controlada.",
    "Continuidad de negocio": "Es la capacidad de mantener o recuperar procesos criticos despues de una interrupcion.",
    "Gestion de incidentes y aprendizaje": "Es responder a fallas, reducir su impacto y convertir lo aprendido en mejoras permanentes.",
    "Etica de automatizacion e inteligencia artificial": "Es evaluar consecuencias, sesgos, limites y responsabilidad cuando una tecnologia toma o recomienda decisiones.",
    "Arquitectura para trabajo remoto y asincrono": "Es organizar herramientas, informacion y decisiones para colaborar sin coincidir siempre en lugar u horario.",
    "Madurez arquitectonica": "Es la capacidad de tomar decisiones consistentes, comprobarlas y aprender sin agregar ceremonias innecesarias.",
}


def add_background(slide):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = PALE
    bg.line.fill.background()
    stripe = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(12.96), 0, Inches(0.373), Inches(7.5))
    stripe.fill.solid()
    stripe.fill.fore_color.rgb = GOLD
    stripe.line.fill.background()


def add_footer(slide, number):
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.65), Inches(7.05), Inches(11.9), Inches(0.012))
    line.fill.solid()
    line.fill.fore_color.rgb = LINE
    line.line.fill.background()
    box = slide.shapes.add_textbox(Inches(0.68), Inches(7.13), Inches(8.5), Inches(0.2))
    p = box.text_frame.paragraphs[0]
    p.text = "ARQUITECTURA DE SOFTWARE  /  TEMAS TRANSVERSALES"
    p.font.name = "Aptos"
    p.font.size = Pt(7)
    p.font.bold = True
    p.font.color.rgb = MUTED
    page = slide.shapes.add_textbox(Inches(11.2), Inches(7.1), Inches(1.2), Inches(0.22))
    p = page.text_frame.paragraphs[0]
    p.text = f"{number:02d} / 30"
    p.alignment = PP_ALIGN.RIGHT
    p.font.name = "Aptos"
    p.font.size = Pt(8)
    p.font.bold = True
    p.font.color.rgb = NAVY


def add_header(slide, title, subtitle, number):
    band = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.12))
    band.fill.solid()
    band.fill.fore_color.rgb = NAVY
    band.line.fill.background()
    marker = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.48), Inches(0.25), Inches(0.08), Inches(0.55))
    marker.fill.solid()
    marker.fill.fore_color.rgb = GOLD
    marker.line.fill.background()
    box = slide.shapes.add_textbox(Inches(0.72), Inches(0.17), Inches(10.6), Inches(0.48))
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = "Aptos Display"
    p.font.size = Pt(21)
    p.font.bold = True
    p.font.color.rgb = WHITE
    sub = slide.shapes.add_textbox(Inches(0.74), Inches(0.73), Inches(10.0), Inches(0.2))
    p = sub.text_frame.paragraphs[0]
    p.text = subtitle
    p.font.name = "Aptos"
    p.font.size = Pt(8)
    p.font.bold = True
    p.font.color.rgb = RGBColor(183, 199, 213)
    num = slide.shapes.add_textbox(Inches(11.5), Inches(0.25), Inches(0.75), Inches(0.4))
    p = num.text_frame.paragraphs[0]
    p.text = f"{number:02d}"
    p.alignment = PP_ALIGN.RIGHT
    p.font.name = "Aptos Display"
    p.font.size = Pt(23)
    p.font.bold = True
    p.font.color.rgb = GOLD
    add_footer(slide, number)


def add_bullet_card(slide, definition, bullets):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.55), Inches(11.85), Inches(4.7))
    card.fill.solid()
    card.fill.fore_color.rgb = WHITE
    card.line.color.rgb = LINE
    card.line.width = 1
    label = slide.shapes.add_textbox(Inches(1.25), Inches(1.82), Inches(1.0), Inches(0.25))
    p = label.text_frame.paragraphs[0]
    p.text = "QUE ES"
    p.font.name = "Aptos"
    p.font.size = Pt(9)
    p.font.bold = True
    p.font.color.rgb = TEAL
    definition_box = slide.shapes.add_textbox(Inches(1.25), Inches(2.05), Inches(10.8), Inches(0.62))
    definition_frame = definition_box.text_frame
    definition_frame.word_wrap = True
    p = definition_frame.paragraphs[0]
    p.text = definition
    p.font.name = "Aptos"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = NAVY
    tf = slide.shapes.add_textbox(Inches(1.25), Inches(2.82), Inches(10.8), Inches(2.9)).text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    for index, text in enumerate(bullets):
        paragraph = tf.paragraphs[0] if index == 0 else tf.add_paragraph()
        paragraph.text = f"- {text}"
        paragraph.font.name = "Aptos"
        paragraph.font.size = Pt(17 if len(text) < 90 else 15)
        paragraph.font.color.rgb = INK
        paragraph.space_after = Pt(14)
        paragraph.level = 0


def add_cover(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_background(slide)
    band = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(2.05))
    band.fill.solid()
    band.fill.fore_color.rgb = NAVY
    band.line.fill.background()
    eyebrow = slide.shapes.add_textbox(Inches(0.85), Inches(0.72), Inches(8), Inches(0.3))
    p = eyebrow.text_frame.paragraphs[0]
    p.text = "ARQUITECTURA DE SOFTWARE  /  SESION COMPLEMENTARIA"
    p.font.name = "Aptos"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = RGBColor(183, 199, 213)
    title = slide.shapes.add_textbox(Inches(0.82), Inches(2.55), Inches(11.0), Inches(1.2))
    p = title.text_frame.paragraphs[0]
    p.text = "30 temas transversales\npara conectar la arquitectura"
    p.font.name = "Aptos Display"
    p.font.size = Pt(30)
    p.font.bold = True
    p.font.color.rgb = NAVY
    intro = slide.shapes.add_textbox(Inches(0.86), Inches(4.18), Inches(9.8), Inches(1.0))
    p = intro.text_frame.paragraphs[0]
    p.text = "Una mirada complementaria a los videos: gobierno, producto, personas, datos, costos, regulacion, sostenibilidad y aprendizaje operativo."
    p.font.name = "Aptos"
    p.font.size = Pt(18)
    p.font.color.rgb = INK
    tag = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.86), Inches(5.75), Inches(3.2), Inches(0.55))
    tag.fill.solid()
    tag.fill.fore_color.rgb = TEAL
    tag.line.fill.background()
    p = tag.text_frame.paragraphs[0]
    p.text = "Material de apoyo para exposicion"
    p.alignment = PP_ALIGN.CENTER
    p.font.name = "Aptos"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = WHITE
    add_footer(slide, 1)


def build():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    add_cover(prs)
    for number, (title, subtitle, bullets) in enumerate(SLIDES[:29], start=2):
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        add_background(slide)
        add_header(slide, title, subtitle, number)
        add_bullet_card(slide, DEFINITIONS[title], bullets)
    prs.save(OUT)
    print(f"Generadas {len(prs.slides)} diapositivas: {OUT}")


if __name__ == "__main__":
    build()