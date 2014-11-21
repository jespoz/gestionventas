# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0036_revisiones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revisiones',
            name='actualizado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='revisiones',
            name='revisado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
