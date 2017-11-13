# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 04:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import items.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to=items.models.path_document)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('0', 'Entregado'), ('1', 'En revision'), ('2', 'Finalizado')], default='0', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('attendant', models.CharField(max_length=45)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item'),
        ),
        migrations.AddField(
            model_name='file',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]
