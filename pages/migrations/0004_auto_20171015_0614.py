# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 06:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20171014_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dateAdded',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 15, 6, 14, 55, 446063, tzinfo=utc), verbose_name='date added'),
        ),
    ]
