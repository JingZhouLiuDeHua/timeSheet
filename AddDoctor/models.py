from django.db import models

# Create your models here.
class Doctor(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    FileNumber = models.PositiveIntegerField()

