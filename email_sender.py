import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")

def send_email(subject, body):
    if not SENDGRID_API_KEY:
        print("❌ SENDGRID_API_KEY not set!")
        return

    if not EMAIL_RECIPIENT:
        print("❌ EMAIL_RECIPIENT not set!")
        return

    message = Mail(
        from_email="no-reply@yourdomain.com",  # can be any verified sender
        to_emails=EMAIL_RECIPIENT,
        subject=subject,
        html_content=body
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"📩 Email sent! Status Code: {response.status_code}")
    except Exception as e:
        print("❌ Failed to send email:", e)
