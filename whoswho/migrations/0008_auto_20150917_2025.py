# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0007_auto_20150917_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='event',
            field=models.ForeignKey(to='whoswho.Event'),
        ),
    ]
