import os
from openai import OpenAI

def generate_story():
    client = OpenAI(
        api_key=os.environ["OPENROUTER_API_KEY"],
        base_url="https://openrouter.ai/api/v1",
    )

    messages = [
        {
            "role": "user",
            "content": "Write a short motivational story for kids about discipline and consistency."
        }
    ]

    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=messages,
        )
        story = response.choices[0].message.content
        print("✅ Story generated successfully")
        return story
    except Exception as e:
        print("❌ Failed to generate story:", e)
        return None
