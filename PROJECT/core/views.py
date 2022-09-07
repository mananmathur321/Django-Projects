from django.shortcuts import HttpResponseRedirect,render
from .models import Student
from .serializers import StudentSerializer
from .forms import StudentForm
from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
import requests,json
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from authentication import views


URL='http://127.0.0.1:8000/stu/'


def adddata(request):
    if request.user.is_authenticated and request.user.is_staff:
        tokensin = request.COOKIES.get('jwt')
        verify=requests.post('http://127.0.0.1:8000/verifytoken/',{'token':tokensin}).text
        verifydata=json.loads(verify)
        if tokensin==verify or len(verifydata)==0:
            if request.method == 'POST':
                pf=StudentForm(request.POST)
                if pf.is_valid():
                    fdata = pf.cleaned_data
                    requests.post(url=URL,data=fdata)
            else:
                pf=StudentForm()
            response = requests.get(url=URL)
            jdata = response.json()
            nm=str(request.user).capitalize
            return render(request,'core/view.html',{'pers':pf, 'per':jdata,'name':nm})
    else:
        return HttpResponseRedirect('/')


def deletedata(request,id):
    if request.user.is_authenticated and request.user.is_staff:
        print(request)
        data={'id':id}
        requests.delete(url=URL,data=data)
        return HttpResponseRedirect('/view/')
    else:
        return HttpResponseRedirect('/')
    

def updatew(request,id):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            instnc=Student.objects.get(pk=id)
            pf=StudentForm(request.POST, instance=instnc)
            if pf.is_valid():
                fdata = pf.cleaned_data
                requests.put(url=URL,data=fdata)
                return HttpResponseRedirect('/view/')
        else:
            instnc=Student.objects.get(pk=id)
            pf=StudentForm(instance=instnc)  
            return render(request,'core/update.html', {'form':pf})
    else:
        return HttpResponseRedirect('/')



@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def api(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Student Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        data = request.data.get('id')
        student = Student.objects.get(id=data)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Student Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        data = request.data.get('id')
        student = Student.objects.get(id=data)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Student Updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        data = request.data.get('id')
        student = Student.objects.get(id=data)
        student.delete()
        return Response({'msg': 'Student Deleted'})