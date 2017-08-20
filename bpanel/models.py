from django.db import models
from django.utils import timezone


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    adress= models.CharField(max_length=30)
    num_pass = models.IntegerField()
