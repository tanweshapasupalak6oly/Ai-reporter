from src.gemini_client import GeminiClient
from src.prompts import SYSTEM_PROMPT


def build_prompt(articles):
    news = "\n\n".join(
        f"Title: {a['title']}\nDate: {a['published']}\nSummary: {a['summary']}\nSource: {a['link']}"
        for a in articles
    )
    return f"{SYSTEM_PROMPT}\n\nWeekly AI News:\n{news}"


def generate_weekly_report(articles):
    client = GeminiClient()
    prompt = build_prompt(articles)
    return client.generate_report(prompt)
