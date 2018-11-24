# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0006_credito_debito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='user_cuenta',
            field=models.ForeignKey(to='sistema.UserProfile', null=True),
        ),
    ]
