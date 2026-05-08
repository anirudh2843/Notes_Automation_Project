from mcp.llm_client import LLMClient


class LLMFailureAnalyzer:
    @staticmethod
    def analyze(exception):
        prompt = f"""

        Analyze Selenium failure:

        {str(exception)}

        Suggest fix.
        """

        return LLMClient.generate(prompt)
