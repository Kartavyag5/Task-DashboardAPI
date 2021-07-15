from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

class Tag(models.Model):
    Name = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.Name}'
    
    
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
    Phase = models.CharField(choices = Phase_Choices, default="To do", max_length=20)
   
   #progress in '%'
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
        time = (self.Deadline - self.start_time)/3600  #time in Hour Format
        return time
       


    