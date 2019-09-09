# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User


from django.db import models


# Create your models here.

class Address(models.Model):
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    postal = models.CharField(max_length=25)
    country = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Enterprise(models.Model):
    name=models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Companies(models.Model):
    Enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.name


class Employee(models.Model):
    Companies=models.ForeignKey(Companies,on_delete=models.CASCADE)
    user=models.OneToOneField(User,on_delete=models.DO_NOTHING)

