# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('core', '0021_auto_20150323_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('logo', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='challengepage',
            name='organization',
            field=models.CharField(default=b'', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='challengepage',
            name='short_description',
            field=models.CharField(default=b'', max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
