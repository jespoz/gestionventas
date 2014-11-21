# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0039_revisiones_proyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='revision',
            field=models.FloatField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
