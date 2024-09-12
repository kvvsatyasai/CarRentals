from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # New URL pattern for the homepage

]
