# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20150309_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
            preserve_default=True,
        ),
    ]
