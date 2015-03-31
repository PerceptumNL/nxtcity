# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20150325_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partnerpage',
            name='url',
        ),
    ]
