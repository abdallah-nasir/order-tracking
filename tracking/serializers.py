from rest_framework import serializers     
from .models import *
from rest_framework.serializers import(     
HyperlinkedIdentityField,ModelSerializer,SerializerMethodField,ValidationError)

import os


order_detail_url = HyperlinkedIdentityField(view_name='home:details',lookup_field="id")
class PlaceSerializer(serializers.ModelSerializer):
    url=order_detail_url    
    user=SerializerMethodField("get_username")
    # shop=SerializerMethodField("get_shop")
    class Meta:
        model = Order
        fields="__all__"
        # exclude = ('search',)
        extra_kwargs={"user":{"read_only":True},"ordered":{"read_only":True},"place":{"read_only":True}}
  
    def get_username(self,order):
        username=order.user.name.username
        return (username)
    

class OrderSerializer(serializers.ModelSerializer):
    shop=SerializerMethodField("get_shop")
    user=SerializerMethodField("get_username")

    class Meta:         
        model = Order
        fields="__all__"
        read_only_fields = ('user', 'delivered',"shop","address","lat_lng","place")
        extra_kwargs={"ordered":{"required":True}}   
    def get_username(self,order):       
        username=order.user.name.username
        return (username)
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields["order"].queryset = Order.objects.filter(ordered=False,delivered=False)
    def get_shop(self,order):
        name=order.shop.name   
        return (name)
    
    
class OrderUpdateSerializer(serializers.ModelSerializer):
    shop=SerializerMethodField("get_shop")   
    user=SerializerMethodField("get_username")
    class Meta:
        model = Order
        fields="__all__"
        read_only_fields = ('user', 'delivered',"shop","address","ordered","place")
        extra_kwargs={"lat_lng":{"required":True}}  
    
    def get_username(self,order):       
        username=order.user.name.username
        return (username)
    def get_shop(self,order):   
        name=order.shop.name   
        return (name)
    
class OrderCloseSerializer(serializers.ModelSerializer):
    shop=SerializerMethodField("get_shop")   
    user=SerializerMethodField("get_username")
    class Meta:
        model = Order
        fields="__all__"
        read_only_fields = ('user', 'lat_lng',"shop","address","ordered","place")
        extra_kwargs={"delivered":{"required":True}}  
    
    def get_username(self,order):       
        username=order.user.name.username
        return (username)
    def get_shop(self,order):   
        name=order.shop.name   
        return (name)
    
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields="__all__"
  

    def validate_image(self,value):
        image_size = value.size / (1024*1024)  #megabytes
        image_type=os.path.splitext(value.name)[1]
        print(value.path)
        if image_size > 2.0 or image_type == ".jpg":
            raise ValidationError("image type or size is unvalid")
        return value
    
    

