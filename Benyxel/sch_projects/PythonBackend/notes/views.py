from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, Add_user
from .models import Note, Person 

# Create your views here.
# ADDUSER
def add_user(req):
    if req.method =="POST":
        form = Add_user(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'New User Added Successful')
            return redirect('persons')
        
    else:
        form = Add_user()
    return render(req, "adduser.html", {"form": form})
    
    # Update
def update(req, id):
    user = get_object_or_404(Person, id = id)
    if req.method == 'POST':
        form = Add_user(req.POST, instance= user)
        if form.is_valid():
            form.save()
            
            return redirect('adduser')
    else:
        form = Add_user(instance= user)
    return render(req, 'update.html', {'form':form})

# Delete
def delete_user(req, id):
    user = get_object_or_404(Person, id = id)
    if req.method == 'POST':
        user.delete()
    return redirect('persons')
    

def read_notes(req):
   
    persons = Person.objects.all()  
    all_notes = Note.objects.all()
    return render(req, 'note.html', {'notes': all_notes, 'persons': persons,  })

def read_note_single(req, id):
    note = get_object_or_404(Note, id=id)
    return render(req, 'details.html', {'note': note},  )

def persons(req):
    persons = Person.objects.all()  
    all_persons = Person.objects.all() 
    return render(req, 'persons.html', {'persons': all_persons, 'persons': persons  })




# Home view

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
        notes_count = Note.objects.count()
        persons_count = Person.objects.count()
        persons = Person.objects.all()   
        return render(request,'index.html', {'persons': persons, 'persons_count': persons_count, 'notes_count': notes_count})

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