# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-22 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('answer', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataSetName', models.CharField(max_length=200)),
                ('treeComplete', models.BooleanField(default=False)),
                ('ldsId', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qid', models.CharField(max_length=3)),
                ('question', models.CharField(max_length=1500)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='dataSet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dtree.DataSet'),
        ),
    ]
