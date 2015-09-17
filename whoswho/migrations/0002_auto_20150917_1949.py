# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import django_countries.fields
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('whoswho', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(max_length=50, null=True, blank=True)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=40)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zip', models.CharField(max_length=10, null=True, blank=True)),
                ('type', models.CharField(max_length=20, choices=[(b'Home', b'Home'), (b'Work', b'Work')])),
                ('public_visible', models.BooleanField(default=False)),
                ('contact_visible', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=40)),
                ('first_name', models.CharField(max_length=40)),
                ('middle_name', models.CharField(max_length=40, blank=True)),
                ('title', models.CharField(max_length=40, blank=True)),
                ('url', models.URLField(blank=True)),
                ('blurb', models.TextField(null=True, blank=True)),
                ('profile_image', easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=b'profile_images/', blank=True)),
                ('qr_image', models.ImageField(null=True, upload_to=b'qr_images/', blank=True)),
                ('twitter_handle', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='ContactGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=40, verbose_name=b'Group Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('type', models.CharField(max_length=20, choices=[(b'Home', b'Home'), (b'Work', b'Work')])),
                ('public_visible', models.BooleanField(default=False)),
                ('contact_visible', models.BooleanField(default=False)),
                ('contact', models.ForeignKey(to='whoswho.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20, choices=[(b'Mobile', b'Mobile'), (b'Mobile Work', b'Mobile Work'), (b'Work', b'Work'), (b'Fax', b'Fax'), (b'Skype', b'Skype')])),
                ('public_visible', models.BooleanField(default=False)),
                ('contact_visible', models.BooleanField(default=False)),
                ('contact', models.ForeignKey(to='whoswho.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('handle', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20, choices=[(b'Skype', b'Skype'), (b'Twitter', b'Twitter'), (b'LinkedIn', b'LinkedIn'), (b'Facebook', b'Facebook'), (b'Pinterest', b'Pinterest')])),
                ('public_visible', models.BooleanField(default=False)),
                ('contact_visible', models.BooleanField(default=False)),
                ('contact', models.ForeignKey(to='whoswho.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.URLField(blank=True)),
                ('type', models.CharField(max_length=20, choices=[(b'Work', b'Work'), (b'Personal', b'Personal'), (b'Portfolio', b'Portfolio'), (b'Blog', b'Blog')])),
                ('public_visible', models.BooleanField(default=False)),
                ('contact_visible', models.BooleanField(default=False)),
                ('contact', models.ForeignKey(to='whoswho.Contact')),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='contact',
            field=models.ForeignKey(default=0, to='whoswho.Organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='groups',
            field=models.ManyToManyField(to='whoswho.ContactGroup'),
        ),
        migrations.AddField(
            model_name='contact',
            name='profession',
            field=models.ForeignKey(blank=True, to='whoswho.Profession', null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='contact',
            name='worked_with',
            field=models.ManyToManyField(related_name='worked_with_rel_+', to='whoswho.Contact'),
        ),
        migrations.AddField(
            model_name='address',
            name='contact',
            field=models.ForeignKey(to='whoswho.Contact'),
        ),
    ]
