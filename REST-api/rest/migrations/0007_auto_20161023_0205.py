# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0006_auto_20161023_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='as',
            name='latitude',
            field=models.CharField(blank=True, default=b'', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='as',
            name='longitude',
            field=models.CharField(blank=True, default=b'', max_length=200, null=True),
        ),
    ]
