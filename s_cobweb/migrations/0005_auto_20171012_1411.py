# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-10-12 14:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s_cobweb', '0004_auto_20170419_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='cpu_type',
        ),
        migrations.RemoveField(
            model_name='host',
            name='server_type',
        ),
        migrations.RemoveField(
            model_name='host',
            name='swap_total',
        ),
    ]