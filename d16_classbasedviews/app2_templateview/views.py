from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class MyTemplateView(TemplateView):
    template_name = 'app2/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["name"] = 'Ram'
        # context["city"] = 'Ayodhya'
        context = {        #Using dictionary for context
            'name':'Ram',
            'city':'Ayodhya'
        }
        return context
    

