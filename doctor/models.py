from django.db import models
from django.contrib.auth.models import User
from .doctor_choices import GENDER,DOCTOR_TYPE,DAYS,STATUS

# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="doctor")
    degree = models.CharField(max_length=100,null=True,blank=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    image = models.URLField(max_length=500,null=True,blank=True)
    depertment = models.CharField(max_length=200,null=True,blank=True)
    total_experience = models.IntegerField(null=True,blank=True)
    doctor_type = models.CharField(choices=DOCTOR_TYPE,null=True,blank=True,max_length=30)
    bmdc_number = models.CharField(max_length=10,null=True,blank=True)
    date_of_birth = models.DateField(blank=True,null=True)
    gender = models.CharField(choices=GENDER,blank=True,null=True,max_length=10)
    district = models.CharField(max_length=100,blank=True,null=True)
    area_thana = models.CharField(max_length=100,blank=True,null=True)
    nid_passport_number = models.CharField(max_length=18,null=True,blank=True)
    registration_number = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=15,null=False,blank=False)
    email = models.EmailField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=200,blank=True,null=True)
    instance_consultation_start_time = models.TimeField(auto_now=False,auto_now_add=False)
    instance_consultation_end_time = models.TimeField(auto_now=False,auto_now_add=False)
    instance_consultation_start_day = models.CharField(choices=DAYS,default="Sat",blank=True,null=True,max_length=10)
    instance_consultation_end_day = models.CharField(choices=DAYS,default="Fri",blank=True,null=True,max_length=10)
    apointment_consultation_start_time = models.TimeField(auto_now=False,auto_now_add=False)
    apointment_consultation_end_time = models.TimeField(auto_now=False,auto_now_add=False)
    apointment_consultation_start_day = models.CharField(choices=DAYS,default="Sat",blank=True,null=True,max_length=10)
    apointment_consultation_end_day = models.CharField(choices=DAYS,default="Fri",blank=True,null=True,max_length=10)
    consultation_fee = models.PositiveIntegerField(null=True,blank=True)
    follow_up_fee = models.PositiveIntegerField(null=True,blank=True)
    follow_up_fee_applicable_days = models.PositiveIntegerField(null=True,blank=True)
    patient_attended = models.PositiveIntegerField(null=True,blank=True)
    joined_date_in_aracol_apps = models.DateTimeField(auto_now_add=True)
    avg_consultation_time = models.PositiveIntegerField(null=True,blank=True)
    doctor_code = models.CharField(max_length=10,null=True,blank=True)
    about = models.TextField(max_length=1000,null=True,blank=True)
    status = models.CharField(choices=STATUS,default="offline",max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}.{self.status}"

    

    
    