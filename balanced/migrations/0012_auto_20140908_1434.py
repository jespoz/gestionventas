# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0011_proyecto_adjunto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyecto',
            options={'ordering': [b'cumplimiento']},
        ),
        migrations.AddField(
            model_name='proyecto',
            name='observacion',
            field=models.TextField(default=b'', null=b'', blank=b''),
            preserve_default=True,
        ),
    ]
