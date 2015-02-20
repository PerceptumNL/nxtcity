# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_languageredirectionpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='language',
            field=models.CharField(default='nl', max_length=10, choices=[(b'nl', b'Nederlands'), (b'en', b'English')]),
            preserve_default=False,
        ),
    ]
