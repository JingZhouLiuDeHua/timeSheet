from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from AddLocation import models


def searchLocation(request):
    template_name = 'base_template.html'
    query = request.GET.get('Location', 'Sector')

    if query:
        results = Location.objects.filter(name_icontains=query).distinct()
    else:
        results = []
    return render(request, template_name, {'results': results})
