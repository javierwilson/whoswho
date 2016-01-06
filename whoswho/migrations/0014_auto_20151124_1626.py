# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0013_auto_20151119_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='birth',
        ),
        migrations.AddField(
            model_name='contact',
            name='age',
            field=models.DateField(null=True, verbose_name=b'Age', blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='dob',
            field=models.DateField(null=True, verbose_name=b'Date of Birth', blank=True),
        ),
    ]
