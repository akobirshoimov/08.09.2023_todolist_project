from django.urls import path
from .views import AllTodoView,CreateTodoView,DelUpdate#UpdateTodolistView,DetailTodolistView,ListTodolistView,CreateTodolistView,DeleteTodolistView,TodaytodoView

urlpatterns = [
    # path('create/',CreateTodolistView.as_view()),
    # path('update/<int:todolist_id>/',UpdateTodolistView.as_view()),
    # path('detail/<int:todolist_id>/',DetailTodolistView.as_view()),
    # path('all/',ListTodolistView.as_view()),
    # path('delete/<int:todolist_id>/',DeleteTodolistView.as_view()),
    # path('today-todo/',TodaytodoView.as_view)
    path('all/',AllTodoView.as_view()),
    path('create/<int:id>/',CreateTodoView.as_view()),
    path('DeleteUpdate/<int:id>/',DelUpdate.as_view())
]