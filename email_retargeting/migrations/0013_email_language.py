# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-14 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_retargeting', '0012_auto_20170806_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='language',
            field=models.CharField(default='', max_length=5),
        ),
    ]