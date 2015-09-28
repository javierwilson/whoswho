# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0011_auto_20150918_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='sex',
            field=models.CharField(max_length=1, null=True, choices=[(b'M', 'Man'), (b'F', 'Woman'), (b'O', '--')]),
        ),
    ]
