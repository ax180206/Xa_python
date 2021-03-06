# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-28 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0005_auto_20180828_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='art.Category', verbose_name='分类名'),
        ),
        migrations.AddField(
            model_name='art',
            name='change_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='最近更新时间'),
        ),
        migrations.AddField(
            model_name='art',
            name='pulish_data',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='发布时间'),
        ),
        migrations.AddField(
            model_name='art',
            name='tags',
            field=models.ManyToManyField(default=1, to='art.Tag', verbose_name='标签'),
        ),
    ]
