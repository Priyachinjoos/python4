from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login (request):
    if request.method=='POST':
        username=request.POST['username']
        pswd=request.POST['password']
        user=auth.authenticate(username=username,password=pswd)

        if user is not None:
            auth.login(request,user)
            return redirect ('/')

        else:
            messages.info(request,"invalid credentials")
            return redirect ('login')
    return render(request,'login.html')

def register (request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        pswd=request.POST['password']
        pswd2=request.POST['password2']
        if pswd==pswd2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            user=User.objects.create_user(username=username,password=pswd,first_name=fname,last_name=lname,email=email)

            user.save();
            return redirect ('login')


        else:
            print("password not matching")
            return redirect('register')
        return redirect('/')

    return render (request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
