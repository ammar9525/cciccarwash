from django.db import models

# Create your models here.

class Detail(models.Model):
    customer_id = models.AutoField
    customer_name = models.CharField(max_length=50, null=True)
    customer_phone = models.CharField(max_length=10, null=True )
    car_id = models.CharField(max_length=50, null=True)
    service_cat = models.CharField(max_length=50,null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)


