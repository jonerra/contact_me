# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151020_2009'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='AttachedInfo',
        ),
    ]
