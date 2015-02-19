# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=10000)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
