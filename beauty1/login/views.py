from django.shortcuts import render
from .forms import Sing_inForm
from .forms import RegisterForm
# from django.contrib.auth import user

def sing_in(request):
    form = Sing_inForm()
    if request.method == 'POST':
        form = Sing_inForm(request.POST)
        if form.is_valid():
            pass

    elif request.method == 'GET':
        context = {
            "form": form
        }
        return render(request, 'sing_in.html', context)

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            pass
    elif request.method == 'GET':
        context = {
            "form": form
        }
        return render(request, 'register.html', context) #вернуть главную страницу вместо регистрации

# Create your views here.
