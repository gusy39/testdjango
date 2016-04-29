from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Car(models.Model):
       cname=models.CharField(max_length=30)
class Person(models.Model):
       Car=models.ForeignKey(Car)
       pname=models.CharField(max_length=30)
