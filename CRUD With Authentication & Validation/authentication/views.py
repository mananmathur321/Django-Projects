from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import signupform
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
    if request.method == "POST":
        x=signupform(request.POST)
        if x.is_valid():
            unm=x.cleaned_data['username']
            upwd=x.cleaned_data['password2']
            ueml=x.cleaned_data['email']
            fnm=x.cleaned_data['first_name']
            lnm=x.cleaned_data['last_name']
            m = User.objects.create_user(username=unm,email=ueml,password=upwd,first_name=fnm,last_name=lnm,is_staff=True)  
            m.save()
            return HttpResponseRedirect('/signin/')
    else:        
        x=signupform()
    return render(request,'authentication/signup.html',{'form':x})

def option(request):
    return render(request,'authentication/options.html')

def signin(request):
    if request.method == 'POST':
        y = AuthenticationForm(request=request, data=request.POST)
        if y.is_valid():
            unm=y.cleaned_data['username']
            upwd=y.cleaned_data['password']
            user=authenticate(username=unm, password=upwd)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/view/')
            
    else:
        y=AuthenticationForm
    return render(request,'authentication/signin.html',{'form':y})


def logoutpage(request):
    logout(request)
    return HttpResponseRedirect('/')