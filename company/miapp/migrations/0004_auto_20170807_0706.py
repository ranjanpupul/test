# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-07 07:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_auto_20170807_0702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='comapnylocation',
            new_name='comapnyLocation',
        ),
    ]
