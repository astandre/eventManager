# Generated by Django 2.2 on 2019-04-17 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventHandler', '0002_auto_20190416_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificacion',
            name='calificacion',
            field=models.IntegerField(choices=[(0, 'Zero'), (1, 'Very Low'), (2, 'Low'), (3, 'Medium'), (4, 'High'), (5, 'Very High')], default=0),
        ),
    ]
