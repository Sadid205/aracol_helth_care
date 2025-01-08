from django.db import models

# Create your models here.

class Medicine(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    price = models.IntegerField(null=False,blank=False)
    description = models.CharField(max_length=1000,null=False,blank=False)
    image = models.URLField(max_length=1000,null=False,blank=False)
    