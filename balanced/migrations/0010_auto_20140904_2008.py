# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0009_auto_20140904_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objetivo',
            old_name='clave',
            new_name='ciclo',
        ),
    ]
