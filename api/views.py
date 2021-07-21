import datetime
from django.shortcuts import render, HttpResponse
from rest_framework.viewsets import ModelViewSet
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
    
    '''
    def create(self,request):
        if request.POST:
            name = request.POST['Name']
            tag = request.POST['Tag']
            Description = request.POST['Description']
            phase = request.POST['Phase']
            y_index = request.POST['y_index']
            
            task = User.objects.filter(Phase=phase, y_index=y_index)
            if task:
                y_index+=1
            newtask = Task.objects.create(Name=name, Tag=tag, Description=Description, phase=Phase, y_index=y_index)
            newtask.save()    
    '''
    
class TaskIndexAPIViewSet(ModelViewSet):
    serializer_class = TaskIndexSerializer
    queryset = Task.objects.all()
    
    
class TagAPIViewset(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    search_fields = ['^Name']
    ordering_fields = ['Name']
    

# this function is only for testing purpose
    
def test(request,pk):
    pass
        
'''
    qs = Task.objects.all()
    for items in qs:
        start_time = items.start_time
    date1 = datetime.datetime.now() - datetime.datetime(start_time)
    date2 =datetime.datetime(2021,7,17,12,4,30)
    date3 = date1 - date2
    return HttpResponse(date1)
'''
    