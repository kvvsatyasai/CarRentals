from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
     path('drive/', views.Drive, name='drive'),
    path('adminlog/', views.admin, name='adminlog'),
    path('register/', views.SignUp, name='register'),  
    path('contact/', views.contact, name='contact'),
    path('bookform/', views.bookingform, name='bookform'),
    path('details/',views.details,name='DET'),
    path('intro', views.intro,name='INT'),
    path('logout', views.handleLogout,name='logout'),
    path('addCar', views.addCar,name='addCar'),
    path('profile', views.profile,name='profile'),
     
]   
