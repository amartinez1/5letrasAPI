from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.gis.db import models

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class TimeStampedModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class Location(models.Model):
#     """
#     A model which holds information about a particular location
#     """
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     point = models.PointField()
