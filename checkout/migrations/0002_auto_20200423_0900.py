# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-23 09:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Postcode',
            new_name='postcode',
        ),
    ]