from django.test import TestCase,SimpleTestCase,Client
from django.urls import reverse,resolve
from .views import signin,signup,otpverify,option,logoutpage


# Create your tests here.
# 'otp','signup','signin','option','logout'
     
class URLTest(SimpleTestCase):
    print("Testing 5 URLS Of Authentication App")
    
    def test_otp_test(self):
        url=reverse('otp')
        self.assertEqual(resolve(url).func,otpverify)
        
    def test_signup_test(self):
        url=reverse('signup')
        self.assertEqual(resolve(url).func,signup)
        
    def test_signin_test(self):
        url=reverse('signin')
        self.assertEqual(resolve(url).func,signin)
        
    def test_blank_test(self):
        url=reverse('option')
        self.assertEqual(resolve(url).func,option)
        
    def test_logout_test(self):
        url=reverse('logout')
        self.assertEqual(resolve(url).func,logoutpage)
        
    
class ViewFunctionsTest(TestCase):
    print("Testing 4 View Function Of Authentication App")
       
    def test_signup(self):
        client=Client()
        response=client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'authentication/signup.html')
        
    def test_signin(self):
        client=Client()
        response=client.get(reverse('signin'))
        self.assertTemplateUsed(response, 'authentication/signin.html')
        
    def test_otpverify(self):
        client=Client()
        response=client.get(reverse('otp'))
        self.assertTemplateUsed(response, 'authentication/otp.html')
        
    def test_logout(self):
        client=Client()
        response=client.get(reverse('logout'))
        self.assertRedirects(response, '/')