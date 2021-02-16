from .serializers import TodoSerializer, CreateTodoSerializer

class SerializerMixin:
    def dispatch(self,request,*args,**kwargs):
        if request.method == "POST":
            self.serializer_class = CreateTodoSerializer
        else:
            self.serializer_class = TodoSerializer
        return super().dispatch(request , *args , **kwargs)