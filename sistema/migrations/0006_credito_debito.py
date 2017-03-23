# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0005_auto_20170310_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.DecimalField(default=b'0.00', max_digits=10, decimal_places=2)),
                ('descripcion', models.CharField(max_length=100)),
                ('user_cuenta', models.ForeignKey(to='sistema.UserProfile')),
            ],
            options={
                'verbose_name': 'Credito',
                'verbose_name_plural': 'Creditos',
            },
        ),
        migrations.CreateModel(
            name='Debito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.DecimalField(default=b'0.00', max_digits=10, decimal_places=2)),
                ('descripcion', models.CharField(max_length=100)),
                ('user_cuenta', models.ForeignKey(to='sistema.UserProfile')),
            ],
            options={
                'verbose_name': 'Debito',
                'verbose_name_plural': 'Debitos',
            },
        ),
    ]
