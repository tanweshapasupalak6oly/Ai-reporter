"""Gemini client wrapper for AI Weekly Reporter."""

import os
from google import genai


class GeminiClient:
    def __init__(self):
        self.client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        self.model = "gemini-2.5-flash"

    def generate_report(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )
        return response.text
