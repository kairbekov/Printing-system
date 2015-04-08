# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20150327_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='data_upload_time',
        ),
    ]
