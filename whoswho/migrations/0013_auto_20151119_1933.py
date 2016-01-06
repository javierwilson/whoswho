# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('whoswho', '0012_contact_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='events',
        ),
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='area_desarrollo_mz',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='area_mz',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='area_productiva_mz',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='birth',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='city',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='community',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='document',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='education',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'P', 'Primaria'), (b'S', 'Secundaria'), (b'U', 'Universitaria'), (b'O', '--')]),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_personal',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_work',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='men_home',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='municipality',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_personal',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_work',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='state',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='street',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='women_home',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='zip',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='contact',
            field=models.ForeignKey(related_name='events', to='whoswho.Contact'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
