from django.db import models
from django import forms
# Create your models here.

class Student(models.Model):
    
    def idchk(self):
        if self<0:
            raise forms.ValidationError("Invalid Id")
    
    def pnochk(self):
        x=len(str(self))
        if x!=10:
            raise forms.ValidationError("Invalid Mobile Number")
        
    def emchk(self):
        if '@' not in self:
            raise forms.ValidationError("Wrong Email")
    
    id=models.IntegerField(primary_key=True, validators=[idchk])
    name=models.CharField(max_length=50)
    mailid=models.EmailField(max_length=80, validators=[emchk])
    phoneno=models.BigIntegerField(validators=[pnochk])