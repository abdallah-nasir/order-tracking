from django.shortcuts import render
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer
from .models import Account
# Create your views here.

class CustomSignUPView(RegisterView):
    serializer_class=CustomRegisterSerializer

    def create(self,serializer):
        serializer=CustomRegisterSerializer(data=self.request.data)
        if serializer.is_valid():
            image=serializer.initial_data['image']
            serializer.save(self.request)
            account=Account.objects.get(name=serializer["username"])
            account.image=image
            account.save()
                
    def get_response(self):
        orginal_response = super().get_response()  
        mydata = {"message": "some message", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response
 
 