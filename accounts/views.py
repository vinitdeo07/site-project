from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def registerPage(request):
    form = RegisterForm()
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request,"Account created for user" + user)
            return redirect("/login")
        else:
            print("error in form saving :", form.errors)

    context={'form':form}
    return render(request,"accounts/register.html",context)

def loginPage(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Username or Password is incorrect")

    context={}
    return render(request,"accounts/login.html",context)

def logoutPage(request):
    logout(request)
    return redirect("/login")