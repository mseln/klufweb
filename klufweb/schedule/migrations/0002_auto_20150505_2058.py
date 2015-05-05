# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=50, default='n.a.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='body',
            field=ckeditor.fields.RichTextField(null=True),
            preserve_default=True,
        ),
    ]
