# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balanced', '0010_auto_20140904_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='adjunto',
            field=models.FileField(null=True, upload_to=b'documentos', blank=True),
            preserve_default=True,
        ),
    ]
