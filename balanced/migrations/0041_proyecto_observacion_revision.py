# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0040_proyecto_revision'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='observacion_revision',
            field=models.TextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
    ]
