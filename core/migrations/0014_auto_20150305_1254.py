# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20150305_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fullblogpage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(),
            preserve_default=True,
        ),
    ]
