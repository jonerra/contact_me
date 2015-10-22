# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_message_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(max_length=300),
        ),
    ]
