# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_landingpage_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='notification',
            field=wagtail.wagtailcore.fields.RichTextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='tag_line',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
