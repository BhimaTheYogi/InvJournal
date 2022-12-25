from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None: 
            login(request, user)
            return redirect('Journal')
        
    return render(request, 'InvJournal/login_register.html', {'page':page})

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    context = {'form': form, 'page': page}
    return render(request, 'InvJournal/login_register.html', context)

@login_required(login_url='login')
def index(request):
    return HttpResponse("Hello, world. You're at the Main Page")
