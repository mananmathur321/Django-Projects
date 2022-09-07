from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    
    def idchk(self):
        if self<0:
            raise serializers.ValidationError("Invalid Id")
    
    def pnochk(self):
        x=len(str(self))
        if x!=10:
            raise serializers.ValidationError("Invalid Mobile Number")
        
    def emchk(self):
        if '@' not in self:
            raise serializers.ValidationError("Wrong Email")
    
    id=serializers.IntegerField(validators=[idchk])
    mailid=serializers.EmailField(max_length=80,validators=[emchk])
    phoneno=serializers.IntegerField(validators=[pnochk])
    
    class Meta:
        model=Student
        fields=['id','name','mailid','phoneno']