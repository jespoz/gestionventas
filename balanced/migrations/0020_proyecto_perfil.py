# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0019_remove_proyecto_lider'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='perfil',
            field=models.ForeignKey(blank=True, to='balanced.Perfil', null=True),
            preserve_default=True,
        ),
    ]
