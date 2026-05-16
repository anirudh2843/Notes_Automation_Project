import json

from mcp.llm_client import generate_response


class LLMTestDataGenerator:
    @staticmethod
    def generate_note():
        prompt = """
Generate realistic test data for a Notes application.

Return ONLY ONE valid JSON object.

Format:
{
    "title": "",
    "description": "",
    "category": ""
}

Rules:
- category must be one of:
  Home
  Work
  Personal
- Do NOT return a list
- Do NOT explain anything
- Do NOT add markdown
"""

        response = generate_response(
            prompt,
            system_prompt=("You are an expert QA test data generator."),
        )

        try:
            data = json.loads(response)

            # If AI accidentally returns list
            if isinstance(data, list):
                data = data[0]

            return data

        except Exception:
            return {
                "title": "AI Generated Note",
                "description": "Fallback Description",
                "category": "Home",
            }
