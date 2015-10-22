# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20151022_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(default='Hello', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.IntegerField(default=0, choices=[(0, b' '), (1, b'Ms.'), (2, b'Mrs.'), (3, b'Mr.'), (4, b'Dr.')]),
        ),
    ]
