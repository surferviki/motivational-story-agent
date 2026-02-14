import os
from story_generator import generate_story
from email_sender import send_email

def main():
    story = generate_story()
    print("Generated Story:\n", story)

    subject = "🌟 Your Weekly Motivational Story!"
    body = story
    recipient = os.getenv("EMAIL_RECIPIENT")

    send_email(subject, body, recipient)

if __name__ == "__main__":
    main()
