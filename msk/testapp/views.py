from django.shortcuts import render
from django.views import generic
from datetime import datetime
# Create your views here.
class ViewIndex(generic.TemplateView):
    
    template_name = 'testapp/index.html'

    def __init__(self):
        now = datetime.now()
    def get(self, request, *args, **kwargs):
        now = datetime.now()
       
        # obj = []
        obj = {}

        self.extra_context = {'obj':obj,'now':now}
        return render(request, self.template_name, self.extra_context)
