import os
import requests
import random
from datetime import datetime

HF_API_KEY = os.getenv("HF_API_KEY")
MODEL_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

TOPICS = [
    "never giving up",
    "being kind to others",
    "believing in yourself",
    "helping friends",
    "trying again after failure",
    "loving nature",
    "being brave",
    "sharing and caring"
]

def generate_story():
    topic = random.choice(TOPICS)

    prompt = f"""
Write a short, fun, motivational story for kids about {topic}.
The story should:
- Be positive and encouraging
- Have a clear beginning, middle, and happy ending
- Be under 300 words
- End with a simple lesson
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 250,
            "temperature": 0.9,
            "top_p": 0.95,
            "do_sample": True
        }
    }

    response = requests.post(MODEL_URL, headers=headers, json=payload)
    result = response.json()

    if isinstance(result, list) and "generated_text" in result[0]:
        return result[0]["generated_text"].strip()

    return "Once upon a time, a little star learned to shine bright even on cloudy days. 🌟"

def save_story(story):
    os.makedirs("stories", exist_ok=True)
    filename = f"stories/story_{datetime.now().strftime('%Y-%m-%d')}.txt"
    with open(filename, "w") as f:
        f.write(story)
    print(f"💾 Story saved to {filename}")

def send_whatsapp(story):
    from twilio.rest import Client

    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_whatsapp = os.getenv("TWILIO_WHATSAPP_FROM")
    to_whatsapp = os.getenv("TWILIO_WHATSAPP_TO")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=story,
        from_=f"whatsapp:{from_whatsapp}",
        to=f"whatsapp:{to_whatsapp}"
    )

    print(f"📩 WhatsApp message sent! SID: {message.sid}")
