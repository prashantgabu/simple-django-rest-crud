from django.db import models
import datetime

# Create your models here.


class Crud(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.DateTimeField(max_length=20,null=True,blank=True,default=datetime.datetime.now())
