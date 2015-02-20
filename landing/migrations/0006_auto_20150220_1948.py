# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_auto_20150220_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingpage',
            name='tag_line',
            field=wagtail.wagtailcore.fields.RichTextField(),
            preserve_default=True,
        ),
    ]
