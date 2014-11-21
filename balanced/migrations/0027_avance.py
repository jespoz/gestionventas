# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0026_observacion_proyecto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avance', models.FloatField(default=0)),
                ('ciclo', models.ForeignKey(to='balanced.Ciclo')),
                ('proyecto', models.ForeignKey(to='balanced.Proyecto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
