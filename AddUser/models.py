from django.db import models

# Create your models here.
class User(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Description = models.CharField(max_length=250)
    LoginIDOrEmail = models.CharField(max_length=250)
    Authority = models.PositiveIntegerField()  # admin or regular, only admin could create user or modify records,regular read-only
    Password  = models.CharField(max_length=250)
    RetypePassword = models.CharField(max_length=250)
