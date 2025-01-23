from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from atividades.models import Favorito
from livros.models import Livro
from .forms import RegisterForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

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
    
    return render(request, 'usuarios/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.is_superuser = form.cleaned_data.get('is_superuser') == 'True'  
            user.is_staff = user.is_superuser  
            user.save()  
            return redirect('usuarios:login')

    else:
        form = RegisterForm()
    
    return render(request, 'usuarios/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('usuarios:login')


def perfil(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  
            return redirect('usuarios:perfil') 
    else:
        form = PasswordChangeForm(user=request.user)

    livros  = Favorito.objects.filter(user=request.user)
    
    return render(request, 'usuarios/perfil.html', {'form': form, 'livros' : livros})