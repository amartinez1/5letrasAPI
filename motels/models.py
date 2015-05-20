from autoslug import AutoSlugField
from core.models import TimeStampedModel
from django.db import models

from versatileimagefield.fields import PPOIField
from versatileimagefield.fields import VersatileImageField


class Motel(TimeStampedModel):
    town = models.ForeignKey('towns.Town', related_name='town')
    name = models.CharField(max_length=50, unique=False)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=50)
    latitude = models.DecimalField(max_digits=16, decimal_places=13,
        blank=True, null=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=13,
        blank=True, null=True)
    price_range = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(editable=False, default=0)
    user_count = models.IntegerField(editable=False, default=0)
    address = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(
        max_length=15, unique=False, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=False)
    website = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    amenities = models.ManyToManyField('motels.Amenitie',
        related_name='amenities', blank=True)

    def __unicode__(self):
        return self.name

    def get_percent(self):
        return self.rating / float(self.user_count)


class MotelImage(TimeStampedModel):
    motels = models.ForeignKey('motels.Motel', related_name='images')
    image = VersatileImageField(
        'Motels Image',
        upload_to='uploaded_files/motels/',
        ppoi_field='image_ppoi',
        blank=True
    )
    image_ppoi = PPOIField()


class Comment(TimeStampedModel):
    motel = models.ForeignKey('motels.Motel', related_name='comments')
    body = models.CharField(max_length=250, unique=False)
    rating = models.FloatField(blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_date']

    def __unicode__(self):
        return self.body

    def save(self, *args, **kwargs):
        motel = self.motel
        print "Test!!! rating {0}, {1}".format(motel.rating, self.rating)
        motel.user_count += 1
        motel.rating += self.rating
        motel.save()
        super(Comment, self).save(*args, **kwargs)


class Amenitie(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=50)

    def __unicode__(self):
        return self.name
