# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-01 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighboursapp', '0002_auto_20191101_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='general_loc',
            field=models.CharField(max_length=50, null=True),
        ),
    ]