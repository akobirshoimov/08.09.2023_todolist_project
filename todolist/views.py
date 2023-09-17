from django.shortcuts import render,get_object_or_404
from .models import TodolistModel
from rest_framework.views import APIView  
from rest_framework.response import Response
from .serializer import Todolistserializer
import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


# Create your views here.
# class CreateTodolistView(APIView):
#     def post(self,request):
#         data = request.data
#         serializer = TodolistModel(data=data)
#         if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data)
#         return Response(serializer.errors)
               
#         return Response(serializer.errors)
class AllTodoView(generics.ListAPIView):
    queryset = TodolistModel.objects.all()
    serializer_class = Todolistserializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return TodolistModel.objects.all()


class CreateTodoView(generics.CreateAPIView):
    queryset = TodolistModel.objects.all()
    serializer_class = Todolistserializer
    permission_classes = (IsAuthenticated,)


# class UpdateTodolistView(APIView):
#     def patch(self,request,*arg,**kwargs):
#         todolist = get_object_or_404(TodolistModel,id = kwargs['todolist_id'])
#         serializer = Todolistserializer(todolist, data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# class DetailTodolistView(APIView):
#     def get(self, request, *args, **kwargs):
#         todolist = get_object_or_404(TodolistModel, id=kwargs['todolist_id'])
#         serialzier = Todolistserializer(todolist.data)

#         return Response(serialzier.data) 

# class ListTodolistView(APIView):
#     def get(self, request):
#         all_data = TodolistModel.objects.all()
#         serializer = Todolistserializer(all_data, many=True)
#         return Response(serializer.data)
  
# class DeleteTodolistView(APIView):
#     def delete(self,request,*args,**kwargs):
#         todolist = get_object_or_404(TodolistModel,id = kwargs['todolist_id'])
#         todolist.delete()
#         return Response({'detail deleted!'})
# class TodaytodoView(APIView):
#     def get(request):
#         today = datetime.date.today()
#         todo = TodolistModel.objects.filter(created_at__date=today)
#         serializer = Todolistserializer(todo,many =True)
#         return Response(serializer.data)

class DelUpdate(generics.RetrieveDestroyAPIView):
    queryset = TodolistModel.objects.all()
    serializer_class = Todolistserializer
    permission_classes = (IsAuthenticated,)

    
    
