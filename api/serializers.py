from rest_framework import serializers, fields
from .models import *

        
class TaskSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Task
        Total_time = fields.Field(source = 'Total_time')
        Tag_list = fields.Field(source = 'Tag_list')
        fields = ['id','Name','Discription','Tags','Tag_list','start_time','Deadline','Progress','Total_time','created_at', 'updated_at']
        extra_kwargs = {'Tags': {'write_only': True}, }
        

class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','Name','Phase','Index']
        
        