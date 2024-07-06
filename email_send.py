import smtplib , ssl
from os import getenv

def email_send(message):

    # My contents
    host_email = getenv("GMAIL")
    password = getenv("GMAILpass")
    host = "smtp.gmail.com"
    port = 465

    # Enter email whom you want to send contents in this list
    elist = [email]

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as script:
        script.login(email,password)
        for email in elist:
            script.sendmail(host_email, elist, message)