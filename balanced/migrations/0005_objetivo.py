# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0004_auto_20140902_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clave', models.CharField(max_length=10)),
                ('objetivo', models.TextField()),
                ('dimension', models.ForeignKey(to='balanced.Dimension')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
