# Generated by Django 3.2 on 2021-05-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0005_alter_entry_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='time',
            field=models.TimeField(default='17:56:02'),
        ),
    ]
