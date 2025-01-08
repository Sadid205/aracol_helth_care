from django.db import models

# Create your models here.

class Checkout(models.Model):
    # author = ManyToMany relationship with author because , an authro can checkout many times.
    name = models.CharField(max_length=500,null=True)
    address = models.CharField(max_length=600,null=True)
    phone = models.CharField(max_length=15,null=True)
    email = models.EmailField(max_length=30,null=True)
    cart = models.OneToOneField('cart.Cart',on_delete=models.CASCADE ,related_name="checkout",blank=True,null=True)