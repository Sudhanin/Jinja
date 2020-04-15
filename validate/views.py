from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
import re
def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password1']
        password1=request.POST['password2']
        if password==password1:

            if User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect('register')
            elif  re.match('[A-Za-z0-9]/w{8,20}$]',password):
                messages.info(request,"Pasword should contain atleast 8 characters"+password)
                return redirect('register')
            else:
                user=User.objects.create_user(username=email,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("user created")
                return redirect('login')
        else:    
           messages.info(request,"password wrong")
           return redirect('register')
        return redirect('/')
    else:
      return render(request,"register.html")
def login(request):
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"home.html",{'dic':username})
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,"login.html")
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect("login")
