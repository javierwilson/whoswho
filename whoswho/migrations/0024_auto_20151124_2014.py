# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0023_auto_20151124_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='monitor',
            field=models.ForeignKey(to='whoswho.Monitor', null=True),
        ),
    ]
