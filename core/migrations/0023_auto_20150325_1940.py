# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('core', '0022_auto_20150325_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerPageSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('title', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('body', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('logo', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='partner', to='core.PartnerPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='partnerpage',
            name='logo',
        ),
        migrations.AddField(
            model_name='partnerpage',
            name='url',
            field=models.URLField(default=b'', blank=True),
            preserve_default=True,
        ),
    ]
