from django import forms
from .models import Comment

class CreateTodoForm(forms.Form):
    title = forms.CharField(max_length=50)

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("title", "body")