# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20150225_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('headline', models.CharField(max_length=200)),
                ('body', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
                ('location', models.CharField(max_length=50)),
                ('event_time', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
