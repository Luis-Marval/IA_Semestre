from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def home(request):
    url = reverse('home')
    return render(request, 'home.html', {'url': url})

def index(request):
    return render(request, 'index.html')


# REGISTRO DE USUARIO
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')      
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

#INICIO DE SESION
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # SE CAPTURAN LOS DATOS
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('index')
    form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'login.html', context)

#CIERRE DE SESION
def logout(request):
    auth.logout(request)
    return redirect('login')