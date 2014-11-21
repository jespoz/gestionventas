# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0022_observacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='observacion',
        ),
    ]
