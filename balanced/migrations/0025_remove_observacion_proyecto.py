# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0024_observacion_proyecto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observacion',
            name='proyecto',
        ),
    ]
