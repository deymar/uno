# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='saldo',
            field=models.DecimalField(default=b'0.00', editable=False, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='codigo',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
