# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0008_auto_20170311_0434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_cuenta', models.CharField(max_length=60)),
                ('user_cuenta2', models.CharField(max_length=60)),
                ('monto', models.DecimalField(default=b'0.00', max_digits=10, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Transferencia',
                'verbose_name_plural': 'Transferencias',
            },
        ),
    ]
