from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class sdata(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    sapid = models.IntegerField(validators=[MinValueValidator(10000000000), MaxValueValidator(99999999999)])
    email = models.CharField(max_length=100)
    phone = models.IntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])

    def __str__(self):
        return self.name


class Foodname(models.Model):

    name = models.CharField(max_length=100)
    image = models.FileField()

    def __str__(self):
        return self.name
