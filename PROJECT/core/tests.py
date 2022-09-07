import imp
from django.test import TestCase,SimpleTestCase,Client,TransactionTestCase
from .models import Student
from rest_framework.test import APITestCase
from django.urls import reverse,resolve
from .views import adddata,deletedata,updatew
from .forms import StudentForm
# Create your tests here.

class StudentTestCase(TestCase):
    def setup(self):
        print("Testing 1 Setup Activity Of Core App")
        Student.objects.create(id=1,name="Kabir",mailid="dohakinghu@gmail.com",phoneno=7012018613)

        
    def test_student_info(self):
        instnce=Student(id=1,name="Kabir",mailid="dohakinghu@gmail.com",phoneno=7012018613)
        instnce.save()
        print("Testing 1 Student Info Case Of Core App")
        qs=Student.objects.all()
        self.assertEqual(qs.count(),1)
        

class ApiAPITestCase(APITestCase):
    global URL
    URL='http://127.0.0.1:8000/stu/'
    
    print("Testing 7 API Conditions Of Core App")
    
    def setup(self):
        print("API Setup Activity")
        instnce=Student(id=1,name="Kabir",mailid="dohaking@gmail.com",phoneno=7012018613)
        instnce.save()
    def test_get_method(self):
        response=self.client.get(URL)
        self.assertEqual(response.status_code,200)
        qs=Student.objects.filter(id=8)
        self.assertEqual(qs.count(),0)
        
        
    def test_post_method(self):
        data={
            'id':3,
            'name':"Tulsi",
            'mailid':"dohokaraja@gmail.com",
            'phoneno':7012018614
            }
        response=self.client.post(URL,data,format='json')
        self.assertEqual(response.status_code,201)
        
    
    def test_post_method_fail(self):
        data={
        'name':"JSON",
        'mailid':"c@s.com",
        'phoneno':7012018613
        }
        response=self.client.post(URL,data,format='json')
        self.assertEqual(response.status_code,400)
        
        
    def test_delete_method(self):
        URL='http://127.0.0.1:8000/stu/5'
        self.client.delete(URL)
        qs=Student.objects.filter(id=5)
        self.assertEqual(qs.count(),0)
        
        
    def test_put_method(self):
        instnce=Student(id=1,name="Kabir",mailid="dohaking@gmail.com",phoneno=7012018613)
        instnce.save()
        data={
            'id':1,
            'name':"JSON",
            'mailid':"c@s.com",
            'phoneno':7012018613
        }
        URL='http://127.0.0.1:8000/stu'
        response=self.client.put(URL,data,format='json')
        self.assertEqual(response.status_code,301)
        
        
    def test_patch_method(self):
        instnce=Student(id=1,name="Baba",mailid="babadon@gmail.com",phoneno=7012018613)
        instnce.save()
        data={
            'id':1,
            'name':"Baba Don",
        }
        URL='http://127.0.0.1:8000/stu'
        response=self.client.patch(URL,data,format='json')
        self.assertEqual(response.status_code,301)
        
     
class URLTest(SimpleTestCase):
    
    print("Testing 3 URLs Of Core App")
    
    def test_home_test(self):
        url=reverse('home')
        self.assertEqual(resolve(url).func,adddata)
        
    def test_deleted_test(self):
        url=reverse('deleted', args=['1'])
        self.assertEqual(resolve(url).func,deletedata)
        
    def test_updatew_test(self):
        url=reverse('updwin',args=['1'])
        self.assertEqual(resolve(url).func,updatew)
    
        
    
class ViewFunctionsTest(TestCase):
    
    print("Testing 3 View Function Of Core App")
       
    def test_adddata(self):
        client=Client()
        response=client.get(reverse('home'))
        self.assertRedirects(response, '/')
        
    def test_deletedata(self):
        client=Client()
        response=client.get(reverse('deleted',args=['1']))
        self.assertRedirects(response, '/')
        
    def test_updatew(self):
        client=Client()
        response=client.get(reverse('updwin',args=['1']))
        self.assertRedirects(response, '/')
        
    
class FormTest(TransactionTestCase):
    
    print("Testing 2 Cases Of Form Of Core App")
    
    def test_StudentForm_valid(self):
        fdata={'id':1,'name':'Baba','mailid':'babadon@gmail.com','phoneno':7012018613}
        form=StudentForm(data=fdata)
        self.assertTrue(form.is_valid())
        
    def test_StudentForm_invalid(self):
        fdata={}
        form=StudentForm(data=fdata)
        self.assertFalse(form.is_valid())