import os
import requests
import random
from datetime import datetime
from twilio.rest import Client

# ============================
# Hugging Face API Setup
# ============================
HF_API_KEY = os.getenv("HF_API_KEY")
MODEL_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

# ============================
# Story Topics
# ============================
TOPICS = [
    "a tiny seed growing into a tree",
    "a brave little kitten learning to climb",
    "two friends solving a mystery in the park",
    "a lost puppy finding its way home",
    "a child learning to ride a bicycle",
    "a magical balloon that teaches courage",
    "a cloud who wanted to touch the rainbow"
]

# ============================
# Generate Story
# ============================
def generate_story():
    topic = random.choice(TOPICS)

    prompt = f"""
Write a fun, motivational story for kids about {topic}.
The story should:
- Have at least 3 paragraphs (beginning, middle, end)
- Include at least 2 characters or objects
- Include a challenge and a solution
- End with a happy ending and a simple lesson
- Be playful, exciting, and suitable for ages 5-10
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 400,
            "temperature": 0.9,
            "top_p": 0.95,
            "do_sample": True
        }
    }

    try:
        response = requests.post(MODEL_URL, headers=HEADERS, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"].strip()
    except Exception as e:
        print(f"⚠️ Hugging Face API failed: {e}")

    # Fallback story in case API fails
    return (
        "Once upon a time, a little star wanted to shine bright, "
        "but the clouds covered the sky. 🌥️\n"
        "It didn’t give up and practiced every night, twinkling a little more each time. ✨\n"
        "Soon, the star shone so brightly that everyone in the sky admired it. 🌟\n"
        "The lesson: even small efforts can lead to great success!"
    )

# ============================
# Save Story to File
# ============================
def save_story(story):
    os.makedirs("stories", exist_ok=True)
    filename = f"stories/story_{datetime.now().strftime('%Y-%m-%d')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(story)
    print(f"💾 Story saved to {filename}")

# ============================
# Send WhatsApp Message
# ============================
def send_whatsapp(story):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_whatsapp = os.getenv("TWILIO_WHATSAPP_FROM")
    to_whatsapp = os.getenv("TWILIO_WHATSAPP_TO")

    if not all([account_sid, auth_token, from_whatsapp, to_whatsapp]):
        print("❌ Twilio environment variables not set!")
        return

    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=story,
            from_=f"whatsapp:{from_whatsapp}",
            to=f"whatsapp:{to_whatsapp}"
        )
        print(f"📩 WhatsApp message sent! SID: {message.sid}")
    except Exception as e:
        print(f"⚠️ Failed to send WhatsApp message: {e}")

# ============================
# Test Run
# ============================
if __name__ == "__main__":
    story = generate_story()
    print("\n🌟 Your Motivational Story 🌟\n")
    print(story)
    save_story(story)
    send_whatsapp(story)
