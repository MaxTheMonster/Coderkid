# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-11 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almanac', '0004_example_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
