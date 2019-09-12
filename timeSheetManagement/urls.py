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
from django.urls import path, include
from django.conf.urls import url
from AddDoctor.views import show_doctors, add_doctor
from AddLocation.views import add_location, showLocation
from AddUser.views import add_user, user_list
from ReportTable.views import showReport
from django.views.generic.base import TemplateView
from LoginLogout import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^doctor_list/', show_doctors, name='show_doctor_list'),
    url(r'^add_doctor/',  add_doctor, name='add_doctor_form'),
    url(r'^register/', add_user, name='add_user_form'),
    url(r'^user_list/', user_list, name='show_user_list'),
    url(r'^location_list/', showLocation, name='show_location_list'),
    url(r'^add_location/', add_location, name='add_location_form'),
    path('', views.login_request, name='login_page'),
    path('timecard/', showReport, name='show_time_card'),
]