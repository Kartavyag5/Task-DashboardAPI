from rest_framework import serializers , fields
from rest_framework.validators import UniqueTogetherValidator
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
        fields = ['id','Name','Discription','Tag','start_time','Deadline','Progress','Total_time','created_at', 'updated_at']
        


class PhaseSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Phase
        Task_in_phase = fields.Field(source = 'Task_in_phase')
        fields = ['Task_in_phase']
        
class PhaseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        
        fields = ['id','Phase','Index','Tasks']
        read_only_fields = []
        validators = [
            UniqueTogetherValidator(
                queryset=Phase.objects.filter(Phase='To do'),
                fields=['Phase', 'Index']
            )
        ]