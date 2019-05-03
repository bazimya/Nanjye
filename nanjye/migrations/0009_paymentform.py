# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-03 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nanjye', '0008_auto_20190425_0702'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('phonenumber', models.IntegerField()),
                ('transaction_code', models.IntegerField()),
            ],
        ),
    ]