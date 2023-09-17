from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class TodolistModel(models.Model):
    task_name = models.CharField(max_length=120 , default= ' nothing')
    created_at = models.DateField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=120)
    desc = models.CharField(max_length=300)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.task_name
    
        
