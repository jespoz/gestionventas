# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('balanced', '0005_objetivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubObjetivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.TextField()),
                ('fecha_plazo', models.DateField()),
                ('cumplimiento', models.FloatField(default=0)),
                ('dimension', models.ForeignKey(to='balanced.Dimension')),
                ('lider', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('objetivo', models.ForeignKey(to='balanced.Objetivo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
