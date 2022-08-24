from django.shortcuts import render,HttpResponseRedirect
from .forms import PersonForm
from .models import Person
from django.contrib.auth import authenticate
from string import capwords
def add(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            pf=PersonForm(request.POST)
            if pf.is_valid():
                pf.save()
        else:
            pf=PersonForm()
        per=Person.objects.all()
        nm=str(request.user).capitalize
        return render(request,'core/view.html',{'pers':pf, 'per':per,'name':nm})
    else:
        return HttpResponseRedirect('/')


def deletedata(request,pno):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            x=Person.objects.get(pk=pno)
            x.delete()
            return HttpResponseRedirect('/view/')
    else:
        return HttpResponseRedirect('/')

def updatew(request,pno):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            x=Person.objects.get(pk=pno)
            pf=PersonForm(request.POST, instance=x)
            if pf.is_valid():
                pf.save()
                return HttpResponseRedirect('/view/')
        else:
            x=Person.objects.get(pk=pno)
            pf=PersonForm(instance=x)  
            return render(request,'core/update.html', {'form':pf})
    else:
        return HttpResponseRedirect('/')