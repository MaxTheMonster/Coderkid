# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-04 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almanac', '0003_remove_post_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='language',
            field=models.CharField(default='python', max_length=40),
            preserve_default=False,
        ),
    ]
