# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields
import versatileimagefield.fields
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('towns', '0001_initial'),
        ('amenities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'name', unique=True, editable=False)),
                ('price_range', models.IntegerField(null=True, blank=True)),
                ('rating', models.FloatField(default=0, editable=False)),
                ('user_count', models.IntegerField(default=0, editable=False)),
                ('address', models.CharField(max_length=255, null=True, blank=True)),
                ('address2', models.CharField(max_length=255, null=True, blank=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('telephone', models.CharField(max_length=15, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('status', models.BooleanField(default=True)),
                ('amenities', models.ManyToManyField(related_name='amenities', to='amenities.Amenitie', blank=True)),
                ('town', models.ForeignKey(related_name='town', to='towns.Town')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MotelImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to=b'uploaded_files/motels/', verbose_name=b'Motels Image', blank=True)),
                ('image_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', max_length=20, editable=False)),
                ('motels', models.ForeignKey(related_name='images', to='motels.Motel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
