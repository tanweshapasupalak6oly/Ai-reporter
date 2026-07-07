"""Email the weekly AI report."""

import os
import smtplib
from email.message import EmailMessage


def send_report(subject: str, body: str, report_file: str):
    msg = EmailMessage()

    msg["Subject"] = subject
    msg["From"] = os.environ["EMAIL_ADDRESS"]
    msg["To"] = os.environ["EMAIL_TO"]

    # Email body
    msg.set_content(
        f"""{body}

The weekly AI report has been generated.

Report file: {report_file}
"""
    )

    # Attach the report
    with open(report_file, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="text",
            subtype="markdown",
            filename=report_file,
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(
            os.environ["EMAIL_ADDRESS"],
            os.environ["EMAIL_APP_PASSWORD"],
        )
        smtp.send_message(msg)
