# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20150305_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='blog_entry', on_delete=b'', blank=True, to='core.FullBlogPage', null=True),
            preserve_default=True,
        ),
    ]
