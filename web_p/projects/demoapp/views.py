from django.shortcuts import render
from .models import Students
from django.http import HttpResponse



def index(request):
    return render(request, 'student/index.html', 
    {'students': Students.objects.all()})
