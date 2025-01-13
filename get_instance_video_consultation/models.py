from django.db import models

# Create your models here.

class GetInstanceVideoConsultation(models.Model):
    patient = models.ForeignKey("patient.Patient",related_name="gt_inst_vid_const",on_delete=models.CASCADE)
    doctor = models.ManyToManyField("doctor.Doctor",related_name="gt_inst_vid_const_list")
    consultation_name = models.CharField(max_length=50,null=False,blank=False)
    consultation_fee = models.FloatField(blank=False,null=False)
    vat_percent = models.PositiveIntegerField(blank=False,null=False)
    platform_fee = models.PositiveIntegerField(blank=False,null=False)
    net_amount = models.PositiveIntegerField(blank=True,null=True)
    vat_in_taka = models.FloatField(blank=True,null=True)
    promo_code = models.CharField(max_length=10,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        self.vat_in_taka = (self.consultation_fee*(self.vat_percent/100))
        self.net_amount = self.consultation_fee+self.vat_in_taka+self.platform_fee
        

    def __str__(self):
        return f"{self.consultation_name}-{self.net_amount}"
