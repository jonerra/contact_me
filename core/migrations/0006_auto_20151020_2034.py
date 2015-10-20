# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151020_2028'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Contact',
        ),
    ]
