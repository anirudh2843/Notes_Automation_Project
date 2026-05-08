class LLMLocatorSuggester:
    @staticmethod
    def suggest(locator):
        by, value = locator

        suggestions = []

        if "xpath" in by.lower():
            suggestions.append("Prefer ID locator")

            suggestions.append("Use data-testid locator")

            suggestions.append("Avoid absolute XPath")

        return suggestions
