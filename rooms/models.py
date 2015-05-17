from autoslug import AutoSlugField
from core.models import TimeStampedModel
from django.db import models

from versatileimagefield.fields import PPOIField
from versatileimagefield.fields import VersatileImageField

class Room(TimeStampedModel):
    motel = models.ForeignKey('motels.Motel', related_name='rooms')
    name = models.CharField(max_length=50, unique=False)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=50)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    room_amenities = models.ManyToManyField('motels.Amenitie', related_name='room_amenities', blank=True)

    def __unicode__(self):
        return self.name

class RoomImage(TimeStampedModel):
    motels = models.ForeignKey('rooms.Room', related_name='images')
    image = VersatileImageField(
        'Rooms Image',
        upload_to='uploaded_files/Rooms/' ,
        ppoi_field='image_ppoi',
        blank=True
    )
    image_ppoi = PPOIField()
