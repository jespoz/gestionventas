# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0020_proyecto_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='abierto',
            field=models.FloatField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proyecto',
            name='cerrado',
            field=models.FloatField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='status',
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='observacion',
            field=models.TextField(default=b'', null=True, blank=True),
        ),
    ]
