# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-28 15:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0006_auto_20180828_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='tags',
        ),
    ]
