"""HTML email template helpers."""

from html import escape


def build_html_email(title: str, summary: str, doc_url: str) -> str:
    return f"""<html><body><h1>{escape(title)}</h1><h2>Executive Summary</h2><pre>{escape(summary)}</pre><p><a href='{escape(doc_url)}'>Open Google Doc</a></p></body></html>"""
