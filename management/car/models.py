from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=70,blank=True)
    email = models.CharField(max_length=50,blank=True)
    password = models.CharField(max_length=30,blank=True)
    
    def __str__(self):
        return f'{self.name}'
    
    
class Cars(models.Model):
    mode = (('PERSONAL DELIVERY = Extra 500','PERSONAL DELIVERY = Extra 500'),('SELF','SELF'))
    id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=70,blank=True)
    color = models.CharField(max_length=70,blank=True)
    price = models.CharField(max_length=10)
    delivery = models.CharField(max_length=50, choices=mode,default='SELF')
    
    def __str__(self):
        return self.model_name
    

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Cars,on_delete=models.CASCADE)
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=10,default='null')
    aadhar = models.FileField(blank=True,upload_to='docs/',null=False)
    driving_license = models.FileField(blank=True,upload_to='docs/',null=False)
    location = models.CharField(max_length=50,blank=True)
    time = models.TimeField(default=timezone.now) 
    
    
    def __str__(self):
        return f'{self.car} - {self.customer}' 
    
    
    
