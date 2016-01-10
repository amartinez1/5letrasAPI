from core.models import TimeStampedModel
from django.db import models


class Comment(TimeStampedModel):
    motel = models.ForeignKey('motels.Motel', related_name='comments')
    body = models.CharField(max_length=250, unique=False)
    rating = models.FloatField(blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_date']

    def __unicode__(self):
        return self.body
