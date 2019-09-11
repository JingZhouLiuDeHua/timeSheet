from django.db import models

# Create your models here.
class Location(models.Model):
    Location = models.CharField(max_length=50)
    Sector = models.CharField(max_length=50)