# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-28 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0002_art_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='art.Category', verbose_name='分类名'),
        ),
        migrations.AlterField(
            model_name='art',
            name='tags',
            field=models.ManyToManyField(default=1, to='art.Tag', verbose_name='标签'),
        ),
    ]
