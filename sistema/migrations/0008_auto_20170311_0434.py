# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0007_auto_20170311_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debito',
            name='user_cuenta',
            field=models.ForeignKey(to='sistema.UserProfile', null=True),
        ),
    ]
