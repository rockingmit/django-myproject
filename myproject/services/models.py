from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    description = models.TextField(max_length=255)


class Feature(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    status = models.IntegerField(default=0)