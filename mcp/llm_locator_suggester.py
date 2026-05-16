from mcp.llm_client import generate_response


class LLMLocatorSuggestor:
    @staticmethod
    def suggest_locator(failed_locator, page_source):
        prompt = f"""
You are an expert Selenium automation engineer.

A Selenium locator failed.

Failed Locator:
{failed_locator}

The failed locator belongs to a LOGIN SUBMIT BUTTON.

Analyze the HTML carefully.

Suggest ONLY XPath locators for the LOGIN BUTTON.

Rules:
- Focus only on login submit button
- Prefer button elements
- Prefer type='submit'
- Prefer text()='Login'
- Return ONLY a valid Python list
- Do NOT explain anything
- Do NOT add markdown
- Do NOT add comments

HTML:
{page_source[:15000]}

Example:
[
    "//button[contains(text(),'Login')]",
    "//button[@type='submit']",
    "//button[@type='submit' and text()='Login']"
]
"""

        response = generate_response(
            prompt,
            system_prompt=("You are an expert Selenium locator healing engine."),
        )

        return response
