from django.urls import path
from . import views


app_name = "apis"
urlpatterns = [
    path("", views.AllTodosView.as_view()),
    path("all_users/", views.AllUsersView.as_view()),
]
