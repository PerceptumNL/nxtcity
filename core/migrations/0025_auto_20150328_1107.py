# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_remove_partnerpage_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnerpagesection',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='partners', to='core.PartnerPage'),
            preserve_default=True,
        ),
    ]
