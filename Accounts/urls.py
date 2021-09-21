from django.urls import path
from . import views
from .views import *
app_name="Accounts"

urlpatterns = [ 
path("",CustomSignUPView.as_view(),name="home"),

]
                  
                  
                  