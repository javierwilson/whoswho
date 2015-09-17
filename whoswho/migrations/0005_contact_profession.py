# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0004_remove_contact_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='profession',
            field=models.ForeignKey(blank=True, to='whoswho.Profession', null=True),
        ),
    ]
