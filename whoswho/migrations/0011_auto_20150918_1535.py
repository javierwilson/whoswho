# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0010_organization_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='groups',
            field=models.ManyToManyField(to='whoswho.ContactGroup', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='worked_with',
            field=models.ManyToManyField(related_name='worked_with_rel_+', to='whoswho.Contact', blank=True),
        ),
    ]
