
from django.shortcuts import render,redirect

from django.contrib.auth.models import User,auth

a="java"
n="testing"

def index(request):
 return render(request,"index.html")

def samp(request):
    return render(request,"test.html",{'l':a,'m':n})

def login(request):
    return render(request,"login.html",)

def register(request):
    return render(request,"register.html") 

def logincheck(request):
    name=request.GET["uname"]
    pas=request.GET["pname"]
    user=auth.authenticate(username=name,password=pas)
    if user is not None:    
        auth.login(request,user)
        return redirect("/")
    else:
        return redirect ("/login")
def registercheck(request):
    username=request.GET["username"]
    firstname=request.GET["fname"]
    lastname=request.GET["lname"]
    email=request.GET["mail"]
    password=request.GET["pas"]
    repassword=request.GET["repas"]
    uchk=User.objects.filter(username=username)
    echk=User.objects.filter(email=email)
    if uchk :
        na="username is already taken"
        return render(request,"test.html",{"na":na})
    elif echk:
        na="email is already taken"
        return render(request,"test.html",{"na":na})
    elif password!=repassword:
        na="invalid password"
        return render(request,"test.html",{"na":na})
    else:
        user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        user.save();
        return redirect("/")
# Create your views here

