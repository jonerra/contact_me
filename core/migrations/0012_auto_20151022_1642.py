# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20151022_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.IntegerField(default=0, choices=[(0, b' '), (1, b'Ms.'), (2, b'Mrs.'), (3, b'Mr.'), (4, b'Dr.')]),
        ),
    ]
