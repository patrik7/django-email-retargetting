# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-16 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_retargeting', '0004_auto_20170415_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='domain',
            field=models.CharField(default='bovine.ch', max_length=128),
        ),
    ]
