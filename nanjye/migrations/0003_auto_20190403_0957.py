# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-03 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nanjye', '0002_auto_20190403_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='Id',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]
