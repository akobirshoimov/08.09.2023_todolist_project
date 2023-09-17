from rest_framework import serializers 
from .models import TodolistModel
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
 

class Todolistserializer(serializers.ModelSerializer):
    class Meta:
        model = TodolistModel
        fields = ('task_name','created_at','updated_at','status','desc','user')
    
    def create(self, validated_data):
        validated_data['user'] = get_object_or_404(User,username=self.context['request'].user)
        return super(Todolistserializer,self).create(validated_data)
     
