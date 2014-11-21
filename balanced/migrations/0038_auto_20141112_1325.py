# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0037_auto_20141112_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revisiones',
            name='avance',
        ),
        migrations.AddField(
            model_name='revisiones',
            name='cumplimiento',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
