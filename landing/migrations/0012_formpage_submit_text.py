# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0011_auto_20150224_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='formpage',
            name='submit_text',
            field=models.CharField(default=b'Submit', max_length=255),
            preserve_default=True,
        ),
    ]
