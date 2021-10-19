from django.shortcuts import render
from .forms import CommentFrom

def sing_in(request):
    if request.method == 'POST':
        print(request.POST['Email'])
        print(request.POST['Password'])
    elif request.method == 'GET':
        return render(request, 'sing_in.html')

def register(request):
    if request.method == 'POST':
        print(request.POST['Email'])
        print(request.POST['Password'])
        print(request.POST['Repeat Password'])
    elif request.method == 'GET':
        return render(request, 'register.html') #вернуть главную страницу вместо регистрации

# Create your views here.
