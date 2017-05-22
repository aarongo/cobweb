# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s_cobweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='exist',
            field=models.CharField(default=b'no', max_length=100, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0'),
        ),
        migrations.AddField(
            model_name='hostgroup',
            name='exist',
            field=models.CharField(default=b'no', max_length=100, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0'),
        ),
    ]
