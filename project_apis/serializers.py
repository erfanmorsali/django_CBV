from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from project_todos.models import Todo , Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ("user","todo")
        

class TodoSerializer(ModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Todo
        fields = "__all__"


class CreateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("title",)

    def validate_title(self, value):
        if Todo.objects.filter(title=value).exists():
            raise serializers.ValidationError("title is not unique")
        return value


class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True)
    class Meta:
        model = User
        exclude = ("password","groups","user_permissions","last_login")