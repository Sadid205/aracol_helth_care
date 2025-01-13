from django.db import models

# Create your models here.

class WishList(models.Model):
    patient = models.OneToOneField("patient.Patient",related_name="wish_list",on_delete=models.CASCADE)
    medicine = models.ManyToManyField('medicine.Medicine',related_name="wish_list",blank=True)
