# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0010_auto_20170313_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagoservicio',
            name='tipo_servicio',
            field=models.CharField(max_length=100),
        ),
    ]
