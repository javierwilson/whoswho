# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0006_contact_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='contact',
            field=models.ForeignKey(to='whoswho.Contact'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set([('contact', 'event')]),
        ),
    ]
