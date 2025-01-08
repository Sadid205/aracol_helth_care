from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    image = models.URLField(max_length=500,blank=True,null=True)
    medicine = models.ManyToManyField('medicine.Medicine',related_name="category",blank=True)
