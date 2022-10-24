#!/usr/bin/env python3

import cgi
import cgitb
import smtplib
from email.message import EmailMessage
from dotenv import dotenv_values

env = dotenv_values(".env")
cgitb.enable()

form = cgi.FieldStorage()

if "from" not in form:
    print("Content-type: */*")
    print("Status: 400 Bad Request")
    print()

    print("Précisez un expéditeur")
    exit(1)
if "content" not in form:
    print("Content-type: */*")
    print("Status: 400 Bad Request")

    print()

    print("Le contenu du mail ne peut pas être vide")
    exit(1)

# Preparing message
msg = EmailMessage()
msg["Subject"] = "Mail du portfolio" if "subject" not in form else form.getvalue("subject")
msg["To"] = "bastian.somon@gmail.com" if "to" not in form else form.getvalue("to")
msg["From"] = form.getvalue("from")
content = form.getvalue("content")
from_ = form.getvalue("from")
msg.set_content(f"Message du portfolio:\nDe: {from_}\n{30 * '-'}\n\n{content}")

# Setting up the SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login(env.get("SMTP_USERNAME"), env.get("SMTP_PASSWORD"))
server.send_message(msg)

print("Content-type: */*")
print("Status: 204 No content")
print()
