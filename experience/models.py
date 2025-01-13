from django.db import models

# Create your models here.

class Experience(models.Model):
    doctor = models.ForeignKey("doctor.Doctor",related_name="experiences",on_delete=models.CASCADE)
    working_place = models.CharField(max_length=100,blank=True,null=True)
    designation = models.CharField(max_length=100,null=True,blank=True)
    department = models.CharField(max_length=100,null=True,blank=True)
    employment_start_date = models.DateField(auto_now_add=False,auto_now=False)
    employment_end_date = models.DateField(auto_now_add=True,auto_now=False)
    period = models.CharField(max_length=50,blank=True,null=True)

    def save(self,*args,**kwargs):
        from datetime import datetime

        start_date = self.employment_start_date
        end_date = self.employment_end_date or datetime.today.date()

        total_period = end_date - start_date

        years = total_period.days // 365
        months = (total_period.days%365)//30

        self.period = f"{years} years {months} months"



  
