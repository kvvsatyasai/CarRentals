from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
import uuid
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Redirecting to try page")  
            return redirect('home')
        else:
            messages.error(request,'Invalid Username or Password')
            
    return render(request, 'car/AdminLogin.html')


def SignUp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        em = request.POST.get('em')
        pa1 = request.POST.get('p1')
        pa2 = request.POST.get('p2')
        print(name,em,pa1,pa2)
        if pa1 != pa2:
            return HttpResponse('password didnot matched')
        user = User.objects.create_user(name,em,pa1)
        
        user.save()
        return render(request,'car/AdminLogin.html')
    else:
       return render(request, 'car/signup.html')


def intro(request):
    return render(request,'car/intro.html')


def home(request):
    cars = Cars.objects.all()
    # for c in cars:
    #     print(c.model_name)
    #     print(c.color)
    print(cars)
    return render(request, 'car/home.html')
def Drive(request):
    return render(request, 'car/drive.html')

def Try(request):
    return render(request, 'car/BookingDetails.html')

def contact(request):
    return render(request, 'car/ContactUs.html')



@login_required(login_url='/login/')
def bookingform(request):
    return render(request, 'car/form.html')






def details(request):
    user_code = str(uuid.uuid4()).replace("-", "")[:8]  # 8-character alphanumeric string
    print(user_code)
    # print(user_code)
    
    
    return HttpResponse('Show time.....')

