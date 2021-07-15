from rest_framework import serializers
from .models import *
from rest_framework.fields import Field

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','Name']

class TaskSerializer(serializers.ModelSerializer):
    Tag = TagSerializer(many=True)
    class Meta:
        model = Task
        Total_time = Field(source = 'Total_time')
        fields = ['id','Name','Discription','Phase','Tag','start_time','Deadline','Progress','Total_time','created_at', 'updated_at']
        
        
