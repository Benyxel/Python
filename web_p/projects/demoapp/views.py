from django.shortcuts import render
from .models import Students
from django.http import HttpResponseRedirect
from django.urls import reverse



def index(request):
    return render(request, 'student/index.html', 
    {'students': Students.objects.all()})

def view_student(request, student_id):
    student = Students.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))