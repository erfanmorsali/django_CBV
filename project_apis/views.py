from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, ListCreateAPIView
from project_todos.models import Todo
from .permissions import IsAdminOrReadOnly
from .mixins import SerializerMixin
from .serializers import UserSerializer


class AllTodosView(SerializerMixin,ListCreateAPIView):
    queryset = Todo.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class AllUsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
