from django.urls import path
from . import views
from .views import *
app_name="tracking"

urlpatterns = [  
path("",Orders.as_view(),name="home"),
path("create/",OrderCreate.as_view(),name="create"),
path("details/<str:id>/",OrderDetails.as_view(),name="details"),
path("order/confirm/<str:id>/",views.order_confirm,name="confirm"),
path("order/update/<str:id>/",views.order_location_update,name="update"),
path("order/delivered/<str:id>/",views.order_deliver,name="close"),
  

path("test/",views.test,name="test"),

]
                  
                  
