"""timeSheetManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from AddDoctor import views
from AddLocation import views
from AddUser import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    # url(r'^doctor_list/', views.showthis),
    # url(r'^add_doctor/',  views.add_doctor),
    #url(r'^doctors_from_db$',views.doctors_from_db,name='doctors_from_db'),
    #url(r'^doctor_list/',views.doctors_from_db),
    #url(r'^add_user/', views.add_user),
    # url(r'^location_list/', views.showLocation),
   # url(r'^add_location/', views.add_location),
    url(r'^add_user/', views.add_user),
    url(r'^user_list/', views.user_list),
]
