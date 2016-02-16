# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0024_auto_20151124_2014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monitor',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='contact',
            name='organization_custom',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='type',
            field=models.ForeignKey(blank=True, to='whoswho.AttendeeType', null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='monitor',
            field=models.ForeignKey(blank=True, to='whoswho.Monitor', null=True),
        ),
    ]
