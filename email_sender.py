import os
import smtplib
from email.message import EmailMessage
import socket

GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

def send_email(subject, body, to):
    if not GMAIL_USER or not GMAIL_APP_PASSWORD:
        print("❌ Gmail credentials missing!")
        return

    if not to:
        print("❌ Recipient email missing!")
        return

    try:
        socket.setdefaulttimeout(30)  # Avoid hanging
        print("Connecting to Gmail SMTP...")
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = GMAIL_USER
        msg["To"] = to

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30) as smtp:
            smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            print("✅ Logged in to Gmail")
            smtp.send_message(msg)
            print(f"📩 Email sent to {to}")

    except Exception as e:
        print("❌ Failed to send email:", e)
