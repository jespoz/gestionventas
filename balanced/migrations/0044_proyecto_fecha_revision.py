# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0043_proyecto_revisado'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='fecha_revision',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
