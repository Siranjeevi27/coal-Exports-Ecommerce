from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
import random
# Create your views here.
#otp=random.randint(1000,9999)
#otp=random.randint(1000,9999)
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def products(request):
    allcoal = Coal.objects.all()
    return render(request,'products.html', {'coals':allcoal})
def logout(request):
    auth.logout(request)
    return redirect('/')
   # return render(request,'logout.html')
def login(request):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        userotp=request.POST['otp']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            #print(f"login with {otp}")
            return redirect('/') 
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
def sighup(request):
    if(request.method=='POST'):
        first_name=request.POST['first_name'],
        last_name=request.POST.get('last_name'),
        email=request.POST['email'],
        username=request.POST['username'],
        password1=request.POST['password1'],
        password2=request.POST['password2'],
        #otp=None
        print(username, password1)
        if(password1==password2):
            if(User.objects.filter(username=username[0]).exists()):
                print("username exists")
                messages.info(request,'Username exits')
                return redirect('sighup')
            elif (User.objects.filter(email=email[0]).exists()):
                print("email exits")
                messages.info(request,'Email exits')
                return redirect('sighup')
            else:
                otp=random.randint(1000,9999)
                user=User.objects.create_user(username=username[0], password=password1[0],email=email[0],first_name=first_name[0],last_name=last_name[0])
                user.save()
                print(otp)
                print('user created')
                Subject="Cherraan Services welcomes you"
                message=f"Hello welcome to Cherraan Services Your opt for signup is {otp}"
                se_mail='cherraan123@gmail.com'
                re_mail=email
                send_mail(Subject,message,se_mail,re_mail)
                print(f"mail is sent successfully with otp {otp}",)
                return redirect('login')  
        else:
            messages.info(request,'Password not matching')
            print("password not matching")
            return redirect('sighup')

        
    else:  
        return render(request,'sighup.html')

