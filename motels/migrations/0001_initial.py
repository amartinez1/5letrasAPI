# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenitie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('body', models.CharField(max_length=250)),
                ('ranking', models.DecimalField(null=True, max_digits=2, decimal_places=1, blank=True)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Motel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(null=True, max_digits=16, decimal_places=13, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=16, decimal_places=13, blank=True)),
                ('number_of_rooms', models.IntegerField(null=True, blank=True)),
                ('price_range', models.IntegerField(null=True, blank=True)),
                ('ranking', models.DecimalField(null=True, max_digits=2, decimal_places=1, blank=True)),
                ('telephone', models.CharField(max_length=15, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to=b'files/', verbose_name=b'image', blank=True)),
                ('image_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', max_length=20, editable=False)),
                ('website', models.URLField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('amenitie', models.ManyToManyField(related_name='amenities', to='motels.Amenitie', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(null=True, max_digits=16, decimal_places=13, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=16, decimal_places=13, blank=True)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to=b'files/', verbose_name=b'image', blank=True)),
                ('image_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', max_length=20, editable=False)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='motel',
            name='town',
            field=models.ForeignKey(related_name='town', to='motels.Town'),
        ),
        migrations.AddField(
            model_name='comment',
            name='motel',
            field=models.ForeignKey(related_name='comments', to='motels.Motel'),
        ),
    ]
