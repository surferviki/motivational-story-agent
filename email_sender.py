import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")

def send_email(subject, body, to):
    try:
        # Convert plain story into HTML paragraphs
        formatted_story = body.replace("\n", "<br><br>")

        html_content = f"""
        <html>
        <body style="margin:0; padding:0; background-color:#f4f4f4; font-family: Arial, sans-serif;">
            <table align="center" width="600" cellpadding="0" cellspacing="0" 
                   style="background-color:#ffffff; padding:30px; border-radius:10px;">
                <tr>
                    <td align="center">
                        <h1 style="color:#2c3e50;">🌟 Weekly Motivation</h1>
                        <hr style="border:none; border-top:1px solid #eee; margin:20px 0;">
                        <p style="font-size:16px; line-height:1.8; color:#333;">
                            {formatted_story}
                        </p>
                        <br>
                        <p style="font-size:14px; color:#888;">
                            Sent automatically by your AI Story Bot 🚀
                        </p>
                    </td>
                </tr>
            </table>
        </body>
        </html>
        """

        message = Mail(
            from_email=FROM_EMAIL,
            to_emails=to,
            subject=subject,
            html_content=html_content,
            plain_text_content=body
        )

        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)

        print(f"📩 Email sent to {to} | Status Code: {response.status_code}")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")
