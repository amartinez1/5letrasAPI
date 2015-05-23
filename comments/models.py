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

    # def save(self, *args, **kwargs):
    #     motel = self.motel
    #     print "Test!!! rating {0}, {1}".format(motel.rating, self.rating)
    #     motel.user_count += 1
    #     motel.rating += self.rating
    #     motel.save()
    #     super(Comment, self).save(*args, **kwargs)