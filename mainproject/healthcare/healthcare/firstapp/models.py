
from django.db import models


class Doctors(models.Model):
    D_name = models.CharField(max_length=50)
    D_address = models.CharField(max_length=200)
    D_gender = models.CharField(max_length=10)
    D_qualification = models.CharField(max_length=50)
    D_email = models.EmailField(max_length=50)
    D_password = models.CharField(max_length=20)

class XrayUpload(models.Model):
    patient_id = models.IntegerField(null=True)
    xray_image = models.ImageField(upload_to='images/')
    result = models.CharField(max_length=50)
    image_date = models.DateTimeField(auto_now=True)




class PatientRegistration(models.Model):
    patientName = models.CharField(max_length=50)
    t_nNo = models.IntegerField()

    patientAge = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phoneNo = models.CharField(max_length=12)
    discription = models.CharField(max_length=50, null=True)
    regDate = models.DateTimeField(auto_now=True)
    doct_id = models.IntegerField()


