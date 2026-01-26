from twilio.rest import Client
import os

def send_whatsapp(story):
    sid = os.getenv("TWILIO_SID")
    token = os.getenv("TWILIO_AUTH_TOKEN")
    from_whatsapp = os.getenv("TWILIO_WHATSAPP_FROM")
    to_whatsapp = os.getenv("WHATSAPP_TO")  # set this to group number (sandbox number must be in group)

    if not all([sid, token, from_whatsapp, to_whatsapp]):
        print("❌ Twilio environment variables not set!")
        return

    client = Client(sid, token)
    message = client.messages.create(
        body=story,
        from_=from_whatsapp,
        to=to_whatsapp
    )

    print(f"📩 WhatsApp group message sent! SID: {message.sid}")
