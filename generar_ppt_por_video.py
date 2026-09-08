from pathlib import Path
import re

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

BASE = Path(r"c:\proj\itm\OPTATIVA_II")
SRC = BASE / "materiales" / "materiales_por_video" / "serie_60_videos"
OUT = SRC / "pptx_por_video"
OUT.mkdir(parents=True, exist_ok=True)

TITLE_BG = RGBColor(9, 23, 42)
ACCENT = RGBColor(224, 178, 76)
LIGHT_BG = RGBColor(239, 243, 247)
CARD_BG = RGBColor(255, 255, 255)
TEXT = RGBColor(28, 39, 52)
MUTED = RGBColor(91, 105, 119)
BORDER = RGBColor(210, 219, 227)
TEAL = RGBColor(35, 147, 145)
WHITE = RGBColor(255, 255, 255)


def clean_text(value: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", value.replace("\r", "")).strip()


def parse_video_file(path: Path):
    text = path.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+(.*)$", text, flags=re.M)
    title = title_match.group(1).strip() if title_match else path.stem.replace("-", " ").title()

    def section(name: str):
        pattern = rf"##\s+{re.escape(name)}\s*\n(.*?)(?=\n##\s+|\Z)"
        m = re.search(pattern, text, flags=re.S)
        if not m:
            return ""
        return clean_text(m.group(1))

    resumen = section("Resumen")
    purpose = section("Propósito de aprendizaje")
    opening = section("Apertura de la clase")
    explanation = section("Explicación paso a paso")
    practice = section("Práctica guiada")
    ideas = section("Ideas principales")
    conclusion = section("Conclusión")
    preguntas = section("Preguntas para reflexión")
    ejemplo = section("Ejemplo en C#")

    # Use first paragraph of summary if available.
    summary_text = re.sub(r"\n+", " ", resumen)
    summary_text = re.sub(r"\s+", " ", summary_text).strip()

    bullets = []
    for line in ideas.splitlines():
        s = line.strip()
        if s.startswith("- "):
            bullets.append(s[2:].strip())
        elif s:
            bullets.append(s)

    questions = []
    for line in preguntas.splitlines():
        s = line.strip()
        if s.startswith("- "):
            questions.append(s[2:].strip())
        elif s:
            questions.append(s)

    result = {
        "num": int(path.stem.split("-")[-1]),
        "title": title,
        "summary": summary_text,
        "purpose": purpose,
        "opening": opening,
        "explanation": explanation,
        "practice": practice,
        "ideas": bullets[:5],
        "conclusion": conclusion,
        "questions": questions[:4],
        "example": ejemplo,
    }
    return result


def add_background(slide):
    shp = slide.shapes.add_shape(1, 0, 0, Inches(13.333), Inches(7.5))
    shp.fill.solid()
    shp.fill.fore_color.rgb = LIGHT_BG
    shp.line.fill.background()

    accent = slide.shapes.add_shape(1, Inches(12.96), 0, Inches(0.37), Inches(7.5))
    accent.fill.solid()
    accent.fill.fore_color.rgb = ACCENT
    accent.line.fill.background()


def add_footer(slide, video_number, section_number):
    line = slide.shapes.add_shape(1, Inches(0.55), Inches(7.08), Inches(12.05), Inches(0.015))
    line.fill.solid()
    line.fill.fore_color.rgb = BORDER
    line.line.fill.background()

    left = slide.shapes.add_textbox(Inches(0.6), Inches(7.14), Inches(6.0), Inches(0.2))
    left_tf = left.text_frame
    left_tf.margin_left = 0
    left_tf.margin_right = 0
    left_p = left_tf.paragraphs[0]
    left_p.text = "ARQUITECTURA DE SOFTWARE  /  MATERIAL DE CLASE"
    left_p.font.name = "Aptos"
    left_p.font.size = Pt(7)
    left_p.font.bold = True
    left_p.font.color.rgb = MUTED

    right = slide.shapes.add_textbox(Inches(10.7), Inches(7.1), Inches(1.7), Inches(0.25))
    right_tf = right.text_frame
    right_tf.margin_left = 0
    right_tf.margin_right = 0
    right_p = right_tf.paragraphs[0]
    right_p.text = f"VIDEO {video_number:02d}  /  {section_number}"
    right_p.alignment = PP_ALIGN.RIGHT
    right_p.font.name = "Aptos"
    right_p.font.size = Pt(8)
    right_p.font.bold = True
    right_p.font.color.rgb = TITLE_BG


def add_header(slide, title, subtitle, video_number, section_number):
    band = slide.shapes.add_shape(1, 0, 0, Inches(13.333), Inches(1.08))
    band.fill.solid()
    band.fill.fore_color.rgb = TITLE_BG
    band.line.fill.background()

    marker = slide.shapes.add_shape(1, Inches(0.45), Inches(0.23), Inches(0.08), Inches(0.52))
    marker.fill.solid()
    marker.fill.fore_color.rgb = ACCENT
    marker.line.fill.background()

    box = slide.shapes.add_textbox(Inches(0.7), Inches(0.14), Inches(11.0), Inches(0.47))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = 0
    tf.margin_right = 0
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = "Aptos Display"
    p.font.bold = True
    p.font.size = Pt(19)
    p.font.color.rgb = WHITE

    sub = slide.shapes.add_textbox(Inches(0.72), Inches(0.72), Inches(8.5), Inches(0.22))
    stf = sub.text_frame
    stf.margin_left = 0
    stf.margin_right = 0
    sp = stf.paragraphs[0]
    sp.text = subtitle
    sp.font.name = "Aptos"
    sp.font.size = Pt(8)
    sp.font.color.rgb = RGBColor(183, 199, 213)
    sp.font.bold = True

    number = slide.shapes.add_textbox(Inches(11.55), Inches(0.28), Inches(0.75), Inches(0.4))
    ntf = number.text_frame
    np = ntf.paragraphs[0]
    np.text = f"{video_number:02d}"
    np.alignment = PP_ALIGN.RIGHT
    np.font.name = "Aptos Display"
    np.font.size = Pt(23)
    np.font.bold = True
    np.font.color.rgb = ACCENT

    add_footer(slide, video_number, section_number)


def add_card(slide, x, y, w, h, title, body_lines, title_color=TITLE_BG, font_size=14):
    card = slide.shapes.add_shape(5, Inches(x), Inches(y), Inches(w), Inches(h))
    card.fill.solid()
    card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = BORDER
    card.line.width = 1

    tb = slide.shapes.add_textbox(Inches(x + 0.18), Inches(y + 0.12), Inches(w - 0.35), Inches(h - 0.15)).text_frame
    tb.word_wrap = True
    tb.margin_left = Inches(0.04)
    tb.margin_right = Inches(0.04)
    tb.margin_top = Inches(0.02)
    tb.vertical_anchor = MSO_ANCHOR.TOP

    p = tb.paragraphs[0]
    p.text = title
    p.font.name = "Aptos Display"
    p.font.bold = True
    p.font.size = Pt(font_size)
    p.font.color.rgb = title_color

    for idx, line in enumerate(body_lines[:6]):
        para = tb.add_paragraph()
        para.text = line if idx == 0 else line
        para.level = 0
        para.font.size = Pt(12 if len(line) > 90 else 13)
        para.font.name = "Aptos"
        para.font.color.rgb = TEXT
        para.space_after = Pt(4)
        if idx == 0 and body_lines:
            para.font.bold = False


def add_bullets(slide, x, y, w, h, title, bullets, title_color=TITLE_BG):
    card = slide.shapes.add_shape(5, Inches(x), Inches(y), Inches(w), Inches(h))
    card.fill.solid()
    card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = BORDER
    card.line.width = 1

    tb = slide.shapes.add_textbox(Inches(x + 0.18), Inches(y + 0.12), Inches(w - 0.22), Inches(h - 0.16)).text_frame
    tb.word_wrap = True
    tb.margin_left = Inches(0.04)
    tb.margin_right = Inches(0.04)
    p = tb.paragraphs[0]
    p.text = title
    p.font.name = "Aptos Display"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = title_color
    for bullet in bullets[:6]:
        para = tb.add_paragraph()
        para.text = f"• {bullet}"
        para.level = 0
        para.font.size = Pt(12)
        para.font.name = "Aptos"
        para.font.color.rgb = TEXT
        para.bullet = True
        para.space_after = Pt(5)


def add_cover_slide(prs, video):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_background(slide)
    add_header(slide, f"Video {video['num']} — {video['title']}", "Material de apoyo para exposición", video['num'], "01 / 03")

    eyebrow = slide.shapes.add_textbox(Inches(0.82), Inches(1.5), Inches(3.5), Inches(0.28))
    etf = eyebrow.text_frame
    ep = etf.paragraphs[0]
    ep.text = "ARQUITECTURA  /  SESIÓN DE APRENDIZAJE"
    ep.font.name = "Aptos"
    ep.font.size = Pt(9)
    ep.font.bold = True
    ep.font.color.rgb = TEAL

    # main title block
    box = slide.shapes.add_textbox(Inches(0.8), Inches(1.82), Inches(11.3), Inches(1.0))
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = video['title']
    p.font.name = "Aptos Display"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = TITLE_BG

    summary_lines = []
    for chunk in re.split(r"(?<=[.!?])\s+", video['summary'][:420]):
        chunk = chunk.strip()
        if chunk:
            summary_lines.append(chunk)
    add_card(slide, 0.8, 3.15, 11.8, 2.65, "Resumen del tema", summary_lines[:4], title_color=TEAL, font_size=16)


def add_content_slide(prs, video):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_background(slide)
    add_header(slide, f"Video {video['num']} — {video['title']}", "Ideas principales", video['num'], "02 / 03")

    add_bullets(slide, 0.65, 1.55, 5.9, 5.25, "Ideas clave", video['ideas'] or [video['summary'][:180]], title_color=TEAL)

    ctx = []
    if video['example']:
        example_text = re.sub(r"```.*?```", "", video['example'], flags=re.S)
        example_text = re.sub(r"#|\*\*|_", "", example_text)
        example_lines = [line.strip() for line in example_text.splitlines() if line.strip()]
        ctx = example_lines[:7]
    else:
        ctx = [video['summary'][:180]]

    add_card(slide, 6.8, 1.55, 5.9, 5.25, "Ejemplo aplicado", ctx, title_color=ACCENT, font_size=15)


def add_class_slide(prs, video):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_background(slide)
    add_header(slide, f"Video {video['num']} — {video['title']}", "Clase en acción", video['num'], "03 / 04")

    purpose = video['purpose'] or "Aplicar el concepto al caso de la plataforma logística."
    opening = video['opening'] or video['summary']
    practice = video['practice'] or "Construir una evidencia pequeña y justificar la decisión tomada."
    add_card(slide, 0.65, 1.45, 12.05, 1.35, "Propósito de aprendizaje", [purpose], title_color=TEAL, font_size=15)
    add_card(slide, 0.65, 3.0, 5.9, 3.25, "Apertura y explicación", [opening, video['explanation'][:450]], title_color=ACCENT, font_size=14)
    add_card(slide, 6.8, 3.0, 5.9, 3.25, "Práctica guiada", [practice, "Evidencia: decisión, alternativa, trade-off y verificación."], title_color=TEAL, font_size=14)


def add_reflection_slide(prs, video):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_background(slide)
    add_header(slide, f"Video {video['num']} — {video['title']}", "Conclusión y reflexión", video['num'], "04 / 04")

    conclusion_text = video['conclusion'][:600] if video['conclusion'] else video['summary'][:600]
    conclusion_lines = [part.strip() for part in re.split(r"(?<=[.!?])\s+", conclusion_text) if part.strip()][:4]
    add_card(slide, 0.7, 1.55, 6.1, 4.85, "Conclusión", conclusion_lines, title_color=TEAL, font_size=15)

    q_lines = video['questions'][:4] if video['questions'] else [
        "¿Qué decisión arquitectónica afecta más la calidad del sistema?",
        "¿Qué riesgo real aparece si no se define un límite claro?",
    ]
    add_bullets(slide, 6.9, 1.55, 5.8, 4.85, "Preguntas para reflexión", q_lines, title_color=ACCENT)


def build_ppt_for_video(video_path: Path):
    video = parse_video_file(video_path)
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    add_cover_slide(prs, video)
    add_content_slide(prs, video)
    add_class_slide(prs, video)
    add_reflection_slide(prs, video)

    out_file = OUT / f"video-{video['num']:02d}.pptx"
    prs.save(out_file)
    return out_file


def main():
    files = sorted(SRC.glob("video-*.md"))
    valid_names = {f"video-{int(file.stem.split('-')[-1]):02d}.pptx" for file in files}
    for old_file in OUT.glob("*.pptx"):
        if old_file.name not in valid_names:
            try:
                old_file.unlink()
            except PermissionError:
                pass
    created = []
    for file in files:
        out = build_ppt_for_video(file)
        created.append(out)
    print(f"OK: {len(created)} presentaciones creadas en {OUT}")
    for item in created[:3]:
        print(item)
    if len(created) > 3:
        print("...")


if __name__ == "__main__":
    main()
