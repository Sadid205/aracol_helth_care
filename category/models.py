from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    image = models.URLField(max_length=500,blank=False,null=False)
    medicine = models.ManyToManyField('medicine.Medicine',related_name="category",blank=False)
