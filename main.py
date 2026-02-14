import os
from story_generator import generate_story
from email_sender import send_email

def main():
    story = generate_story()
    print("Generated Story:\n", story)

    subject = "🌟 Your Weekly Motivational Story!"
    body = story
    recipient = os.getenv("EMAIL_RECIPIENT")
    if not recipient:
        print("ERROR: EMAIL_RECIPIENT not set!")
        return

    try:
        send_email(subject, body, recipient)
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)

if __name__ == "__main__":
    main()
    # keep alive only if deployed as Web Service
    import time
    while True:
        time.sleep(60)
