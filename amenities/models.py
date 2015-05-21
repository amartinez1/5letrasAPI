from django.db import models

from core.models import TimeStampedModel

from autoslug import AutoSlugField


class Amenitie(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=50)

    def __unicode__(self):
        return self.name
