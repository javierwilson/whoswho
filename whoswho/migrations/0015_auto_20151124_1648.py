# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0014_auto_20151124_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created',
            field=models.DateField(default=datetime.date(2015, 10, 1), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='modified',
            field=models.DateField(default=datetime.date(2015, 10, 1), auto_now=True),
            preserve_default=False,
        ),
    ]
