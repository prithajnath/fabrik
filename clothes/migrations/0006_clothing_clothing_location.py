# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0005_clothing_owned_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothing',
            name='clothing_location',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
