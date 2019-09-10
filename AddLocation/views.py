from django.shortcuts import render,redirect
from AddLocation import models

# Create your views here.
def location_list(request):
    location=models.Location.objects.all()
    return render(request,'location_list.html',{'location_list':location})



def add_location(request):
    if request.method == 'POST':
        Location = request.POST.get('Location')
        Sector = request.POST.get('Sector')
        location=models.Location.objects.create(Location=Location,Sector=Sector)
        #doc = models.Doctor.objects.create(First_name="a", Last_name="y", FileNumber=1)
        #user = models.User.objects.create(First_name="tao", Last_name="yan", Description="doctor",LoginIDOrEmail="doctor@gmail.com",Authority=0,Password="abc",RetypePassword="abc")
        location.save()
        return redirect('/location_list/')
    #print("request.method==POST not called")
    return render(request,'add_location.html')