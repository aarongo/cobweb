# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s_cobweb', '0002_auto_20170419_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='exist',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0'),
        ),
        migrations.AlterField(
            model_name='hostgroup',
            name='exist',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0'),
        ),
    ]
