# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_message_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(default='hello', max_length=300),
            preserve_default=False,
        ),
    ]
