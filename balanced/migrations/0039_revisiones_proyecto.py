# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0038_auto_20141112_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='revisiones',
            name='proyecto',
            field=models.ForeignKey(to='balanced.Proyecto', null=True),
            preserve_default=True,
        ),
    ]
