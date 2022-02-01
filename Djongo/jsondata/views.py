from django.shortcuts import render
from . models import *
# Create your views here.

def index(request):
    data = jsoninfo.objects.all()

    context ={
        "data": data
    }

    return render(request, 'jsondata/index.html', context)