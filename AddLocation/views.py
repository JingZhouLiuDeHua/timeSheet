from django.shortcuts import render
from .models import User
# Create your views here.
def viewUsers(request):
    users = User.objects.all()
    return render(request, 'usertable.html', {'users': users})

