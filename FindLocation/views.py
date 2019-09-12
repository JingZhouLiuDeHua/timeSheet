from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from AddLocation import models


def searchLocation(request):
    query1 = request.GET.get('Location')
    query2 = request.Get.get('Sector')
    if method == 'POST':
        if query1:
            results = Location.objects.filter(name_icontains=query1).distinct()
        elif query2:
            results = Location.objects.filter(name_icontains=query2).distinct()
        else:
            results = []

    return render(request, {'results': results}, template_name= 'location_list.html')

