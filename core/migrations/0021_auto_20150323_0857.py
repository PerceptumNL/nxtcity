# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_challengeindexpage_challengepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengepage',
            name='short_description',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='challengepage',
            name='organization',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
