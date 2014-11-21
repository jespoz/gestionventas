# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0006_subobjetivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indicador', models.CharField(max_length=50)),
                ('cumplimiento', models.FloatField(default=0)),
                ('fecha_plazo', models.DateField()),
                ('subobjetivo', models.ForeignKey(to='balanced.SubObjetivo')),
            ],
            options={
                'verbose_name_plural': b'Indicadores',
            },
            bases=(models.Model,),
        ),
    ]
