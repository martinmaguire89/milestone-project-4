# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-11 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200611_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('singles', 'singles'), ('mixed_cases', 'mixed_cases'), ('merchandise', 'merchandise')], default='singles', max_length=120),
        ),
    ]
