from django.db import models
from .review_choices import RATING
# Create your models here.

class Review(models.Model):
    patient = models.ForeignKey("patient.Patient",related_name="reviews",on_delete=models.CASCADE)
    doctor = models.ForeignKey("doctor.Doctor",related_name="reviews",on_delete=models.CASCADE)
    rating = models.CharField(choices=RATING,default="1",max_length=10,null=True,blank=True)
    text = models.TextField(max_length=500,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reveiwed by {self.patient} for Dr. {self.doctor}"


