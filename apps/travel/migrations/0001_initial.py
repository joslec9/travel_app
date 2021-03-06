# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinedTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('datestart', models.DateTimeField()),
                ('dateend', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('planner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_registration.User')),
            ],
        ),
        migrations.AddField(
            model_name='joinedtrip',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Travel'),
        ),
        migrations.AddField(
            model_name='joinedtrip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_registration.User'),
        ),
    ]
