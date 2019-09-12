from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from AddDoctor import models


def searchDoctor(request):
    query = request.GET.get('First_name', 'Last_name', 'FileNumber')

    if query:
        results = Doctor.objects.filter(name_icontains=query).distinct()
    else:
        results = []
    return render(request, {'results': results}, template_name= 'list_doctors.html')