"""Fetch this week's AI news from trusted RSS feeds."""

import feedparser

AI_FEEDS = [
    "https://openai.com/news/rss.xml",
    "https://blog.google/technology/ai/rss/",
    "https://www.anthropic.com/news/rss.xml",
    "https://venturebeat.com/category/ai/feed/",
]


def fetch_news(limit=20):
    articles = []
    for feed in AI_FEEDS:
        try:
            parsed = feedparser.parse(feed)
            for entry in parsed.entries[:5]:
                articles.append({
                    "title": entry.get("title", ""),
                    "link": entry.get("link", ""),
                    "published": entry.get("published", ""),
                    "summary": entry.get("summary", "")
                })
        except Exception:
            continue
    return articles[:limit]
