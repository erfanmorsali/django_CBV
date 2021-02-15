from django import contrib
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import forms
from django.http.response import HttpResponse
from django.views.generic import ListView , DetailView , FormView , CreateView , UpdateView , DeleteView
from django.views.generic.edit import FormMixin
from django.views.generic.base import TemplateView 
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Todo
from .forms import CreateCommentForm


class HomePage(TemplateView):
    template_name = "project_todos/home_page.html"


class AllTodosView(ListView):
    # QuerySet for listview
    queryset = Todo.objects.all()
    ordering = ['-id']
    template_name = "project_todos/todos.html"
    context_object_name = "todos_list"

    # send additional data to template
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        return context


class TodoDetailView(LoginRequiredMixin,FormMixin ,DetailView):    
    template_name = "project_todos/todo_detail.html"
    form_class = CreateCommentForm
    success_url = reverse_lazy("todos:todos_page")


    def get_object(self,**kwargs):
        todo =  Todo.objects.filter(id=self.kwargs["id"],title=self.kwargs['title']).first()
        return todo
    
    def post(self,request,*args, **kwargs):
        form = self.get_form()
        todo = self.get_object()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.todo = todo
            comment.save()
        return super().form_valid(form)

    def get_object_comments(self):
        obj = self.get_object()
        return obj.comments.all()

    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context['comments'] = self.get_object_comments()
        return context

# class CreateTodoView(FormView):
#     template_name = "project_todos/create_todo.html"
#     form_class = CreateTodoForm
#     success_url = reverse_lazy("todos:todos_page")

#     def form_valid(self, form):
#         cd = form.cleaned_data
#         Todo.objects.create(user=self.request.user,title=cd['title'])
#         return super().form_valid(form)


class CreateTodoView(CreateView):
    model = Todo
    template_name = "project_todos/create_todo.html"
    fields = ("title","time_to_do")
    success_url = reverse_lazy("todos:todos_page")

    def form_valid(self, form):
        new_todo = form.save(commit=False)
        new_todo.user = self.request.user 
        new_todo.save()
        return super().form_valid(form)


class DeleteTodoView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todos:todos_page")
    template_name = "project_todos/delete_todo.html"


class UpdateTodoView(UpdateView):
    model = Todo
    fields = ("title" , "time_to_do")
    template_name = "project_todos/update_todo.html"
    success_url = reverse_lazy("todos:todos_page")