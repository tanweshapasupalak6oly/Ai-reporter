"""Export AI reports as PDF."""

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def export_pdf(report_text: str, output_path: str):
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(output_path)
    story = []
    for line in report_text.split("\n"):
        story.append(Paragraph(line or " ", styles["BodyText"]))
    doc.build(story)
    return output_path