# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0025_auto_20160106_1506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['start', 'name']},
        ),
        migrations.AddField(
            model_name='event',
            name='monitor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='contact',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]
