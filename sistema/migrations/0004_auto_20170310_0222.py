# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_auto_20170308_0242'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagoServicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cuenta_servicio', models.CharField(max_length=50)),
                ('monto', models.DecimalField(default=b'0.00', max_digits=10, decimal_places=2)),
                ('user_cuenta', models.UUIDField()),
            ],
            options={
                'verbose_name': 'Pago de Servicio',
                'verbose_name_plural': 'Pago de Servicios',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('servicio', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.AddField(
            model_name='pagoservicio',
            name='tipo_servicio',
            field=models.ForeignKey(to='sistema.Servicio'),
        ),
    ]
