from django.shortcuts import render
from .models import Cart
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializer import CartModelSerializer
from medicine.models import Medicine
# Create your views here.

class CartModelViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartModelSerializer
    lookup_field = "pk"

    def create(self,request,*args,**kwargs):
        medicine_ids = request.data.get("medicine")
        cart_object = None
        if len(Cart.objects.all())==1:
            cart_object = Cart.objects.get(id=5)
        else:
            cart_object = Cart.objects.create()
        
        medicines = Medicine.objects.filter(id__in=medicine_ids)
        cart_object.medicine.add(*medicines)

        serializer = CartModelSerializer(cart_object)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def destroy(self,request,*args,**kwargs):
        medicine_ids = request.data.get("medicine")
        cart_object = Cart.objects.get(id=5)
        medicines = Medicine.objects.filter(id__in=medicine_ids)
        cart_object.medicine.remove(*medicines)
        serializer = CartModelSerializer(cart_object)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
