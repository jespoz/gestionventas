# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0021_auto_20140915_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observacion', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': b'Observaciones',
            },
            bases=(models.Model,),
        ),
    ]
