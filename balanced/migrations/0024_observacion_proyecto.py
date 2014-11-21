# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0023_remove_proyecto_observacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='observacion',
            name='proyecto',
            field=models.ForeignKey(blank=True, to='balanced.Proyecto', null=True),
            preserve_default=True,
        ),
    ]
