from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from django.contrib.auth.models import User
from datetime import datetime 
import time
from django.contrib import admin
from django.core.validators import validate_email
from django.conf import settings

def mail(receiver_mail,name):
    subject = "MORNING REGARDS"
    from_email = settings.EMAIL_HOST_USER
    # mail_message = """Dear {},\nGOOD MORNING!! HAVE A NICE DAY""".format(name)
    d = {}
    for i in range(len(name)):
        d[receiver_mail[i]] = name[i]
    #to_email = ['shubhimay18@gmail.com', 'qwerty@gmail.com']  # list of people you're sending the email to
    successful_recipients = []
    unsuccessful_recipients = []
    yes=[]
    no=[]
    for email in d:
        try:
            print("TRY*****************************************")
            report = send_mail(
                subject=subject,
                from_email=from_email,
                recipient_list = [email],
                message="""Dear {},\nGOOD MORNING!! HAVE A NICE DAY AHEAD""".format(d[email]),
                fail_silently=False)
            validate_email(email)
            yes.append(email)
            print("yessssssss")
        except Exception as e: 
            print(e)
            print("EXCEPT**********************************************")
            no.append(email)
            print("NOOOOOOOo")
            report = 0
        print(datetime.today())
        print(report, type(report))
        if report:
            successful_recipients.append(email)
            print("mail successfully sent !!")
        else:
            unsuccessful_recipients.append(email)
            print("mail not sent !!")
    print("YES", yes)
    print("NO", no)
    return successful_recipients, unsuccessful_recipients

def mass_mail(name):
    subject = "GOOD MORNING"
    from_email = "SHUBHI"
    message = """Dear {},\nGOOD MORNING!! HAVE A NICE DAY""".format(name)
    recipient_list=['shubhimay18@gmail.com', 'er.shubhiagarwal@gmail.com'],

    messages = [(subject , message, from_email, [r]) for r in recipient_list]

    send_mass_mail(messages)

