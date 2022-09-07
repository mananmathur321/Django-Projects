from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id','name', 'mailid', 'phoneno']
        labels = {'id':'ID',
                  'name':'Name',
                  'phoneno':'Phone Number',
                  'mailid':'Email'
                  }

        
        widgets = {'id':forms.NumberInput(attrs={'placeholder':'Enter Your ID','class':'form-control'}),
                   'name':forms.TextInput(attrs={'placeholder':'Enter Your Name','class':'form-control'}),
                   'mailid':forms.EmailInput(attrs={'placeholder':'Enter Your Email','class':'form-control'}),
                   'phoneno':forms.TextInput(attrs={'placeholder':'Enter Your Phone Number','class':'form-control'})
                  }
