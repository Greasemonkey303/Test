#! /bin/python3

import smtplib
import ssl
from email.message import EmailMessage

from django.dispatch import receiver
import h11

subject = "Email From Python"
body = "this is a test email from Python!"
sender_email = "zachsfreed@gmail.com"
receiver_email = "zachsfreed@gmail.com"
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")
