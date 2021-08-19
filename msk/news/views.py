from django.shortcuts import render
from django.views import generic
from datetime import datetime
# Create your views here.

class ViewIndex(generic.TemplateView):
    
    template_name = 'news/index.html'

    def __init__(self):
        now = datetime.now()

    def test(self,request):
        now = datetime.now()
        self.extra_context = {'obj':{},'now':now}
        return render(request, self.template_name, self.extra_context)