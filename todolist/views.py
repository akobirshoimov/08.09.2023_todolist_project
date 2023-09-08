from django.shortcuts import render,get_object_or_404
from .models import TodolistModel
from rest_framework.views import APIView  
from rest_framework.response import Response
from .serializer import Todolistserializer

# Create your views here.
class CreateTodolistView(APIView):
    def post(self,request):
        data = request.data
        serializer = TodolistModel(data = data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
        return Response(serializer.errors)
               
#         return Response(serializer.errors)
class UpdateTodolistView(APIView):
    def patch(self,request,*arg,**kwargs):
        todolist = get_object_or_404(TodolistModel,id = kwargs['todolist_id'])
        serializer = Todolistserializer(todolist, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DetailTodolistView(APIView):
    def get(self, request, *args, **kwargs):
        todolist = get_object_or_404(TodolistModel, id=kwargs['todolist_id'])
        serialzier = Todolistserializer(todolist)

        return Response(serialzier.data) 

class ListTodolistView(APIView):
    def get(self, request):
        all_data = TodolistModel.objects.all()
        serializer = Todolistserializer(all_data, many=True)
        return Response(serializer.data)
  
class DeleteTodolistView(APIView):
    def delete(self,request,*args,**kwargs):
        todolist = get_object_or_404(TodolistModel,id = kwargs['todolist_id'])
        todolist.delete()
        return Response({'detail deleted!'})
    


