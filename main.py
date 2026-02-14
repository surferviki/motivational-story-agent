import os
from story_generator import generate_story
from email_sender import send_email


def main():
    story = generate_story()
    print("✅ Story generated successfully")

    subject = "🌟 Your Weekly Motivational Story!"
    recipient = os.getenv("EMAIL_RECIPIENT")

    if not recipient:
        raise ValueError("EMAIL_RECIPIENT is not set")

    send_email(subject, story, recipient)


if __name__ == "__main__":
    main()
