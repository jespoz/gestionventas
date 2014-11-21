# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0029_delete_monthlyweatherbycity'),
    ]

    operations = [
        migrations.AddField(
            model_name='observacion',
            name='usuario',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='observacion',
            name='observacion',
            field=models.CharField(max_length=1500),
        ),
    ]
