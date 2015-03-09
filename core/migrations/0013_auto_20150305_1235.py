# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20150305_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fullblogpage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(default=b'', blank=True),
            preserve_default=True,
        ),
    ]
