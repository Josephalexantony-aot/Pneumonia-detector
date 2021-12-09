"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index, name='index'),
    path('status_update/', views.status_update, name='status_update'),
    path('failed/', views.failed, name='failed'),
    path('valuedisplay/',views.valuedisplay, name='valuedisplay'),
    path('view_doctors/', views.view_doctors, name='view_doctors'),
    path('home/',views.home, name='home'),
    path('admin/',views.admin, name='admin'),
    path('view_patients/',views.view_patients, name='view_patients'),
    path('admin_view_patients/',views.admin_view_patients, name='admin_view_patients'),
    path('patientRegistration/', views.patientRegistration, name='patientRegistration'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('',views.guesthome, name='guesthome'),
    path('doctorregister/',views.doctorregister, name='doctorregister'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('home/',views.home, name='home'),
    path('signout/',views.signout, name='signout'),
    path('hotel_image_view/',views.hotel_image_view, name = 'hotel_image_view'), 
    path('success/', views.success, name = 'success'), 
    path('display_hotel_images/',views.display_hotel_images, name = 'display_hotel_images'),
    #..............
    path('readmore/',views.readmore, name='readmore'),
    path('home_doctor/', views.home_doctor, name='home_doctor'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)
