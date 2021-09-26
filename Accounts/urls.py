from django.urls import path
from . import views
from .views import *
app_name="Accounts"

urlpatterns = [ 
path("supplier/",SupplierSignUPView.as_view(),name="home"),
path("driver/",DriverSignUPView.as_view(),name="driver"),
path("customer/",CustommerSignUPView.as_view(),name="customer"),

]
              
                  
                  