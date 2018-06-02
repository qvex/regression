# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-30 05:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regressionApp', '0003_auto_20180630_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cropprediction',
            name='predYears',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='predYears_set', to='regressionApp.PredYear'),
        ),
    ]
