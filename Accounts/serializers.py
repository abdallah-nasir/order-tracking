from rest_framework import serializers     
from rest_framework.serializers import(     
HyperlinkedIdentityField,ModelSerializer,SerializerMethodField,ValidationError)
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
import os
CHOICES=(    
    ("Driver","Driver"),
    ("Customer","Customer"),
    ("Supplier","Supplier")
)
 
class CustommerRegisterSerializer(RegisterSerializer):
    email=serializers.EmailField(required=True)
    image=serializers.ImageField(required=True)      
    def get_cleaned_data(self):
        super(CustommerRegisterSerializer,self).get_cleaned_data()
        return {
            'email': self.validated_data.get('email',""),
            'password1': self.validated_data.get('password1',""),
            'image': self.validated_data.get('image',"")    
        }
    def validate_image(self,value):
        size=value.size / (1024 * 1024)
        type=os.path.splitext(value.name)[1]

        if size > 2 or type != ".jpg":
            raise ValidationError("image size is more than (2Mb)") 
    def save(self, request):
        user = super().save(request)
        user.username=self.data.get("username")
        user.first_name=self.data.get("username")
        user.save()
        myacount=user.account
        myacount.type="Customer"
        myacount.image=request.FILES["image"]   
        myacount.save()
  
        return user          

class SupplierRegisterSerializer(RegisterSerializer):
    email=serializers.EmailField(required=True)
    image=serializers.ImageField(required=True)      
    trade_name=serializers.CharField(required=True)
    def get_cleaned_data(self):    
        super(SupplierRegisterSerializer,self).get_cleaned_data()
        return {
            'trade_name': self.validated_data.get('trade_name',""),
            'username': self.validated_data.get('username',""),
            'email': self.validated_data.get('email',""),
            'password1': self.validated_data.get('password1',""),
            'image': self.validated_data.get('image',"")    
        }
    def validate_image(self,value):
        size=value.size / (1024 * 1024)
        type=os.path.splitext(value.name)[1]

        if size > 2 or type != ".jpg":
            raise ValidationError("image size is more than (2Mb)") 
    def save(self, request):
        user = super().save(request)
        user.username=self.data.get("username")
        user.first_name=self.data.get("username")
        user.save()
        myaccount=user.account
        myaccount.type='Supplier'
        myaccount.trade_name=self.data.get("trade_name")
        myaccount.image=request.FILES["image"]   
        myaccount.save()
        return user      
   
class DriverRegisterSerializer(RegisterSerializer):
    email=serializers.EmailField(required=True)
    image=serializers.ImageField(required=True)      
    def get_cleaned_data(self):
        super(DriverRegisterSerializer,self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username',""),
            'email': self.validated_data.get('email',""),
            'password1': self.validated_data.get('password1',""),
            'image': self.validated_data.get('image',"")    
        }
    def validate_image(self,value):
        size=value.size / (1024 * 1024)
        type=os.path.splitext(value.name)[1]

        if size > 2 or type != ".jpg":
            raise ValidationError("image size is more than (2Mb)") 
    def save(self, request):
        user = super().save(request)
        user.username=self.data.get("username")
        user.first_name=self.data.get("username")
        user.save()
        myacount=user.account
        myacount.type='Driver'
        myacount.image=request.FILES["image"]   

        myacount.save()
        return user   