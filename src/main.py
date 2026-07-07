"""AI Weekly Reporter entry point."""

from src.config import validate
from src.news_fetcher import fetch_news
from src.report_generator import generate_weekly_report
from src.email_sender import send_report
from src.utils import report_title, executive_summary


def main():
    validate()

    articles = fetch_news()
    report = generate_weekly_report(articles)
    title = report_title()

    # Save the report instead of using Google Docs
    filename = "weekly_report.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(report)

    summary = executive_summary(report)

    # Email the local file name instead of a Google Docs link
    send_report(title, summary, filename)

    print(f"Done! Report saved to {filename}")


if __name__ == "__main__":
    main()
