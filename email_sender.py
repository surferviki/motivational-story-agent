def send_email(subject, body, to):
    if not GMAIL_USER or not GMAIL_APP_PASSWORD:
        print("ERROR: Gmail credentials not set!")
        return

    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = GMAIL_USER
        msg["To"] = to

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            smtp.send_message(msg)
            print(f"📩 Email sent to {to}")

    except Exception as e:
        print("Failed to send email:", e)
