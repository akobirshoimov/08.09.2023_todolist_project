from django.urls import path
from .views import UpdateTodolistView,DetailTodolistView,ListTodolistView,CreateTodolistView,DeleteTodolistView

urlpatterns = [
    path('create/',CreateTodolistView.as_view()),
    path('update/<int:todolist_id>/',UpdateTodolistView.as_view()),
    path('detail/<int:todolist_id>/',DetailTodolistView.as_view()),
    path('all/',ListTodolistView.as_view()),
    path('delete/<int:todolist_id>/',DeleteTodolistView)
]