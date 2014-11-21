# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0015_auto_20140915_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='perfil',
            field=models.ForeignKey(blank=True, to='balanced.Perfil', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='lider',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
