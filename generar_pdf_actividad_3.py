from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, PageBreak, Preformatted

BASE = Path(r"C:\proj\itm\OPTATIVA_II")
SOURCE = BASE / "materiales" / "actividad_3_dominio_y_diseno.md"
OUTPUT = BASE / "materiales" / "actividad_3_dominio_y_diseno.pdf"


def inline_markup(text):
    text = escape(text)
    text = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    return text


def build_pdf():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleCustom", parent=styles["Title"], alignment=TA_CENTER, fontSize=20, leading=25, spaceAfter=18))
    styles.add(ParagraphStyle(name="HeadingCustom", parent=styles["Heading2"], fontSize=14, leading=18, spaceBefore=12, spaceAfter=7, textColor="#123B5D"))
    styles.add(ParagraphStyle(name="SubheadingCustom", parent=styles["Heading3"], fontSize=11, leading=14, spaceBefore=8, spaceAfter=5, textColor="#2D6A7F"))
    styles.add(ParagraphStyle(name="BodyCustom", parent=styles["BodyText"], fontSize=9.5, leading=13, spaceAfter=6))
    styles.add(ParagraphStyle(name="BulletCustom", parent=styles["BodyText"], fontSize=9.5, leading=13, leftIndent=16, firstLineIndent=-9, spaceAfter=3))

    story = []
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    code = False
    code_lines = []

    for raw in lines:
        line = raw.rstrip()
        if line.startswith("```"):
            if code:
                story.append(Preformatted("\n".join(code_lines), styles["Code"]))
                story.append(Spacer(1, 6))
                code_lines = []
            code = not code
            continue
        if code:
            code_lines.append(line)
            continue
        if not line:
            continue
        if line == "---":
            story.append(Spacer(1, 8))
            continue
        if line.startswith("# "):
            story.append(Paragraph(inline_markup(line[2:]), styles["TitleCustom"]))
        elif line.startswith("## "):
            story.append(Paragraph(inline_markup(line[3:]), styles["HeadingCustom"]))
        elif line.startswith("### "):
            story.append(Paragraph(inline_markup(line[4:]), styles["SubheadingCustom"]))
        elif line.startswith("- "):
            story.append(Paragraph("&#8226; " + inline_markup(line[2:]), styles["BulletCustom"]))
        elif re.match(r"^\d+\. ", line):
            story.append(Paragraph(inline_markup(line), styles["BulletCustom"]))
        elif line.startswith("> "):
            story.append(Paragraph("<i>" + inline_markup(line[2:]) + "</i>", styles["BodyCustom"]))
        else:
            story.append(Paragraph(inline_markup(line), styles["BodyCustom"]))

    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=letter,
        rightMargin=0.65 * inch,
        leftMargin=0.65 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch,
        title="Actividad 3: Diseño y dominio",
        author="OPTATIVA II",
    )
    doc.build(story)
    print(f"PDF generado: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
