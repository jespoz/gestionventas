# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0030_auto_20140929_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observacion',
            name='observacion',
            field=models.CharField(max_length=10000),
        ),
    ]
