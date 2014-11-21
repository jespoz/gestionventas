# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('balanced', '0007_indicador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.TextField()),
                ('fecha_plazo', models.DateField()),
                ('cumplimiento', models.FloatField(default=0)),
                ('indicador', models.CharField(default=b'', max_length=50, null=True)),
                ('dimension', models.ForeignKey(to='balanced.Dimension')),
                ('lider', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('objetivo', models.ForeignKey(to='balanced.Objetivo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='indicador',
            name='subobjetivo',
        ),
        migrations.DeleteModel(
            name='Indicador',
        ),
        migrations.RemoveField(
            model_name='subobjetivo',
            name='dimension',
        ),
        migrations.RemoveField(
            model_name='subobjetivo',
            name='lider',
        ),
        migrations.RemoveField(
            model_name='subobjetivo',
            name='objetivo',
        ),
        migrations.DeleteModel(
            name='SubObjetivo',
        ),
    ]
