from rest_framework import serializers , fields
from .models import *
#from rest_framework.fields import Field

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']
        

class TaskSerializer(serializers.ModelSerializer):
    Tag = TagSerializer(many=True)
    class Meta:
        model = Task
        Total_time = fields.Field(source = 'Total_time')
        fields = ['id','Name','Discription','Phase','Tag','start_time','Deadline','Progress','Total_time','created_at', 'updated_at']
        
        
