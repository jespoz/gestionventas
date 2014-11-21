# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0032_proyecto_checkeado'),
    ]

    operations = [
        migrations.AddField(
            model_name='avance',
            name='checkeado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='checkeado',
        ),
    ]
