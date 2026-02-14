import os
from openai import OpenAI

def generate_story():
    client = OpenAI(
        api_key=os.environ["OPENROUTER_API_KEY"],
        base_url="https://openrouter.ai/api/v1",
    )

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "Write a short motivational story about discipline and consistency."
            }
        ],
    )

    return response.choices[0].message.content
