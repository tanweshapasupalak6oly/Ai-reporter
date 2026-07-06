"""AI Weekly Reporter entry point."""

from src.config import validate
from src.news_fetcher import fetch_news
from src.report_generator import generate_weekly_report
from src.google_docs import create_report
from src.email_sender import send_report
from src.utils import report_title, executive_summary, google_doc_url


def main():
    validate()
    articles = fetch_news()
    report = generate_weekly_report(articles)
    title = report_title()
    doc_id = create_report(title, report)
    doc_url = google_doc_url(doc_id)
    summary = executive_summary(report)
    send_report(title, summary, doc_url)
    print(f"Done! Report created: {doc_url}")


if __name__ == '__main__':
    main()