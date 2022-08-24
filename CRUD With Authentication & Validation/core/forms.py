from django import forms
from django.core import validators
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'pno', 'email', 'pwd']
        labels = {'name':'Name',
                  'pno':'Phone Number',
                  'email':'Email',
                  'pwd':'Password'
                  }

        
        widgets = {'pwd':forms.PasswordInput(render_value=True, attrs={'placeholder':'Enter Your Password','class':'form-control'}),
                   'name':forms.TextInput(attrs={'placeholder':'Enter Your Name','class':'form-control'}),
                   'email':forms.EmailInput(attrs={'placeholder':'Enter Your Email','class':'form-control'}),
                   'pno':forms.TextInput(attrs={'placeholder':'Enter Your Phone Number','class':'form-control'})
                  }