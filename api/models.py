from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

class Tag(models.Model):
    name = models.CharField(max_length=20,unique=True)
    
    def __str__(self):
        return f'{self.name}'
    
    
Phase_Choices = (
        ("To do","to do"),
        ("In Progress","in progress"),
        ( "Review","review"),
        ("Done","done")
    )

class Task(models.Model):
    Name = models.CharField(max_length = 200)
    Tag = models.ManyToManyField(Tag)
    Discription = models.TextField(max_length=400)
    #Phase = models.CharField(choices = Phase_Choices, default="To do", max_length=20)
    #index = models.IntegerField(default = None,null=True)
   
   # progress in '%'
    Progress = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
        
    start_time = models.DateTimeField()
    Deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.Name}'
    
    @property
    def Total_time(self):
        
        time = str((self.Deadline - self.start_time)/3600)[5:] + ' hour' #time in Hour Format
        
        return f'{time}'
 

class Phase(models.Model):
    Phase = models.CharField(choices=Phase_Choices, default="To do", max_length=20)
    Index = models.IntegerField()
    Tasks = models.ForeignKey(Task, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.Phase}:{self.Index}'
        
    @property
    def Task_in_phase(self):
        To_do = []
        In_Progress = []
        Review = []
        Done = []
        Dict1 = {}
        Dict2 = {}
        Dict3 = {}
        Dict4 = {}
        
        Todo_obj = Phase.objects.filter(Phase='To do')
        for item in Todo_obj:
            task = str(item.Tasks)
            Dict1.update({'Id': item.id, 'Index':item.Index, 'Task':task })
            Dict1_copy = Dict1.copy()
            To_do.append(Dict1_copy)
            
        In_Progress_obj = Phase.objects.filter(Phase='In Progress')
        for item in In_Progress_obj:
            task = str(item.Tasks)
            Dict2.update({"id": item.id, 'Index':item.Index, 'Task':task })
            Dict2_copy = Dict2.copy()
            In_Progress.append(Dict2_copy)
            
        Review_obj = Phase.objects.filter(Phase='Review')
        for item in Review_obj:
            task = str(item.Tasks)
            Dict3.update({"id": item.id, 'Index':item.Index, 'Task':task })
            Dict3_copy = Dict3.copy()
            Review.append(Dict3_copy)
        
        Done_obj = Phase.objects.filter(Phase='Done')
        for item in Done_obj:   
            task = str(item.Tasks)
            Dict4.update({"id": item.id, 'Index':item.Index, 'Task':task })
            Dict4_copy = Dict4.copy()
            Done.append(Dict4_copy)
            
        Phases = {'To do':To_do, 'In Progress':In_Progress, 'Review':Review, 'Done':Done}
        return Phases
        
        