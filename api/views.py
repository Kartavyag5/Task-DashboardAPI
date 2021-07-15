from django.shortcuts import render
from rest_framework.generics import *
from .serializers import *
from .models import *
from rest_framework.filters import SearchFilter,OrderingFilter

class TaskAPIView(ListCreateAPIView):
    serializer_class =TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['^Name', '^Phase']
    ordering_fields = '__all__'
    
class TaskDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class =TaskSerializer
    queryset = Task.objects.all()
    
class TagAPIView(ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    search_fields = ['^Name']
    ordering_fields = ['Name']
    
class TagDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    