from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from django.contrib.auth.models import User
from datetime import datetime 
import time

def mail(receiver_mail,name):
    subject = "MORNING REGARDS"
    from_email = "AUTOMATED EMAIL"
    # mail_message = """Dear {},\nGOOD MORNING!! HAVE A NICE DAY""".format(name)
    d = {}
    for i in range(len(name)):
        d[receiver_mail[i]] = name[i]
    #to_email = ['shubhimay18@gmail.com', 'qwerty@gmail.com']  # list of people you're sending the email to
    successful_recipients = []
    unsuccessful_recipients = []
    for email in d:
        report = send_mail(subject=subject, from_email=from_email, recipient_list=['user@hotmail.fr'], message="""Dear {},\nGOOD MORNING!! HAVE A NICE DAY AHEAD""".format(d[email]), fail_silently=False)
        print(datetime.today())
        if report:
            successful_recipients.append(email)
            print("mail successfully sent !!")
        else:
            unsuccessful_recipients.append(email)
            print("mail not sent !!")
    return successful_recipients, unsuccessful_recipients

def mass_mail(name):
    subject = "GOOD MORNING"
    from_email = "SHUBHI"
    message = """Dear {},\nGOOD MORNING!! HAVE A NICE DAY""".format(name)
    recipient_list=['shubhimay18@gmail.com', 'er.shubhiagarwal@gmail.com'],

    messages = [(subject , message, from_email, [r]) for r in recipient_list]

    send_mass_mail(messages)

