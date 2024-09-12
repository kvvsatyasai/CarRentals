from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('adminlog/', views.admin, name='adminlog'),
    
    path('BookingDetails/', views.Try, name='BookingDetails'),
    path('contact/', views.contact, name='contact'),
     
]
