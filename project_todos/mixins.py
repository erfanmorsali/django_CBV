class FieldsDetectorMixin:
    def dispatch(self,request,*args,**kwargs):
        if request.user.username == "erfan":
            self.fields = ("title",)
        else:
            self.fields = ("title","time_to_do")
        return super().dispatch(request,*args,**kwargs)