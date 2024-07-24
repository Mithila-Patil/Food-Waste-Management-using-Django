from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('donor/', views.donor, name='donor'),
    path('receiver/', views.receiver, name='receiver'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('foodid/', views.foodid, name='foodid'),
    path('formdonor/', views.formdonor, name='formdonor'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

admin.site.site_header="Food Waste Management"
admin.site.index_title="DASHBOARD"
