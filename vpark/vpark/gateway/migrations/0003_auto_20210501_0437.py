# Generated by Django 3.2 on 2021-04-30 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0002_auto_20210501_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='user',
        ),
        migrations.AlterField(
            model_name='entry',
            name='time',
            field=models.TimeField(default='04:37:30'),
        ),
    ]
