# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motel',
            name='ranking',
            field=models.DecimalField(null=True, max_digits=3, decimal_places=1, blank=True),
        ),
    ]
