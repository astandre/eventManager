# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-21 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_local_img_local'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='latitud_evento',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='evento',
            name='longitud_evento',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='local',
            name='latitud_local',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='local',
            name='longitud_local',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
