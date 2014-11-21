# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0008_auto_20140904_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='indicador',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True),
        ),
    ]
