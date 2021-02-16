from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("project_todos.urls",namespace='todos')),
    path('api/v1/', include("project_apis.urls",namespace='apis')),
]
