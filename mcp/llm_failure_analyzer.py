from mcp.llm_client import generate_response


class LLMFailureAnalyzer:
    @staticmethod
    def analyze(error):
        prompt = f"""
Analyze this Selenium automation failure.

Error:
{error}

Provide:
1. Root Cause
2. Fix Suggestion
3. Prevention Recommendation
"""

        return generate_response(
            prompt,
            system_prompt=("You are an expert Selenium failure analyzer."),
        )
