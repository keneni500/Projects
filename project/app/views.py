from django.shortcuts import render
from django.http import HttpResponse
from .  import models

# Create your views here.

def index(request):
    all_vendors=models.Vendors.objects.all()
    return render(request,'index.html', {'vendors': all_vendors})

def about(request):
    message='This is just vendors page history and all about vendors'
    return render(request, 'about.html', {'message':message})