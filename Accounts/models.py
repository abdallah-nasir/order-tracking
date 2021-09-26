from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token 
# Create your models here.


def upload_image(instance,filename,**kwargs):
    return f"accounts/{instance.name.username}/{instance.type}-{filename}" 
CHOICES=(
    ("Driver","Driver"),
    ("Customer","Customer"),
    ("Supplier","Supplier")
)

@receiver(post_save,sender=User)
def create_account(sender,instance,created,**kwargs):
    if created:
        Account.objects.create(name=instance)
        try:
            Token.objects.get(user=instance)
        except:
            Token.objects.create(user=instance)
class Account(models.Model):
    name=models.OneToOneField(User,on_delete=models.CASCADE)
    trade_name=models.CharField(max_length=50,blank=True,null=True)
    image=models.ImageField(upload_to=upload_image)
    type=models.CharField(choices=CHOICES,max_length=20)
    phone=models.CharField(max_length=15,blank=True)
    def __str__(self):
        return self.name.username
    
    
@receiver(post_delete,sender=Account)
def submission_delete(sender,instance,*args,**kwargs):
    instance.image.delete(False)   
    