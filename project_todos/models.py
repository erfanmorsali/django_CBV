from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User,related_name="todos",on_delete=models .CASCADE)
    title = models.CharField(max_length=50)
    time_to_do = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo,related_name='comments',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()


    def __str__(self) :
        return self.title