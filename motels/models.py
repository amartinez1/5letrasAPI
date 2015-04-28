from django.db import models

# Create your models here.


class Town(models.Model):
    name = models.CharField(max_length=50, unique=False)
    latitude = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Motel(models.Model):
    town = models.ForeignKey(Town)
    name = models.CharField(max_length=50, unique=False)
    latitude = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)
    ranking = models.DecimalField(
        max_digits=2, decimal_places=1, blank=True, null=True)
    telephone = models.CharField(
        max_length=15, unique=False, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
