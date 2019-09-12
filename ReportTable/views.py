from django.shortcuts import render, redirect
from .models import Report

# Create your views here.

from django.shortcuts import render,redirect

# Create your views here.
from ReportTable import models
from .models import Report


def showthis(request):
    all_objects = Report.objects.all()
    context = {'all_objects': all_objects}
    return render(request, 'report_list.html', context)

def add_report(request):
    if request.method == 'POST':
        Doctor_name = request.POST.get('Doctor_name')
        FileNumber = request.POST.get('FileNumber')
        Location =request.POST.get('Location')
        Sector = request.POST.get('Sector')
        Work_Date = request.POST.get('Work_Date')
        Time_In = request.POST.get('Time_In')
        Time_Out = request.POST.get('Time_Out')
        Hours_Worked = request.POST.get('Hours_Worked')
        Hours_Code = request.POST.get('Hours_Code')
        Report_Date = request.POST.get('Report_Date')
        Batch_ID = request.POST.get('Batch_ID')
        Company_Code = request.POST.get('Company_Code')
        report = models.Report.objects.create(Doctor_name=Doctor_name, FileNumber=FileNumber, Location=Location,Sector=Sector,Work_Date=Work_Date,Time_In=Time_In,Time_Out=Time_Out,Hours_Worked=Hours_Worked,Hours_Code=Hours_Code,Report_Date=Report_Date,Batch_ID=Batch_ID,Company_Code=Company_Code)
        report.save()
        return redirect('/report_list/')
    #print("request.method==POST not called")
    return render(request,'add_report.html')

def showReport(request):
    all_objects = Report.objects.all()
    context = {'all_objects': all_objects}
    return render(request, 'TimeCard.html', context)
