# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20171015_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='name',
            field=models.CharField(default='Test, 15 Oct', max_length=65),
            preserve_default=False,
        ),
    ]
