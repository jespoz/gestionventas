# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0041_proyecto_observacion_revision'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='actualizado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
