# Generated by Django 3.2 on 2021-05-01 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0004_alter_entry_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='time',
            field=models.TimeField(default='03:13:40'),
        ),
    ]