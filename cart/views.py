from django.shortcuts import render
from .models import Cart
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializer import CartModelSerializer
# Create your views here.

class CartModelViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartModelSerializer
    lookup_field = "pk"
  
