# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-07 10:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_null_help_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewformelement',
            options={'ordering': ('order', 'name')},
        ),
    ]
