# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0018_auto_20140915_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='lider',
        ),
    ]
