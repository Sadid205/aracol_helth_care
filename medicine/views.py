# Create your views here.
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from .models import Medicine
from .serializer import MedicineSerializer


class MedicineModelViewSet(ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    lookup_field = "pk"
