from rest_framework import serializers, fields
from .models import *

        
class TaskSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Task
        Total_time = fields.Field(source = 'Total_time')
        Tag_list = fields.Field(source = 'Tag_list')
        fields = ['id','Name','Discription','Phase','Index','Tags','Tag_list','start_time','Deadline','Progress','Total_time','created_at', 'updated_at']
        extra_kwargs = {
            'Tags': {'write_only': True},
            'Index': {'write_only': True},
            'Phase': {'write_only': True}
        }
        
        
        


class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','Name','Phase','Index']
        # validators = [
        #      UniqueTogetherValidator(
        #          queryset=Phase.objects.filter(Phase='To do'),
        #          fields=['Phase', 'Index']
        #      )]
        #read_only_fields = ['Name']

        