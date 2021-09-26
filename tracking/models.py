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
from rest_auth.models import TokenModel
# Create your models here.   

def upload_image(instance,filename,**kwargs):
    try:    
        title=instance.title
        dest=f"category/{instance.title}/{filename}"
    except:
        title=instance.price
        dest=f"prodcuts/{instance.title}/{filename}"
    return dest
   


class Image(models.Model):
    image=models.ImageField(upload_to=upload_image)

class Category(models.Model):
    title=models.CharField(max_length=50)
    image=models.ManyToManyField(Image)
    
    def __str__(self):
        return self.title

class Product(models.Model):    
    title=models.CharField(max_length=50)
    image=models.ManyToManyField(Image)
    price=models.PositiveIntegerField(default=0)
    quantity=models.PositiveIntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.TextField()
    
    def __str__(self):
        return self.title

@receiver(post_delete,sender=Product)
def submission_delete(sender,instance,*args,**kwargs):
    instance.image.delete(False)   

@receiver(post_delete,sender=Category)
def submission_delete(sender,instance,*args,**kwargs):
    instance.image.delete(False)   

class Address(models.Model):
    name=models.CharField(max_length=120)
    lat_lng=models.CharField(max_length=100)
    account=models.ForeignKey(Account,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Shop(models.Model):
    name=models.CharField(max_length=100)
    address=models.ManyToManyField(Address) 

    def __str__(self):    
        return self.name  

    
class Product_Cart(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)
    ordered=models.BooleanField(default=False)
    delivered=models.BooleanField(default=False)
    def __str__(self):
        return (self.user.name.username)

    
class Cart(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    product=models.ManyToManyField(Product_Cart)
    ordered=models.BooleanField(default=False)
    delivered=models.BooleanField(default=False)
    def __str__(self):
        return (self.user.name.username)


class Order(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True,blank=False)   
    place=models.CharField(max_length=300,blank=True,null=True)
    shop=models.ForeignKey(Shop,on_delete=models.SET_NULL,null=True,blank=False)
    ordered=models.BooleanField(default=False)
    delivered=models.BooleanField(default=False)

    # shop=   
    def __str__(self):
        return (f"order-{self.id}")
    
    
class Test(models.Model):
    lat_lng = models.CharField(max_length=100)
    image=models.ImageField()
    def __str__(self):
        return self.lat_lng
