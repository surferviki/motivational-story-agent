import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Environment variables (set these in Railway)
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")


def send_email(subject, body, to):
    try:
        if not SENDGRID_API_KEY:
            raise ValueError("SENDGRID_API_KEY is not set")
        if not FROM_EMAIL:
            raise ValueError("FROM_EMAIL is not set")
        if not to:
            raise ValueError("Recipient email is missing")

        # Convert story into clean HTML paragraphs
        paragraphs = body.split("\n")
        formatted_story = "".join(
            f"<p style='margin-bottom:18px;'>{p}</p>"
            for p in paragraphs if p.strip()
        )

        # Startup-style HTML email template
        html_content = f"""
        <html>
        <body style="margin:0; padding:0; background-color:#f2f4f8; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;">

            <table width="100%" cellpadding="0" cellspacing="0">
                <tr>
                    <td align="center">

                        <table width="600" cellpadding="0" cellspacing="0"
                               style="background:#ffffff; margin:40px 0; border-radius:16px; padding:40px; box-shadow:0 10px 30px rgba(0,0,0,0.08);">

                            <!-- Header -->
                            <tr>
                                <td align="center">
                                    <h2 style="margin:0; color:#6C63FF; font-size:13px; letter-spacing:2px;">
                                        AI POWERED WEEKLY SERIES
                                    </h2>
                                    <h1 style="margin:10px 0 20px 0; color:#111827; font-size:28px;">
                                        🌟 Your Weekly Motivation
                                    </h1>
                                    <hr style="border:none; border-top:1px solid #eee;">
                                </td>
                            </tr>

                            <!-- Story Content -->
                            <tr>
                                <td style="font-size:16px; line-height:1.8; color:#374151; padding-top:20px;">
                                    {formatted_story}
                                </td>
                            </tr>

                            <!-- CTA Button -->
                            <tr>
                                <td align="center" style="padding:30px 0;">
                                    <a href="#"
                                       style="background:#6C63FF;
                                              color:white;
                                              padding:14px 28px;
                                              text-decoration:none;
                                              border-radius:8px;
                                              font-weight:600;
                                              display:inline-block;">
                                        Keep Growing 🚀
                                    </a>
                                </td>
                            </tr>

                            <!-- Footer -->
                            <tr>
                                <td align="center" style="font-size:13px; color:#9CA3AF; padding-top:20px;">
                                    Sent automatically by your AI Story Engine<br>
                                    Built with OpenRouter • SendGrid • Railway
                                </td>
                            </tr>

                        </table>

                    </td>
                </tr>
            </table>

        </body>
        </html>
        """

        # Create SendGrid message
        message = Mail(
            from_email=FROM_EMAIL,
            to_emails=to,
            subject=subject,
            plain_text_content=body,
            html_content=html_content
        )

        # Send email
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)

        print(f"📩 Email sent to {to} | Status Code: {response.status_code}")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")
