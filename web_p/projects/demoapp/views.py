from django.shortcuts import render
from .models import demoappModel
from .form import demoappForm
from django.http import HttpResponse

def create_view(request):
    form = demoappForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'demoapp/create_view.html', context)

def index(request):
    return HttpResponse("Hello, world!")