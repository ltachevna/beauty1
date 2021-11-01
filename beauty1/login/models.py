from django.db import models


class Sing_in(models.Model):
    email = models.CharField(max_lenght=40)
    password = models.CharField(max_lenght=20)

class Register(models.Model):
    email = models.CharField(max_lenght=40)
    password = models.CharField(max_lenght=20)
    repeat_password = models.CharField(max_lenght=20)



# Create your models here.
