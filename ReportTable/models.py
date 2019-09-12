from django.db import models

# Create your models here.
class Report(models.Model):
    Doctor_name = models.CharField(max_length=50)
    FileNumber = models.PositiveIntegerField()
    Location = models.CharField(max_length=50)
    Sector = models.CharField(max_length=50)
    Work_Date = models.DateTimeField(auto_now_add=True)
    Time_In = models.DateTimeField(auto_now_add=True)
    Time_Out = models.DateTimeField(auto_now_add=True)
    Hours_Worked = models.PositiveIntegerField()
    Hours_Code = models.CharField(max_length=50)
    Report_Date = models.DateTimeField(auto_now_add=True)
    Batch_ID = models.PositiveIntegerField()
    Company_Code = models.PositiveIntegerField()
