# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-01 12:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('neighboursapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='police',
            name='neighbour',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='neighbour',
            name='healthCare',
            field=models.TextField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='neighbour',
            name='nearPolice',
            field=models.TextField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='neighbourhoodName',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Police',
        ),
    ]
