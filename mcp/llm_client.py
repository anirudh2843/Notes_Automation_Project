from openai import OpenAI

from config.config_reader import Config


client = OpenAI(
    api_key=Config.OPENAI_API_KEY,
    base_url=Config.OPENAI_BASE_URL,
)


def generate_response(
    prompt,
    system_prompt="You are an AI automation assistant.",
):
    response = client.chat.completions.create(
        model=Config.OPENAI_MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0,
    )

    return response.choices[0].message.content
