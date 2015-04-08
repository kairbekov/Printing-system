# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20150327_1908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='data_upload_date',
            new_name='data_upload_time',
        ),
        migrations.RemoveField(
            model_name='data',
            name='user_id',
        ),
    ]
