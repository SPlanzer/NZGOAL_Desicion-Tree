# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-26 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtree', '0008_auto_20160926_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='ldsId',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
