from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                
                return redirect('index')
           
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:login')

    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('usuarios:login')
