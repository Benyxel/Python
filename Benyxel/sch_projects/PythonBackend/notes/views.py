from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Note

# Create your views here.

def add_user(req):
    pass

def read_notes(req):
    all_note = Note.objects.all()
    pass

def read_single_note(req):
    pass


def home_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have Been logged in')
            return redirect('home_view')
        
        else:
            messages.success(request, ' There was an Erorr logging in, Please try again ')
        
            return redirect('home_view')
    else:    
        return render(request,'index.html', {})




def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logout")
    return redirect('home_view')

def register_user(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password  = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have created an account')
            return redirect('home_view')
        
        
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})