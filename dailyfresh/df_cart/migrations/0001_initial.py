# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0002_auto_20180516_1717'),
        ('df_user', '0002_auto_20180514_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('ccount', models.IntegerField()),
                ('cgoods', models.ForeignKey(to='df_goods.GoodsInfo')),
                ('cuser', models.ForeignKey(to='df_user.UserInfo')),
            ],
        ),
    ]
