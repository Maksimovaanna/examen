from django.db import models
from django.urls import reverse
# Create your models here.

class Test(models.Model):
    field1 = models.CharField(max_length=50)
    field2 = models.IntegerField(default=0)
    field3 = models.IntegerField(default=0)
