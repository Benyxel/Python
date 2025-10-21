from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
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
    pass