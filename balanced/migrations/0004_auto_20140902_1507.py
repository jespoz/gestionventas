# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0003_auto_20140901_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciclo',
            name='observacion',
            field=models.TextField(default=b'', null=True),
        ),
    ]
