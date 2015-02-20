# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20150220_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPageSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('title', models.CharField(max_length=255)),
                ('page', modelcluster.fields.ParentalKey(related_name='sections', to='landing.LandingPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='landingpagepart',
            name='page',
        ),
        migrations.DeleteModel(
            name='LandingPagePart',
        ),
    ]
