# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_auto_20161022_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='as',
            name='latitude',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='as',
            name='longitude',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
