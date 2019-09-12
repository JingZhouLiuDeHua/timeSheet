from django.shortcuts import render, redirect
from .models import Report

# Create your views here.

def addreport(request):
    if request.method == 'POST':
        locate = request.POST.get('Location')
        sec = request.POST.get('Sector')
        rep = Report.objects.create(Location=locate,Sector=sec)
        #doc = models.Doctor.objects.create(First_name="a", Last_name="y", FileNumber=1)
        #user = models.User.objects.create(First_name="tao", Last_name="yan", Description="doctor",LoginIDOrEmail="doctor@gmail.com",Authority=0,Password="abc",RetypePassword="abc")
        rep.save()
        return redirect('/timecard/')
    #print("request.method==POST not called")
    return render(request,'add_location.html')

def showReport(request):
    all_objects = Report.objects.all()
    context = {'all_objects': all_objects}
    return render(request, 'TimeCard.html', context)
