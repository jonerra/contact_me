# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151020_2012'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AttachedInfo',
            new_name='Contact',
        ),
    ]
