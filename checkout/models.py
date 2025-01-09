from django.db import models

# Create your models here.

class Checkout(models.Model):
    # author = ManyToMany relationship with author because , an authro can checkout many times.
    name = models.CharField(max_length=500,null=False,blank=False)
    address = models.CharField(max_length=600,null=False,blank=False)
    phone = models.CharField(max_length=15,null=False,blank=False)
    email = models.EmailField(max_length=30,null=False,blank=False)
    