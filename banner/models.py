from django.db import models
from .banner_choices import PAGE_CHOICES
# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length=100,blank=False,null=True)
    page = models.CharField(choices=PAGE_CHOICES,max_length=10,blank=False,null=False)
    image = models.URLField(max_length=500,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.page} - {self.title}"

