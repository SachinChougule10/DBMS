# Generated by Django 3.2 on 2021-05-10 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0016_alter_entry_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='time',
            field=models.TimeField(default='01:47:43'),
        ),
    ]