# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0031_auto_20140929_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='checkeado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
