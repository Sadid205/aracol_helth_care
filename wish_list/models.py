from django.db import models

# Create your models here.

class WishList(models.Model):
    medicine = models.ManyToManyField('medicine.Medicine',related_name="wish_list",blank=True)
