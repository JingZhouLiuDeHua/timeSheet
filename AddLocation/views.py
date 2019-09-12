from django.shortcuts import render, redirect
from .models import Location


def add_location(request):
    if request.method == 'POST':
        locate = request.POST.get('Location')
        sec = request.POST.get('Sector')
        loc = Location.objects.create(Location=locate,Sector=sec)
        #doc = models.Doctor.objects.create(First_name="a", Last_name="y", FileNumber=1)
        #user = models.User.objects.create(First_name="tao", Last_name="yan", Description="doctor",LoginIDOrEmail="doctor@gmail.com",Authority=0,Password="abc",RetypePassword="abc")
        loc.save()
        return redirect('/location_list/')
    #print("request.method==POST not called")
    return render(request,'add_location.html')

def showLocation(request):
    all_objects = Location.objects.all()
    context = {'all_objects': all_objects}
    return render(request, 'location_list.html', context)

# Create your views here.

