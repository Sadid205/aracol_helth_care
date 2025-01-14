from django.shortcuts import render
from .serializer import DoctorSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Doctor
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class DoctorFilter(filters.FilterSet):
    first_name = filters.CharFilter(field_name="first_name",lookup_expr="icontains")
    last_name = filters.CharFilter(field_name="last_name",lookup_expr="icontains")
    specialization = filters.CharFilter(field_name="specialization",lookup_expr="icontains")
    doctor_code = filters.CharFilter(field_name="doctor_code",lookup_expr="icontains")
    depertment = filters.CharFilter(field_name="depertment",lookup_expr="icontains")

    class Meta:
        model = Doctor
        fields = ['first_name','last_name','specialization','doctor_code','depertment']

class DoctorModelViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DoctorFilter
    lookup_field = "pk"

    # def list (self,request,*args,**kwargs):


