# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0012_auto_20140908_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='status',
            field=models.FloatField(default=0, null=b'', blank=b''),
            preserve_default=True,
        ),
    ]
