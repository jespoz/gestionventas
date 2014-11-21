# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0002_ciclo_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Perspectiva',
            new_name='Dimension',
        ),
        migrations.AlterModelOptions(
            name='dimension',
            options={'verbose_name_plural': b'Dimensiones'},
        ),
        migrations.AddField(
            model_name='ciclo',
            name='observacion',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='dimension',
            old_name='perspectiva',
            new_name='dimension',
        ),
    ]
