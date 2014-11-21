# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('balanced', '0033_auto_20141006_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='perfil',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='lider',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ciclo',
            name='observacion',
            field=models.TextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
    ]
