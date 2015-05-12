from autoslug import AutoSlugField
from core.models import TimeStampedModel
from django.db import models

from versatileimagefield.fields import PPOIField
from versatileimagefield.fields import VersatileImageField


# Create your models here.
class Town(TimeStampedModel):
    name = models.CharField(max_length=50, unique=False)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=50)
    latitude = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=13, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class TownImage(TimeStampedModel):
    towns = models.ForeignKey('towns.Town', related_name='images')
    image = VersatileImageField(
        'Towns Image',
        upload_to='uploaded_files/motels/' ,
        ppoi_field='image_ppoi',
        blank=True
    )
    image_ppoi = PPOIField()