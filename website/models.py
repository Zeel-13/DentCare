from django.db import models

# Create your models here.
class Appointment(models.Model):
    service=models.CharField(max_length=20)
    patient_name=models.CharField(max_length=15)
    patient_email=models.EmailField(max_length=50)
    doctor=models.CharField(max_length=15)
    date=models.CharField(max_length=15)
    time=models.CharField(max_length=15)