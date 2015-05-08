# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
                'abstract': False,
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
                ('ranking', models.DecimalField(null=True, max_digits=2, decimal_places=1, blank=True)),
                ('telephone', models.CharField(max_length=15, null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
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
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='motel',
            name='town',
            field=models.ForeignKey(to='motels.Town'),
        ),
        migrations.AddField(
            model_name='comment',
            name='motel',
            field=models.ForeignKey(to='motels.Motel'),
        ),
    ]
