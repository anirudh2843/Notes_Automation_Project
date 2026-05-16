from mcp.llm_client import generate_response


class LLMLocatorSuggestor:
    @staticmethod
    def suggest_locator(failed_locator, page_source):
        prompt = f"""
You are an expert Selenium automation engineer.

A Selenium locator failed.

Failed Locator:
{failed_locator}

Analyze the HTML carefully.

Suggest alternative XPath or CSS locators
for the FAILED element.

Rules:
- Prefer stable locators
- Prefer id
- Prefer name
- Prefer data-testid
- Return ONLY valid Python list
- Do NOT explain anything
- Do NOT add markdown
- Focus ONLY on the failed element

HTML:
{page_source[:15000]}

Example:
[
    "//input[@id='email']",
    "//button[@type='submit']"
]
"""

        return generate_response(
            prompt,
            system_prompt=("You are an expert Selenium locator healing engine."),
        )
