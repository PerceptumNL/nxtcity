# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_blogpage_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='author',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
