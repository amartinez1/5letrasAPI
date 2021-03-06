from core.models import TimeStampedModel
from django.contrib.gis.db import models

from motels.models import Motel

from autoslug import AutoSlugField
from versatileimagefield.fields import PPOIField
from versatileimagefield.fields import VersatileImageField


class Town(TimeStampedModel):
    name = models.CharField(max_length=50, unique=False)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=50)
    point = models.PointField()
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def count(instance):
        return Motel.objects.filter(town=instance,
                                    town__status=True,
                                    status=True).count()


class TownImage(TimeStampedModel):
    towns = models.ForeignKey(Town, related_name='images')
    image = VersatileImageField(
        'Towns Image',
        upload_to='uploaded_files/motels/',
        ppoi_field='image_ppoi',
        blank=True
    )
    image_ppoi = PPOIField()
