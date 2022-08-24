from django.db import models
from django.core.exceptions import ValidationError
from django import forms

def pnochk(value):
    x=len(str(value))
    if x!=10:
        raise forms.ValidationError("Invalid Mobile Number")
    
def pwcheck(value):
    x=value.isalnum()
    y=len(value)
    if x and y>8:
        raise forms.ValidationError("Incompatible Password")
    
def emchk(value):
    if '@' not in value:
        raise forms.ValidationError("Wrong Email")

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=70)
    pno=models.BigIntegerField(primary_key=True,validators=[pnochk])
    email=models.CharField(max_length=70,validators=[emchk])
    pwd=models.CharField(max_length=10,validators=[pwcheck])