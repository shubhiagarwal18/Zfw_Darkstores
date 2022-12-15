from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from core_app.models import savedata
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from core_app.send_mail import mail
from django.contrib.auth import get_user_model
from django.contrib import admin
import time
from datetime import datetime
from threading import Timer
import logging
from core.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.template.loader import get_template
import schedule
import time
from django.http import HttpResponse
from PIL import Image
from django.urls import reverse
from django.utils.html import strip_tags

logger = logging.getLogger('django')

def image_load(request):
    print("\nImage Loaded\n")
    red = Image.new('RGB', (1, 1))
    response = HttpResponse(content_type="image/png")
    red.save(response, "PNG")
    return response

def home(request):
    logger.info("Logger information")
    logger.critical("Logger critical")
    logger.warning("Logger warning")
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

    subject = "Testing Purpose"
    from_email = "anubhav.april01@gmail.com"
    # html_content = get_template('email.html').render({'name': 'name'})
    # msg = EmailMessage(subject, html_content, from_email, to=['shubhimay18@gmail.com'])
    # msg.content_subtype ='html'
    # msg.send()
    # print("msg send")

    # using template to generate the email content
    template = get_template("email.html")
    context_data = dict()

    # pass the variable image_url to template
    # image_load is the URL name. see below
    context_data["image_url"] = request.build_absolute_uri(reverse("image_load"))
    html_text = get_template('email.html').render(context_data)
    print(context_data)
    print(html_text)
    plain_text = strip_tags(html_text)
    print(plain_text)
    msg = EmailMessage(subject, html_text, from_email, to=['shubhimay18@gmail.com'])
    msg.content_subtype ='html'
    msg.send()
    print("mail sent with image")

    return render(request, 'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        #print(request.POST)
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username = username):
            msg = "Username already exist!! Please try some other username."
            messages.error(request, "Username already exist!! Please try some other username.")
            return redirect('home')

        if User.objects.filter(email = email):
            msg = "Username already exist!! Please try some other username."
            messages.error(request, "Username already exist!! Please try some other username.")
            return redirect('home')

        savedata(username = username, password = password, email = email).save()
        User.objects.create_user(username, email, password).save()

        messages.success(request, "You have successfully registered !!")
        msg = "You have successfully registered !!"
    return redirect('home')
    #return render(request, "index.html", {"msg": msg})

def signin(request):
    if request.method == 'POST':
        print(request.POST)
        usr = request.POST.get("user-name")
        pwd = request.POST.get("pass-word")
        user = authenticate(username= usr, password= pwd)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, "Bad Credentials !!")
            return redirect('home')
         
    return render(request, 'newpage.html')

def signout(request):
    logout(request)
    messages.success(request, "You are logged out !!")
    return redirect('home')

def sending_mail_to_all_users():
    users1 = User.objects.values_list('email')
    email = [email[0] for email in users1]
    name1 = User.objects.values_list('username')
    username = [name[0] for name in name1]
    print(username)
    while True:
        successful_recipients, unsuccessful_recipients = mail(email, username)   
        time.sleep(60*3)
        print(successful_recipients)
        print(unsuccessful_recipients)     
        print("mail done")

def job():
    print("I'm working...")
    sending_mail_to_all_users()

#schedule.every(2).minutes.do(job)
# schedule.every().hour.do(job)
schedule.every().day.at("12:46").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


# x=datetime.today()
# y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
# delta_t=y-x
# print("******************")
# print(delte_t)
# secs=delta_t.seconds+1

# def hello_world():
#     print("hello world")
#     #...

# t = Timer(secs, hello_world)
# t.start()