# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20151022_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.IntegerField(default=b'title', choices=[(0, b' '), (1, b'Ms.'), (2, b'Mrs.'), (3, b'Mr.'), (4, b'Dr.')]),
        ),
    ]
