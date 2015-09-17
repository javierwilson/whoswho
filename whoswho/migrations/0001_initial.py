# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import django_countries.fields
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttendeeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Attendee Type',
                'verbose_name_plural': 'Attendee Types',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('title', models.CharField(max_length=400, null=True, verbose_name='Title', blank=True)),
                ('organizer', models.CharField(max_length=200, null=True, verbose_name='Organizer', blank=True)),
                ('text', models.TextField(blank=True)),
                ('start', models.DateTimeField(null=True, verbose_name='Start', blank=True)),
                ('end', models.DateTimeField(null=True, verbose_name='End', blank=True)),
                ('place', models.CharField(max_length=200, null=True, verbose_name='Place', blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Profession',
                'verbose_name_plural': 'Profession',
            },
        ),
        migrations.AddField(
            model_name='attendance',
            name='event',
            field=models.ForeignKey(to='whoswho.Profession'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='type',
            field=models.ForeignKey(to='whoswho.AttendeeType'),
        ),
    ]
