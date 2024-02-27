from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def learnDjango(request):
    return HttpResponse('<h1>Learning Django</h1>')



def if_for(request):
    context = {
        'name' : 'Mahesh',
        'digit' : 0,
        'names' : ['ramesh','mahesh','umesh','suresh']
    }
    return render(request,'app1/iffor.html',context=context)

def appleveltemplate(request):
    return render(request,'app1/appleveltemplate.html')