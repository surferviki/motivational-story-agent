import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_story():
    prompt = """
Write a short motivational story (5–7 sentences).
Make it positive, simple, and inspiring.
End with a hopeful message.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a kind motivational storyteller."},
            {"role": "user", "content": prompt}
        ]
    )

    story = response.choices[0].message.content
    return story


if __name__ == "__main__":
    story = generate_story()
    print("\n🌟 Your Motivational Story 🌟\n")
    print(story)
