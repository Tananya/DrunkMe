# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-21 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DrunkMe', '0009_auto_20170522_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='bar',
            name='Password',
            field=models.CharField(default='barpassword', max_length=50),
        ),
        migrations.AddField(
            model_name='bar',
            name='Username',
            field=models.CharField(default='baruser', max_length=50),
        ),
    ]
