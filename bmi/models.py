from django.db import models
from .bmi_choices import GENDER,BMI_INDEX
# Create your models here.

class BMI(models.Model):
    patient = models.ForeignKey("patient.Patient",related_name="bmi",on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER,max_length=20,blank=False,null=False)
    weight_kg = models.FloatField(blank=False,null=False)
    height_feet = models.PositiveIntegerField(blank=False,null=True)
    height_remaining_inches = models.PositiveIntegerField(blank=False,null=True)
    age = models.PositiveIntegerField(blank=False,null=False)
    date = models.DateTimeField(auto_now_add=True)
    bmi = models.FloatField(blank=True,null=True)
    bmi_index = models.CharField(choices=BMI_INDEX,max_length=30,blank=True,null=True)
    

    def __str__(self):
        return f"{self.patient} - {self.bmi_index}"