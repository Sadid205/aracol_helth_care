from django.db import models

# Create your models here.
class Cart(models.Model):
    patient = models.OneToOneField("patient.Patient",related_name="cart",on_delete=models.CASCADE)
    medicine = models.ManyToManyField('medicine.Medicine',related_name="carts",blank=True)
    