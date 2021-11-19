from django.shortcuts import render
from .forms import LoginForm


def sing_in(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            pass

    elif request.method == 'GET':
        context = {
            "form": form
        }
        return render(request, 'home_page.html', context)

def register(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            pass
    elif request.method == 'GET':
        context = {
            "form": form
        }
        return render(request, 'home_page.html', context)


