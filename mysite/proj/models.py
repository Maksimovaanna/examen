from django.db import models
from django.urls import reverse
# Create your models here.

class Test(models.Model):
    nomer_reysa = models.IntegerField(default=0)
    aeroport_vileta = models.CharField(max_length=50)
    aeroport_prileta = models.CharField(max_length=50)
    vremya_vileta = models.CharField(max_length=50)
    dlitelnost_poleta = models.CharField(max_length=50)

class ID(models.Model):
    id_passajira = models.IntegerField(default=0)
    nomer_telefona = models.CharField(max_length=50)
    parol = models.CharField(max_length=50)
    kolichestvo_mil = models.IntegerField(default=0)