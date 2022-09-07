from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import signupform,otpview
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
import random
import json,requests

# Create your views here.

def option(request):
    return render(request,'authentication/options.html')
    

def signup(request):
    global otp,unm,upwd,ueml,fnm,lnm
    otp=random.randint(1000,9999)
    if request.method == "POST":
        x=signupform(request.POST)
        if x.is_valid():
            unm=x.cleaned_data['username']
            upwd=x.cleaned_data['password2']
            ueml=x.cleaned_data['email']
            fnm=x.cleaned_data['first_name']
            lnm=x.cleaned_data['last_name']
            email = EmailMessage('Verification OTP',f"Your OTP Is {otp}",to=[ueml])
            email.send()
            return HttpResponseRedirect('/otp/')
    else:        
        x=signupform() 
    return render(request,'authentication/signup.html',{'form':x})



def otpverify(request):
    if request.method=='POST':
        form=otpview(data=request.POST)
        if form.is_valid:
            print(form)
            print(form.cleaned_data['otp'])
            fotp=form.cleaned_data['otp']
            if fotp==otp:
                instnc = User.objects.create_user(username=unm,email=ueml,password=upwd,first_name=fnm,last_name=lnm,is_staff=True)  
                instnc.save()
                print("User Created Successfully")
                return HttpResponseRedirect('/signin/')
            else:
                msg="Wrong OTP"
                return render(request,'authentication/otp.html',{'form':form,'ms':msg})
    else:
        form=otpview()
    return render(request,'authentication/otp.html',{'form':form})


def signin(request):
    global accesstoken,refreshtoken
    if request.method == 'POST':
        y = AuthenticationForm(request=request, data=request.POST)
        if y.is_valid():
            unm=y.cleaned_data['username']
            upwd=y.cleaned_data['password']            
            gettoken=requests.post('http://127.0.0.1:8000/gettoken/',{'username':unm,'password':upwd}).text
            tokendata=json.loads(gettoken)
            accesstoken=tokendata["access"]
            refreshtoken=tokendata["refresh"]
            print(accesstoken)
            
            verify=requests.post('http://127.0.0.1:8000/verifytoken/',{'token':accesstoken}).text
            veridata=json.loads(verify)
            if accesstoken==verify or len(veridata)==0:
                user=authenticate(username=unm, password=upwd)
                if user is not None:
                    login(request,user)
                    response = HttpResponseRedirect('/view/')
                    response.set_cookie(key='jwt', value=accesstoken, httponly=True)
                    return response
            else:
                result=requests.post('http://127.0.0.1:8000/refreshtoken/',{'refresh':refreshtoken}).text
                data=json.loads(result)
                accesstoken=data["access"]
                requests.post('http://127.0.0.1:8000/verifytoken/',{'token':accesstoken}).text
                user=authenticate(username=unm, password=upwd)
                login(request,user)
                response = HttpResponseRedirect('/view/')
                response.set_cookie(key='jwt', value=accesstoken, httponly=True)
                return response
    else:
        y=AuthenticationForm
    return render(request,'authentication/signin.html',{'form':y})


def logoutpage(request):
    logout(request)
    response = HttpResponseRedirect('/')
    response.delete_cookie('jwt')
    return response