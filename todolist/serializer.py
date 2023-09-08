from rest_framework import serializers 
from .models import TodolistModel
 

class Todolistserializer(serializers.ModelSerializer):
    class Meta:
        model = TodolistModel
        fields = ('task_name','created_at','updated_at','status','desc')
