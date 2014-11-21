# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0035_proyecto_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revisiones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observacion', models.TextField()),
                ('actualizado', models.BooleanField()),
                ('revisado', models.BooleanField()),
                ('avance', models.ForeignKey(to='balanced.Avance')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
