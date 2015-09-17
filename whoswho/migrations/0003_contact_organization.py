# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0002_auto_20150917_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='organization',
            field=models.ForeignKey(blank=True, to='whoswho.Organization', null=True),
        ),
    ]
