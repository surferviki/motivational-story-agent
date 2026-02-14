from openrouter import OpenRouter
import os

def generate_story():
    client = OpenRouter(
        api_key=os.environ["OPENROUTER_API_KEY"]
    )

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "Write a short motivational story about discipline and consistency."
            }
        ]
    )

    return response.choices[0].message.content
