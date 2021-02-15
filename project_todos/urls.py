from django.urls import path
from . import views


app_name = "todos"
urlpatterns = [
    path('', views.HomePage.as_view() , name="home_page"),
    path('all_todos/', views.AllTodosView.as_view() , name="todos_page"),
    path('todo_detail/<title>/<id>/', views.TodoDetailView.as_view() , name="todo_detail"),
    path('create_todo/', views.CreateTodoView.as_view() , name="create_todo"),
    path('delete_todo/<int:pk>', views.DeleteTodoView.as_view() , name="delete_todo"),
    path('update_todo/<int:pk>', views.UpdateTodoView.as_view() , name="update_todo"),
]
