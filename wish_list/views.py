from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import WishList
from .serializer import WishListModelSerializer
from medicine.models import Medicine
from medicine.serializer import MedicineSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class WishListModelViewset(ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListModelSerializer
    lookup_field = 'pk'

    def create(self,request,*args,**kwargs):
        medicine_ids = request.data.get("medicine")
        wish_list_object = None
        if len(WishList.objects.all())==1:
            wish_list_object = WishList.objects.get(id=1)
        else:
            wish_list_object = WishList.objects.create()
        
        
        medicines_list = Medicine.objects.filter(id__in=medicine_ids)
        wish_list_object.medicine.add(*medicines_list)

        serializer = WishListModelSerializer(wish_list_object)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def destroy(self,request,*args,**kwargs):
        medicine_ids = request.data.get("medicine")
        wish_list_object = WishList.objects.get(id=1)
        medicines_list = Medicine.objects.filter(id__in=medicine_ids)
        wish_list_object.medicine.remove(*medicines_list)
        serializer = WishListModelSerializer(wish_list_object)
        return Response(serializer.data,status=status.HTTP_200_OK)
    


