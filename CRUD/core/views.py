from django.shortcuts import render,HttpResponseRedirect
from .forms import PersonForm
from .models import Person
def add(request):
    if request.method == 'POST':
        pf=PersonForm(request.POST)
        if pf.is_valid():
            pf.save()
    
    pf=PersonForm()
    per=Person.objects.all()
    return render(request,'core/view.html',{'pers':pf, 'per':per})


def deletedata(request,pno):
    if request.method == 'POST':
        x=Person.objects.get(pk=pno)
        x.delete()
    pf=PersonForm()
    return HttpResponseRedirect('/')

def updatew(request,pno):
    if request.method == 'POST':
        x=Person.objects.get(pk=pno)
        pf=PersonForm(request.POST, instance=x)
        if pf.is_valid():
            pf.save()
    else:
        x=Person.objects.get(pk=pno)
        pf=PersonForm(instance=x)  
    return render(request,'core/update.html', {'form':pf})
