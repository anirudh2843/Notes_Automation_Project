import uuid

from mcp.llm_client import LLMClient


class LLMTestDataGenerator:
    @staticmethod
    def generate_note():
        unique_id = uuid.uuid4().hex[:5]

        prompt = f"""

        Generate test data
        for notes application.
        """

        LLMClient.generate(prompt)

        return {
            "title": f"AI Note {unique_id}",
            "description": (f"AI Generated Description {unique_id}"),
            "category": "Home",
        }
