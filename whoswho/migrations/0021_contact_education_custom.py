# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0020_contact_organization_custom'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='education_custom',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
