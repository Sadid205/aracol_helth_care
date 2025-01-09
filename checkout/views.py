from django.shortcuts import render
from .models import Checkout
from rest_framework.viewsets import ModelViewSet
from .serializer import CheckoutModelSerializer
from cart.models import Cart
from rest_framework.response import Response
from rest_framework import status
from medicine.models import Medicine
from medicine.serializer import MedicineSerializer
# Create your views here.


class CheckoutModelViewset(ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutModelSerializer
    lookup_field = 'pk'

    def create(self,request,*args,**kwargs):
        existing_cart_object = None
        try:
            existing_cart_object = Cart.objects.get(id=5)
        except Cart.DoesNotExist:
            return Response({"failed":"This cart dosen't exist!"},status=status.HTTP_404_NOT_FOUND)
        if existing_cart_object is not None:
            total_amount = 0
            all_medicine = existing_cart_object.medicine.all()
            for medicine in all_medicine:
                total_amount+=medicine.price
            serialized_all_medicine = MedicineSerializer(all_medicine,many=True).data
            existing_cart_object.medicine.clear()
            return Response({"purchased_medicine":serialized_all_medicine,"paid":f"{total_amount} Taka"})

