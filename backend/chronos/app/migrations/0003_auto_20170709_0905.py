# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-09 09:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170709_0858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weather',
            old_name='skycorn',
            new_name='skycon',
        ),
    ]
