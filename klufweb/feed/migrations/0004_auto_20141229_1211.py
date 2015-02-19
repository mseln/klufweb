# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20141227_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 29, 11, 11, 7, 540368, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2014, 12, 29, 11, 11, 29, 101175, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 29, 11, 11, 42, 82623, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
