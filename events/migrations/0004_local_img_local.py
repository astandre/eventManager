# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-20 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_evento_direccion_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='img_local',
            field=models.CharField(default='img.png', max_length=300),
        ),
    ]