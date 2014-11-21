# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0017_remove_proyecto_lider'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='lider',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='perfil',
        ),
    ]
