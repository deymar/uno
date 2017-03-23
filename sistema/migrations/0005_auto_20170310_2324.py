# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_auto_20170310_0222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='id',
        ),
        migrations.AlterField(
            model_name='pagoservicio',
            name='user_cuenta',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='servicio',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
    ]
