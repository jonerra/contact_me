# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20151022_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=4, choices=[(b'0', b'Ms.'), (b'1', b'Mrs.'), (b'2', b'Mr.'), (b'3', b'Dr.')]),
        ),
    ]
