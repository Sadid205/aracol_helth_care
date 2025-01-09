from django.shortcuts import render
from .serializer import CategoryModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Category
# Create your views here.

class CategoryModelViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = "pk"
