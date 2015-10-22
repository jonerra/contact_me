# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_message_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 22, 16, 53, 58, 740947, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
