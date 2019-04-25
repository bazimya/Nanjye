# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-23 15:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nanjye', '0004_auto_20190403_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=2500)),
                ('lastname', models.CharField(max_length=2500)),
                ('username', models.CharField(max_length=2500)),
                ('profile_image', models.FileField(null=True, upload_to='images/')),
                ('email', models.CharField(max_length=2500)),
                ('location', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_product', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='productowner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2500)),
                ('phone', models.CharField(max_length=2500)),
                ('emargencephonenumber', models.CharField(max_length=2500)),
                ('profile', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='workers',
            name='user',
        ),
        migrations.RenameField(
            model_name='buyer',
            old_name='contact',
            new_name='name_tockenkey',
        ),
        migrations.RenameField(
            model_name='buyer',
            old_name='fname',
            new_name='product_list',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='discription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='location',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='phone',
        ),
        migrations.DeleteModel(
            name='workers',
        ),
        migrations.AddField(
            model_name='buyer',
            name='client_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nanjye.client'),
        ),
        migrations.AddField(
            model_name='product',
            name='categoryfrk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nanjye.categories'),
        ),
        migrations.AddField(
            model_name='product',
            name='imagefrk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nanjye.image'),
        ),
        migrations.AddField(
            model_name='product',
            name='productownfrk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nanjye.productowner'),
        ),
    ]