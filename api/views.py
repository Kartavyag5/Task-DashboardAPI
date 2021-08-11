from django.shortcuts import  get_object_or_404
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.decorators import api_view

from django.db.models import Count


class TaskAPIViewSet(ModelViewSet):
    serializer_class =TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['^Name', '^Phase']
    ordering_fields = '__all__'
    
        
class PhaseViewSet(ViewSet):
    queryset=Task.objects.all()
    serializer_class = PhaseSerializer
    
    def list(self, request):
        To_do = []
        In_Progress = []
        Review = []
        Done = []
        Dict1 = {}
        Dict2 = {}
        Dict3 = {}
        Dict4 = {}

        def sortFunc(e):
            return e['Index']
        
        #Re arrenge list after create new Task
        q = Task.objects.filter(Phase='To do').annotate(Count('Index')).order_by('Index')
        print('To do re-arrenge')
        count=q.count()
        for i in range(0,count):
            Task.objects.filter(Phase='To do',Name=q[i]).update(Index=i+1)
        
        Todo_obj = Task.objects.filter(Phase='To do')
        for item in Todo_obj:
            task = str(item.Name)
            Dict1.update({'Id': item.id, 'Index':item.Index, 'Task':task })
            Dict1_copy = Dict1.copy()
            To_do.append(Dict1_copy)            
        To_do.sort(key=sortFunc)

        In_Progress_obj = Task.objects.filter(Phase='In Progress')
        for item in In_Progress_obj:
            task = str(item.Name)
            Dict2.update({"id": item.id, 'Index':item.Index, 'Task':task })
            Dict2_copy = Dict2.copy()
            In_Progress.append(Dict2_copy)
        In_Progress.sort(key=sortFunc)
            
        Review_obj = Task.objects.filter(Phase='Review')
        for item in Review_obj:
            task = str(item.Name)
            Dict3.update({"id": item.id, 'Index':item.Index, 'Task':task })
            Dict3_copy = Dict3.copy()
            Review.append(Dict3_copy)
        Review.sort(key=sortFunc)
        
        Done_obj = Task.objects.filter(Phase='Done')
        for item in Done_obj:   
            task = str(item.Name)
            Dict4.update({"id": item.id, 'Index':item.Index, 'Task':task })
            Dict4_copy = Dict4.copy()
            Done.append(Dict4_copy)
        Done.sort(key=sortFunc)
            
        Phases = {'To do':To_do, 'In Progress':In_Progress, 'Review':Review, 'Done':Done}
        return Response(Phases)


    def retrieve(self, request, pk=None):
        queryset = Task.objects.filter(id=pk)
        task = get_object_or_404(queryset, pk=pk)
        serializer = PhaseSerializer(task)
        return Response(serializer.data)


@api_view(['GET','PUT'])
def partial_update(request,pk,*args, **kwargs):
    task = Task.objects.get(id=pk)

    old_phase = task.Phase
    old_index = task.Index
    serializer = PhaseSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

    if request.method=='PUT':
        new_phase = request.data.get('Phase')
        new_index = request.data.get('Index')
        new_phase_obj = Task.objects.filter(Phase=new_phase)
      
        for items in new_phase_obj:
            
            if Task.objects.filter(Phase=new_phase).count()==1:
                Task.objects.filter(Index=items.Index, Phase=new_phase).update(Index=1)

            if old_index < items.Index:                
                Task.objects.filter(Index=items.Index, Phase=old_phase).exclude(Index=pk).update(Index= items.Index - 1)
                print("elif 1")
            
            
            elif new_index < items.Index:
                                
                Task.objects.filter(Index=items.Index, Phase=new_phase).exclude(Index=pk).update(Index= items.Index + 1)
                print('elif 2')
                
        # this checks the if same phase and same index already exists:
        task2=Task.objects.filter(Phase=new_phase, Index=new_index).exclude(id=pk)
        if task2.exists():
            Task.objects.filter(Index=new_index, Phase=new_phase).exclude(id=pk).update(Index= new_index + 1)
            print('if exists')

             
        # re-arrenge index of new Phase
        q = Task.objects.filter(Phase=new_phase).annotate(Count('Index')).order_by('Index')
        print(q.count())
        count=q.count()
        for i in range(0,count):
            Task.objects.filter(Phase=new_phase,Name=q[i]).update(Index=i+1)

        #re-arrenge index of old Phase
        q2 = Task.objects.filter(Phase=old_phase).annotate(Count('Index')).order_by('Index')
        print(q2.count())
        count=q2.count()
        for i in range(0,count):
            Task.objects.filter(Phase=old_phase,Name=q2[i]).update(Index=i+1)

        Index_Change_Payload = {'id':pk, 'old_phase':old_phase, 'old_index':old_index, 'new_phase':new_phase, 'new_index':new_index}
        return Response(Index_Change_Payload)
    
    return Response(serializer.data)

