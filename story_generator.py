import os
from openrouter import OpenRouter

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenRouterAPI(api_key=OPENROUTER_API_KEY)

def generate_story():
    prompt = """
    Write a short motivational story for kids (5–7 sentences).
    Make it positive, creative, and inspiring.
    End with a hopeful lesson.
    """

    response = client.text.create(
        model="gpt-j-6B-instruct",  # free/open friendly
        input=prompt,
        max_output_tokens=180
    )

    # some backends return text differently
    return response.get("output_text") or response.get("output", "")
