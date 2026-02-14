import os
from story_generator import generate_story
from email_sender import send_email

def main():
    story = generate_story()
    if not story:
        print("❌ No story generated. Exiting.")
        return

    subject = "🌟 Your Weekly Motivational Story!"
    body = story
    recipient = os.getenv("EMAIL_RECIPIENT")
    if not recipient:
        print("❌ EMAIL_RECIPIENT not set. Exiting.")
        return

    send_email(subject, body)

if __name__ == "__main__":
    main()
