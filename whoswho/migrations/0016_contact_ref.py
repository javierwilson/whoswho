# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0015_auto_20151124_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='ref',
            field=models.IntegerField(null=True, verbose_name=b'Reference', blank=True),
        ),
    ]
