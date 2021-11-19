from django.db import models


class Login(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    repeat_password = models.CharField(max_length=100)
    # post = models.ForeignKey(related_name="login", on_delete=models.CASCADE)



