from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
import random

# Create your views here.
def semail(request):
    return render(request, "email.html")
def otp(request):
    username=request.POST["name"]
    email=request.POST["email"]
    subject = 'otp'
    n=random.random()
    n=n*10000
    n=int(n)
    n=str(n)
    message = n
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ustadkittu525@gmail.com','sanusaurav94@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return render(request, "veryfi.html", {'otp':message})
def veryfi(request):
    otp=request.POST["otp"]
    otp1=request.POST["otp1"]
    if otp==otp1:
        return render(request, "update.html")
    else:
        return render(request, "email.html")
        
    