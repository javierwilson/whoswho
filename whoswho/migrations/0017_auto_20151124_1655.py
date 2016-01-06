# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0016_contact_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='age',
            field=models.IntegerField(null=True, verbose_name=b'Age', blank=True),
        ),
    ]
