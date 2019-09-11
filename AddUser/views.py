from django.shortcuts import render,redirect
from AddUser import models

# Create your views here.
def user_list(request):
    user=models.User.objects.all()
    return render(request,'user_list.html',{'user_list':user})



def add_user(request):
    if request.method == 'POST':
        First_name = request.POST.get('First_name')
        Last_name = request.POST.get('Last_name')
        Description =request.POST.get('Description')
        LoginIDOrEmail = request.POST.get('LoginIDOrEmail')
        Authority = request.POST.get('Authority')
        Password = request.POST.get('Password')
        RetypePassword = request.POST.get('RetypePassword')
        #doc = models.Doctor.objects.create(First_name="a", Last_name="y", FileNumber=1)
        user = models.User.objects.create(First_name=First_name, Last_name=Last_name, Description=Description,LoginIDOrEmail=LoginIDOrEmail,Authority=Authority,Password=Password,RetypePassword=RetypePassword)
        user.save()
        return redirect('/user_list/')
    #print("request.method==POST not called")
    return render(request,'add_user.html')