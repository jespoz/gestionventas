# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0025_remove_observacion_proyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='observacion',
            name='proyecto',
            field=models.ForeignKey(blank=True, to='balanced.Proyecto', null=True),
            preserve_default=True,
        ),
    ]
