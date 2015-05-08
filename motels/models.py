from django.db import models

from core.models import TimeStampedModel


class Town(TimeStampedModel):
    name = models.CharField(max_length=50, unique=False)
    latitude = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)

    def __unicode__(self):
        return self.name

class Motel(TimeStampedModel):
    town = models.ForeignKey(Town, related_name='town')
    name = models.CharField(max_length=50, unique=False)
    latitude = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)
    ranking = models.DecimalField(
        max_digits=2, decimal_places=1, blank=True, null=True)
    telephone = models.CharField(
        max_length=15, unique=False, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Comment(TimeStampedModel):
    motel = models.ForeignKey(Motel, related_name='comments')
    body = models.CharField(max_length=250, unique=False)
    ranking = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    def __unicode__(self):
        return self.body

