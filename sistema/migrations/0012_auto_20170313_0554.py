# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0011_auto_20170313_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagoservicio',
            name='user_cuenta',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
