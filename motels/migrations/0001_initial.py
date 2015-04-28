# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(null=True, max_digits=23, decimal_places=20, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=23, decimal_places=20, blank=True)),
                ('ranking', models.DecimalField(null=True, max_digits=2, decimal_places=2, blank=True)),
                ('telephone', models.CharField(max_length=15, null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(null=True, max_digits=23, decimal_places=20, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=23, decimal_places=20, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='motel',
            name='town',
            field=models.ForeignKey(to='motels.Town'),
        ),
    ]
