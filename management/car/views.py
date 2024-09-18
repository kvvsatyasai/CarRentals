from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *


# Create your views here.
def home(request):
    return render(request, 'car/home.html')

def Try(request):
    return render(request, 'car/BookingDetails.html')

def contact(request):
    return render(request, 'car/ContactUs.html')

def admin(request):
    if request.method == 'POST':
        u = Customer.objects.all()
        print(u)
        username = request.POST.get('username')
        password = request.POST.get('pass')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Redirecting to try page")  
            return redirect('BookingDetails')
        else:
            messages.error(request,'Invalid Username or Password')

    return render(request, 'car/AdminLogin.html')

