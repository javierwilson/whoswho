# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0018_remove_contact_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='age',
            field=models.IntegerField(null=True, verbose_name=b'Age', blank=True),
        ),
    ]
