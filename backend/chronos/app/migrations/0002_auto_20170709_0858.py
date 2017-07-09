# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-09 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='datetime',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='event',
            name='Region',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Place'),
        ),
    ]