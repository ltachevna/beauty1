from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.sing_in, name="sing_in"),
    path("registrestion/", views.register, name="register")

]