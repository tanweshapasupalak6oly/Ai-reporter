"""Email the weekly AI report."""

import smtplib
from email.message import EmailMessage
import os


def send_report(subject: str, body: str, google_doc_url: str):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = os.environ['EMAIL_ADDRESS']
    msg['To'] = os.environ['EMAIL_TO']

    msg.set_content(f"{body}\n\nGoogle Docs Report:\n{google_doc_url}")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_APP_PASSWORD'])
        smtp.send_message(msg)
