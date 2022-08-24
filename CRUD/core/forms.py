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
        
        # def clean_pno(self):
        #     if len(str(self.cleaned_data(Person.pno)))!=10:
        #         raise forms.ValidationError("Invalid Mobile Number")
        #     else:
        #         return self.cleaned_data(Person.pno)
            
        # def clean_email(self):
        #     if '@' not in self.cleaned_data(Person.email):
        #         raise forms.ValidationError("Wrong Email")
        #     else:
        #         return self.cleaned_data(Person.email)
            
        # def clean_pwd(self):
        #     x=self.cleaned_data(Person.pwd).isalnum()
        #     y=len(self.cleaned_data(Person.pwd))
        #     if x and y>8:
        #         raise forms.ValidationError("Incompatible Password")
        #     else:
        #         return self.cleaned_data(Person.pwd)