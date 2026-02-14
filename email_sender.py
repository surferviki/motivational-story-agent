import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

def send_email(subject, body, to):
    if not SENDGRID_API_KEY:
        print("❌ SENDGRID_API_KEY not set!")
        return

    if not to:
        print("❌ Recipient email not set!")
        return

    message = Mail(
        from_email="no-reply@yourdomain.com",  # Can be any verified sender in SendGrid free tier
        to_emails=to,
        subject=subject,
        html_content=body
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"📩 Email sent to {to} | Status Code: {response.status_code}")
    except Exception as e:
        print("❌ Failed to send email:", e)
