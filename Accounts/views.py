from django.shortcuts import render
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from .serializers import * 
from .models import Account

# Create your views here.

class SupplierSignUPView(RegisterView):
    serializer_class=SupplierRegisterSerializer

    def create(self,serializer):
        serializer=SupplierRegisterSerializer(data=self.request.data)
        if serializer.is_valid():
            # image=serializer.initial_data['image']
            serializer.save(self.request)
            # account=Account.objects.get(name=serializer["username"])
            # account.image=image
            # account.save()
            # serializer.save
            message={"message":"done"}
        else:    
            message=(serializer.errors)   
        return Response(message)
    def get_response(self):
        orginal_response = super().get_response()  
        mydata = {"message": "some message", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response

class CustommerSignUPView(RegisterView):
    serializer_class=CustommerRegisterSerializer

    def create(self,serializer):
        serializer=CustommerRegisterSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save(self.request)
            message={"message":"done"}
        else:    
            message=(serializer.errors)   
        return Response(message)
    def get_response(self):
        orginal_response = super().get_response()  
        mydata = {"message": "some message", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response
 
 
class DriverSignUPView(RegisterView):
    serializer_class=DriverRegisterSerializer

    def create(self,serializer):
        serializer=DriverRegisterSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save(self.request)
            message={"message":"done"}
        else:    
            message=(serializer.errors)   
        return Response(message)     
    def get_response(self):
        orginal_response = super().get_response()  
        mydata = {"message": "some message", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response
 