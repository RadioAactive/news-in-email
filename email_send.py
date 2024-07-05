import smtplib , ssl
from os import getenv

def email_send(message):
    email = getenv("GMAIL")
    password = getenv("GMAILpass")
    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as script:
        script.login(email,password)
        script.sendmail(email,email, message)