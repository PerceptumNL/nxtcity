# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('filename', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('data', models.TextField()),
                ('size', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
