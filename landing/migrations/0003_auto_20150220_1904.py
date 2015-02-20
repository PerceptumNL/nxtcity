# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_landingpagepart'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='landingpagepart',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='landingpagepart',
            name='sort_order',
            field=models.IntegerField(null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='landingpagepart',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='parts', to='landing.LandingPage'),
            preserve_default=True,
        ),
    ]
