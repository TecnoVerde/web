from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
# Create your views here.

def index(request):
    return render(request, 'TecnoVerde/index.html')

def contaminacion(request):
    return render(request, 'TecnoVerde/contaminacion.html')
    
def alternativas(request):
    return render(request, 'TecnoVerde/alternativas.html')

def ss(request):
    return render(request, 'TecnoVerde/ss.html')

def index3(request):
    return render(request, 'TecnoVerde/index3.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SignupForm()

    context = {
        'form': form
    }
    return render(request, 'TecnoVerde/signup.html', context)

def loginForm(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index3')
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'TecnoVerde/login.html', context)

def logout_user(request):
    logout(request)

    return redirect('index')

