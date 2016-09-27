# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-22 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtree', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ManyToManyField(to='dtree.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qid',
            field=models.CharField(max_length=2),
        ),
    ]