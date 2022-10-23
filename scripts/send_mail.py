import cgi
import cgitb
# import smtplib
# from env import dotenv_values
# from email.message import EmailMessage
#
# env = dotenv_values(".env")

cgitb.enable()

# form = cgi.FieldStorage()
#
# if "from" not in form:
#     print("Content-type: text/html")
#     print("Status: 400 Bad Request")
#     print()
#
#     print("Aucun expéditeur n'a été spécifié.")
#
#     exit(1)
#
# if "content" not in form:
#     print("Content-type: text/html")
#     print("Status: 400 Bad Request")
#     print()
#
#     print("Aucun contenu")
#
#     exit(1)
#
#
# # Send mail
# msg = EmailMessage()
# msg.set_content(form.getvalue("content"))
#
# subject = "Mail du portfolio" if "subject" not in form else form.getvalue("subject")
# msg['Subject'] = subject
# msg['From'] = form.getvalue("from")
# msg['To'] = "bastian.somon@gmail.com"
#
# # Send the message via gmail SMTP server.
# s = smtplib.SMTP('smtp.gmail.com')
# s.ehlo()
# s.starttls()
# s.login(env.get("SMTP_USERNAME"), env.get("SMTP_PASSWORD"))
# s.send_message(msg)
# s.quit()

print("Content-type: */*")
print("Status: 200 OK")
print()

print("Ok")
