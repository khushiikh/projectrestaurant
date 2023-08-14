from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request,'index.html',{})

def formContact(request):
    name1=request.POST.get('name','default')
    print(name1)

    mail1=request.POST.get('mail','default')
    print(mail1)

    phn1=request.POST.get('phn','default')
    phn1=int(phn1)
    print(phn1)

    message1=request.POST.get('message','default')
    print(message1)

    c=Contact(Name=name1,Email=mail1,Phone=phn1,Message=message1)
    c.save()


    return HttpResponse("thank you for visiting us")

def order(request):
    return render(request,'order.html',{})

def orderNow(request):
    Name=request.POST.get('name','default')
    Add=request.POST.get('address','default')
    Item=request.POST.get('item','default')
    Qty=request.POST.get('qty','default')
    print(Name,Add,Item,Qty)
    subject = 'Order'
    message = f'Name : {Name} \n Address : {Add} \n Item : {Item} \n Qty : {Qty}.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['www.khushi0909@gmail.com', ]
    send_mail( subject, message, email_from, recipient_list )

    return HttpResponse("<h1 style='color:red'>Thanks for Your Order. Enjoy Your Day & <a href='/'>Click Here</a> For Home Page.</h1>")
