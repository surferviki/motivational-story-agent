import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")  # Must be a valid email

# Use a verified sender in SendGrid
VERIFIED_SENDER = "vignesh.instrumentation@gmail.com"

def send_email(subject, body):
    if not SENDGRID_API_KEY:
        print("❌ SENDGRID_API_KEY not set!")
        return
    if not EMAIL_RECIPIENT:
        print("❌ EMAIL_RECIPIENT not set!")
        return
    if not VERIFIED_SENDER:
        print("❌ VERIFIED_SENDER not set!")
        return
    if not body:
        print("❌ Email body is empty!")
        return

    try:
        message = Mail(
            from_email=VERIFIED_SENDER,
            to_emails=EMAIL_RECIPIENT,
            subject=subject,
            html_content=str(body)  # ensure string
        )
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"📩 Email sent to {EMAIL_RECIPIENT} | Status Code: {response.status_code}")
    except Exception as e:
        print("❌ Failed to send email:", e)
