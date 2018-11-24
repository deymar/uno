# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_auto_20170308_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='codigo',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='correo',
            field=models.EmailField(unique=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='saldo',
            field=models.DecimalField(default=b'0.00', max_digits=10, decimal_places=2),
        ),
    ]
