from langchain_core.prompts import PromptTemplate


class LLMClient:
    @staticmethod
    def generate(prompt):
        return f"AI Response Generated for: {prompt}"
