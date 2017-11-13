# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 04:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=65)),
                ('amount', models.FloatField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=45)),
                ('quantity', models.FloatField()),
                ('unity', models.CharField(max_length=45)),
                ('unit_cost', models.FloatField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Budget')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('0', 'Creado'), ('1', 'Planificado'), ('2', 'Gestión por iniciar'), ('3', 'En ejecución'), ('4', 'Finalizado'), ('5', 'Detenido'), ('6', 'Cancelado')], default='0', max_length=1)),
                ('location', models.TextField(blank=True, null=True)),
                ('project_type', models.CharField(choices=[('0', 'Interno'), ('1', 'Externo'), ('2', 'Conjunto')], default='0', max_length=1)),
                ('attendant', models.CharField(blank=True, max_length=45, null=True)),
                ('snip', models.CharField(blank=True, max_length=45, null=True)),
                ('nog', models.CharField(blank=True, max_length=45, null=True)),
                ('smip', models.CharField(blank=True, max_length=45, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
        migrations.AddField(
            model_name='budget',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='budget', to='projects.Project'),
        ),
    ]
