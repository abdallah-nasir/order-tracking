from django.shortcuts import render
from rest_framework.serializers import Serializer
from .models import *
import requests
from .forms import *
from .serializers import *    
from rest_framework.permissions import(IsAuthenticated,IsAuthenticatedOrReadOnly,
                                       AllowAny,)
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view,permission_classes,authentication_classes

from rest_framework.generics import ListCreateAPIView,ListAPIView, RetrieveAPIView,RetrieveUpdateAPIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
# from django.contrib.gis.geos import Point

# Create your views here.

# from geopy.geocoders import Nominatim
import json
# geolocator = Nominatim(user_agent="tracking")
api="d611419749b667a306600e1772193619"
google="AIzaSyCzhBefcZf1envB4TrkOs-xsXR7ldFS3XI"

# def order_create(request):


class Orders(ListAPIView):
    queryset=Order.objects.all()             
    serializer_class=PlaceSerializer 
    
class OrderDetails(RetrieveAPIView):             
    queryset=Order.objects.all()                    
    serializer_class=PlaceSerializer    
    lookup_field="id" 
    
class OrderCreate(ListCreateAPIView):             
    queryset=Order.objects.all()                 
    serializer_class=PlaceSerializer        
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]          
    def perform_create(self,serializer): 
        if serializer.is_valid():    
            print("valid")
            lat_lng= serializer.initial_data["lat_lng"]  
            query=serializer.initial_data["address"]  
            shop=serializer.initial_data["shop"]   
            # search=serializer.initial_data["place"]
            url=requests.get(f"http://api.positionstack.com/v1/forward?access_key={api}&query={query}")
            results_1=url.json() 
            url_2=requests.get(f"http://api.positionstack.com/v1/reverse?access_key={api}&query={lat_lng}")
            # url_2=requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat_lng}&key={google}") #reverse lat,lng
            results_2=url_2.json()
            filters={}
            for i in results_2["data"]:
                if i["country"] == "Egypt": 
                    filters["country"] = i["country"]
                    filters["region"]= i["region"]          
                    filters["lattitude"] = i["latitude"]
                    filters["longitude"]=i["longitude"]
            filters=json.dumps(filters,indent = 4)
            my_json=json.loads(filters)    
            lat=my_json["lattitude"]        
            lng=my_json["longitude"]  
            lat_lng=f"{lat},{lng}" 
            
            serializer.save(user=self.request.user.account,place=f'{results_1["data"][0]["street"]},{results_1["data"][0]["name"]}')
            message={"message":my_json,status:status.HTTP_201_CREATED}   
        else:
            message={serializer.errors}
        return Response(message)    


@api_view(["PUT"])
@permission_classes((IsAuthenticated,))        
@authentication_classes((TokenAuthentication,))
def order_confirm(request,id):
    try:
        order=Order.objects.get(id=id,ordered=False,delivered=False)
        if request.user.account.type == "Driver":
            serializer=OrderSerializer(order,data=request.data)
            if serializer.is_valid():
                serializer.save()   
                message={"message":"order is updated","order":serializer.data,"status":status.HTTP_201_CREATED}
            else:
                message=(serializer.errors)
            return Response(message)
   
        else:         
            message={"message":"you are not a driver","status":status.HTTP_403_FORBIDDEN}
            return Response(message)

    except Order.DoesNotExist:    
        message={"message":"invalid order","status":status.HTTP_404_NOT_FOUND}   

        return Response(message)

@api_view(["PUT"])
@permission_classes((IsAuthenticated,))     
@authentication_classes((TokenAuthentication,))
def order_location_update(request,id):
    try:
        order=Order.objects.get(id=id,ordered=True,delivered=False)
        serializer=OrderUpdateSerializer(order,data=request.data)
        if serializer.is_valid(): 
            serializer.save()   
            message={"message":"order is updated","order":serializer.data,"status":status.HTTP_201_CREATED}
        else:
            message=(serializer.errors)
        return Response(message)  
    except Order.DoesNotExist:    
        message={"message":"invalid order","status":status.HTTP_404_NOT_FOUND}
        return Response(message)  

@api_view(["PUT"])
@permission_classes((IsAuthenticated,))         
@authentication_classes((TokenAuthentication,))          
def order_deliver(request,id):
    try:   
        order=Order.objects.get(id=id,ordered=True,delivered=False)
        serializer=OrderCloseSerializer(order,data=request.data)
        if serializer.is_valid():    
            print("valid")
            serializer.save()   
            message={"message":"order is delivered","order":serializer.data,"status":status.HTTP_201_CREATED}
        else:   
            message=(serializer.errors)
        return Response(message)     

    except Order.DoesNotExist:       
        message={"message":"invalid order","status":status.HTTP_404_NOT_FOUND}
        return Response(message)     
  
@api_view(["GET","POST"])
def test(request):
    if request.method == 'POST':
        serializer=TestSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method == "GET":
        search=request.GET.get("qs")
        query=Test.objects.filter(Q(lat_lng__icontains=search)) 
        print(query)
        serializer=TestSerializer(query,many=True)
        data={"count":query.count(),"data":serializer.data}
        return Response(data)
    