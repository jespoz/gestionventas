# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0014_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='lider',
            field=models.ForeignKey(to='balanced.Perfil'),
        ),
    ]
