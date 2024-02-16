# delivery/models.py

from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)

class Item(models.Model):
    type = models.CharField(max_length=255)
    description = models.TextField()

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=255)
    base_distance_in_km = models.FloatField()
    km_price = models.FloatField()
    fix_price = models.FloatField()
