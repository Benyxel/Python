from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello world")


def signup(request):
    return HttpResponse("signup")

def login(request):
    return HttpResponse("login")

def logout(request):
    return HttpResponse("logout")