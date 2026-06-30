import os
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

class Summarizer:

    def summarize(self, text: str) -> str:

        if not text or not text.strip():
            return ""

        clean_text = re.sub(
            r"^Subject:.*\n?",
            "",
            text,
            flags=re.IGNORECASE
        ).strip()

        prompt = f"""
You are an expert email summarizer.

Summarize the following email in ONLY 3 to 5 sentences.

Rules:
- Return ONLY the summary.
- No headings.
- No bullet points.
- Maximum 80 words.
- Focus on the main purpose.
- Mention only important information.
- Ignore greetings, signatures and repeated details.

Email:

{clean_text}
"""

        try:

            response = client.chat.completions.create(
                model="openai/gpt-4.1-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert business email summarizer."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2,
                max_tokens=150
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            return f"Error: {e}"