"""Utility helpers for AI Weekly Reporter."""

from datetime import datetime


def report_title():
    return f"Weekly AI Research Report - {datetime.now().strftime('%d %B %Y')}"


def executive_summary(report: str, max_lines: int = 8):
    lines = [line for line in report.splitlines() if line.strip()]
    return "\n".join(lines[:max_lines])


def google_doc_url(document_id: str) -> str:
    return f"https://docs.google.com/document/d/{document_id}/edit"
