import datetime
from django.shortcuts import render, HttpResponse

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import *
from .serializers import *
from .models import *
from rest_framework.filters import SearchFilter,OrderingFilter
from django.core.exceptions import ValidationError

class TaskAPIViewSet(ModelViewSet):
    serializer_class =TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['^Name', '^Phase']
    ordering_fields = '__all__'
    
    
class TagAPIViewset(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    search_fields = ['^Name']
    ordering_fields = ['Name']
    
class TaskInPhaseViewset(ModelViewSet):
    serializer_class = PhaseSerializer
    queryset = Phase.objects.all()
    

class TaskInPhaseViewset2(ModelViewSet):
    serializer_class = PhaseDetailsSerializer
    queryset = Phase.objects.filter(Phase='To do')
    for items in queryset:
        print(items.Phase)
    def get(self,request,pk):
        id=pk
        phase = Phase.objects.all()
        print(phase.Index)
        

        
     


# this function is only for testing purpose
def test(request,pk):
    pass
        
