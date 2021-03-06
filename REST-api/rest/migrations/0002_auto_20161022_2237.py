# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 22:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prefix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RenameField(
            model_name='pathupdate',
            old_name='name',
            new_name='path',
        ),
        migrations.AddField(
            model_name='pathupdate',
            name='prefix',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='paths', to='rest.Prefix'),
            preserve_default=False,
        ),
    ]
