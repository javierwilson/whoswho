# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0017_auto_20151124_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='age',
        ),
    ]
