from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from AddDoctor import models
from .models import Doctor



# Create your views here.

def doctor_list(request):
    doctor=models.Doctor.objects.all()
    return render(request,'doctor_list.html',{'doctor_list':doctor})

def try_this(request):
    all_objects = Doctor.objects.all()
    context = {'all_objects': all_objects}
    return render(request, 'list_doctors.html', context)

def showthis(request):
    all_objects = Doctor.objects.all()
    context = {'all_objects': all_objects}
    return render(request, 'doctor_list.html', context)



def doctors_from_db(request):
    doctors_list=Doctor.objects.all()
    return render(request,'doctor_list.html',{'doctors':doctors_list})


def add_doctor(request):
    if request.method == 'POST':
        First_name = request.POST.get('First_name')
        Last_name = request.POST.get('Last_name')
        FileNumber =request.POST.get('FileNumber')
        print(First_name)
        print(Last_name)
        print(FileNumber)
        doc=models.Doctor.objects.create(First_name=First_name,Last_name=Last_name,FileNumber=FileNumber)
        #doc = models.Doctor.objects.create(First_name="a", Last_name="y", FileNumber=1)
        #user = models.User.objects.create(First_name="tao", Last_name="yan", Description="doctor",LoginIDOrEmail="doctor@gmail.com",Authority=0,Password="abc",RetypePassword="abc")
        doc.save()
        return redirect('/doctor_list/')
    #print("request.method==POST not called")
    return render(request,'add_doctor.html')