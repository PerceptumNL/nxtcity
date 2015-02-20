# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20150220_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='footer_content',
            field=wagtail.wagtailcore.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landingpage',
            name='tag_line',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landingpagesection',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landingpagesection',
            name='short_title',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
