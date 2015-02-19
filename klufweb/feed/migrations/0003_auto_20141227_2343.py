# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20141227_2243'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='NewsArticle',
        ),
    ]
