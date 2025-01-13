from django.db import models
from django.contrib.auth.models import User
from .patient_choices import GENDER,BLOOD_GROUPS,ROLE

# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="patient")
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    image = models.URLField(max_length=500,null=True,blank=True)
    gender = models.CharField(max_length=10,choices=GENDER,null=True,blank=True)
    date_of_birth = models.DateField(blank=True,null=True)
    district = models.CharField(max_length=100,null=True,blank=True)
    sub_district = models.CharField(max_length=100,null=True,blank=True)
    union_pourashava_ward = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=14,blank=False,null=False)
    email = models.EmailField(max_length=50,blank=True,null=True)
    profession = models.CharField(max_length=50,null=True,blank=True)
    height_feet = models.PositiveIntegerField(blank=True,null=True)
    height_inches = models.PositiveIntegerField(blank=True,null=True)
    weight = models.PositiveIntegerField(blank=True,null=True)
    blood_group = models.CharField(max_length=10,choices=BLOOD_GROUPS,blank=True,null=True)
    aracol_app_point = models.PositiveIntegerField(default=0,null=True,blank=True)
    recently_viewed_profile = models.ManyToManyField("doctor.Doctor",related_name="viewed_by",blank=True)
    referral_unique_code = models.CharField(max_length=10,blank=True,null=True)
    total_registration_by_refer = models.PositiveIntegerField(blank=True,null=True,default=0) 
    successfull_referrals = models.PositiveIntegerField(null=True,blank=True,default=0)
    rewards_received = models.PositiveIntegerField(null=True,blank=True,default=0)
    role = models.CharField(choices=ROLE,default="patient",max_length=20)
    def __str__(self):
        return f"{self.first_name} {self.last_name}."