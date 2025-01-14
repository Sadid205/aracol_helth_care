from django.db import models

# Create your models here.
class Cart(models.Model):
    medicine = models.ManyToManyField('medicine.Medicine',related_name="carts",blank=True)
    