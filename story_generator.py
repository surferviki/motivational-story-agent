import os
from datetime import datetime
# Comment out OpenAI import for now
# from openai import OpenAI
# from twilio.rest import Client  # We'll import Twilio only where needed

# ============================
# STORY GENERATION FUNCTION
# ============================
def generate_story():
    # Mock story for testing
    story = (
        "Once upon a time, there was a small seed that wanted to grow into a big tree. "
        "Every day, it soaked up sunlight and drank water, even when storms came. "
        "The seed never gave up, and slowly it grew taller and stronger. "
        "One day, it became the tallest tree in the forest, giving shade and shelter to everyone. "
        "Remember, no matter how small you start, patience and effort will make you flourish!"
    )
    return story

# ============================
# SAVE STORY TO FILE
# ============================
def save_story(story):
    os.makedirs("stories", exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"stories/story_{today}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(story)
    print(f"💾 Story saved to {filename}")

# ============================
# SEND WHATSAPP MESSAGE
# ============================
from twilio.rest import Client

def send_whatsapp(story):
    sid = os.getenv("TWILIO_SID")
    token = os.getenv("TWILIO_AUTH_TOKEN")
    from_whatsapp = os.getenv("TWILIO_WHATSAPP_FROM")
    to_whatsapp = os.getenv("WHATSAPP_TO")

    if not all([sid, token, from_whatsapp, to_whatsapp]):
        print("❌ Twilio environment variables not set!")
        return

    client = Client(sid, token)
    message = client.messages.create(
        body=story,
        from_=from_whatsapp,
        to=to_whatsapp
    )
    print(f"📩 WhatsApp message sent! SID: {message.sid}")

# ============================
# RUN DIRECTLY
# ============================
if __name__ == "__main__":
    story = generate_story()
    print("\n🌟 Your Motivational Story 🌟\n")
    print(story)
    save_story(story)
    send_whatsapp(story)
