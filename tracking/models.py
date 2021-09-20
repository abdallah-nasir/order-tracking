# from django.contrib.gis.db import models
from django.db import models
from Accounts.models import *
# from django.contrib.gis.geos import Point
# from location_field.models.spatial import LocationField
# from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save,post_delete
from django.utils.text import slugify
from django.dispatch import receiver

# Create your models here.   



class Shop(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    lat_lng=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    address = models.CharField(max_length=255) #optinal
    lat_lng = models.CharField(max_length=100,blank=True,null=True)
    shop=models.ManyToManyField(Shop)
    ordered=models.BooleanField(default=False)
    delivered=models.BooleanField(default=False)

    # shop=
    def __str__(self):
        return (f"order-{self.id}")
    
class Driver(models.Model):
    user=models.ForeignKey(Account,default=1,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    my_location=models.CharField(max_length=100) #(lat,lng) only
    def __str__(self):
        return str(self.order.id)
    
    
class Test(models.Model):
    lat_lng = models.CharField(max_length=100)

    def __str__(self):
        return self.lat_lng
