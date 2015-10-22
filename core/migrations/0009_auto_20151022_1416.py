# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20151021_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.IntegerField(default=0, choices=[(0, b'Ms.'), (1, b'Mrs.'), (2, b'Mr.'), (3, b'Dr.')]),
        ),
    ]
