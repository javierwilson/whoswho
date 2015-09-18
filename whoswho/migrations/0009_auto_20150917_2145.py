# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0008_auto_20150917_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='events',
            field=models.ManyToManyField(to='whoswho.Event', through='whoswho.Attendance'),
        ),
        migrations.AlterField(
            model_name='attendeetype',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='profession',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name='Name'),
        ),
    ]
