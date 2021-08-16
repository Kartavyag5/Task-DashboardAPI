from django.shortcuts import  get_object_or_404
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response

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
        # q = Task.objects.filter(Phase='To do').annotate(Count('Index')).order_by('Index')
        # print('To do re-arrenge')
        # count=q.count()
        # for i in range(0,count):
        #     Task.objects.filter(Phase='To do',Name=q[i]).update(Index=i+1)
        
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
    old_phase_obj = Task.objects.filter(Phase=old_phase)
    old_index = task.Index
    serializer = PhaseSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

    if request.method=='PUT':
        new_phase = request.data.get('Phase')
        new_index = request.data.get('Index')
        new_phase_obj = Task.objects.filter(Phase=new_phase)


        # if two phases are same
        if new_phase==old_phase:
            for items in new_phase_obj:
                count = Task.objects.filter(Phase=new_phase).count()
                if count==new_index :
                    Task.objects.filter(id=pk, Phase=old_phase).update(Index= count+1)
                    new_index += 1
                    print("count1")
                    break

                if new_index==1:
                    Task.objects.filter(id=pk, Phase=old_phase).update(Index= 0)
                    print("count2")
                    break

                elif old_index < new_index:
                    if items.Index > old_index and items.Index <= new_index:                
                        Task.objects.filter(Index=items.Index, Phase=old_phase).exclude(id__exact=pk).update(Index= items.Index - 1)
                        print("elif 1")
                    
                elif new_index < old_index:
                    if items.Index > new_index:     
                        Task.objects.filter(Index=items.Index, Phase=new_phase).exclude(id__exact=pk).update(Index= items.Index + 1)
                        print('elif 2')

        #two phases are different
        else:
            count=Task.objects.filter(Phase=new_phase).count()
            for items in new_phase_obj:
                if new_index==1:
                    Task.objects.filter(id=pk, Phase=new_phase).update(Index= 0)
                    print("Index1")
                    break
                
                if new_index==count:
                    Task.objects.filter(id=pk, Phase=new_phase).update(Index= count+1)
                    new_index += 1
                    print("Index-count")
                    break
                
                if new_index <= items.Index:                        
                    Task.objects.filter(Index=items.Index, Phase=new_phase).exclude(id__exact=pk).update(Index= items.Index + 1)
                    print('elif 4')

        # this checks the if same phase and same index already exists:
        task2=Task.objects.filter(Phase=new_phase, Index=new_index).exclude(id__exact=pk)
        if task2.exists():
            if count==new_index:
                task3=Task.objects.filter(Phase=new_phase).exclude(id__exact=pk)
                for items in task3:
                    Task.objects.filter(Phase=new_phase).exclude(id__exact=pk).update(Index=items.Index-1)
                print('if exists')

            if count > new_index:
                Task.objects.filter(Index=new_index, Phase=new_phase).exclude(id__exact=pk).update(Index= new_index + 1)
                print('if exists2')
            
             
        # re-arrenge index of new Phase
        q = Task.objects.filter(Phase=new_phase).annotate(Count('Index')).order_by('Index')
        print('Re-arrenge1')
        count=q.count()
        lst = []
        for i in range(0,count):
            lst.append(q[i])
        for i in range(0,count):
            Task.objects.filter(Phase=new_phase,Name=lst[i]).update(Index=i+1)
            
        #re-arrenge index of old Phase
        q2 = Task.objects.filter(Phase=old_phase).annotate(Count('Index')).order_by('Index')
        print('Re-arrenge2')
        count=q2.count()
        lst2 = []
        for i in range(0,count):
            lst2.append(q2[i])
        for i in range(0,count):
            Task.objects.filter(Phase=old_phase,Name=lst2[i]).update(Index=i+1)

        Index_Change_Payload = {'id':pk, 'old_phase':old_phase, 'old_index':old_index, 'new_phase':new_phase, 'new_index':new_index}
        return Response(Index_Change_Payload)
    
    return Response(serializer.data)

