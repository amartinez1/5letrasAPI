from autoslug import AutoSlugField
from core.models import TimeStampedModel
from django.db import models

from towns.models import Town

from versatileimagefield.fields import PPOIField
from versatileimagefield.fields import VersatileImageField

class Motel(TimeStampedModel):
    town = models.ForeignKey('towns.Town', related_name='town')
    name = models.CharField(max_length=50, unique=False)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=50)
    latitude = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)
    number_of_rooms = models.IntegerField(blank=True, null=True, unique=False)
    price_range = models.IntegerField(blank=True, null=True)
    ranking = models.DecimalField(
        max_digits=2, decimal_places=1, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True, unique=True)
    address2 = models.CharField(max_length=255, blank=True, null=True, unique=True)
    telephone = models.CharField(
        max_length=15, unique=False, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=False)
    website = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    amenities = models.ManyToManyField('motels.Amenitie', related_name='amenities', blank=True)

    def __unicode__(self):
        return self.name

class MotelImage(TimeStampedModel):
    motels = models.ForeignKey('motels.Motel', related_name='images')
    image = VersatileImageField(
        'Motels Image',
        upload_to='uploaded_files/motels/' ,
        ppoi_field='image_ppoi',
        blank=True
    )
    image_ppoi = PPOIField()

class Comment(TimeStampedModel):
    motel = models.ForeignKey('motels.Motel', related_name='comments')
    body = models.CharField(max_length=250, unique=False)
    ranking = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        ordering = ['-created_date']

    def __unicode__(self):
        return self.body


class Amenitie(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name