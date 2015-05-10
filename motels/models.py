from autoslug import AutoSlugField
from core.models import TimeStampedModel
from django.db import models

from versatileimagefield.fields import VersatileImageField, PPOIField


class Amenitie(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name

class Town(TimeStampedModel):
    name = models.CharField(max_length=50, unique=False)
    latitude = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)
    image = VersatileImageField(
        'Image',
        upload_to='files/',
        ppoi_field='image_ppoi',
        blank=True
    )
    image_ppoi = PPOIField()
    slug = AutoSlugField(populate_from='name', unique=True, max_length=50)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Motel(TimeStampedModel):
    town = models.ForeignKey(Town, related_name='town')
    name = models.CharField(max_length=50, unique=False)
    latitude = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)
    number_of_rooms = models.IntegerField(blank=True, null=True, unique=False)
    price_range = models.IntegerField(blank=True, null=True)
    ranking = models.DecimalField(
        max_digits=2, decimal_places=1, blank=True, null=True)
    telephone = models.CharField(
        max_length=15, unique=False, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=False)
    image = VersatileImageField(
        'Image',
        upload_to='files/',
        ppoi_field='image_ppoi',
        blank=True
    )
    image_ppoi = PPOIField()
    website = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    amenitie = models.ManyToManyField(Amenitie, related_name='amenities', blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=50)

    def __unicode__(self):
        return self.name

class Comment(TimeStampedModel):
    motel = models.ForeignKey(Motel, related_name='comments')
    body = models.CharField(max_length=250, unique=False)
    ranking = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        ordering = ['-created_date']

    def __unicode__(self):
        return self.body