# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-21 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DrunkMe', '0008_auto_20170522_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
