# Generated by Django 3.2 on 2021-05-10 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0018_alter_entry_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='time',
            field=models.TimeField(default='02:01:32'),
        ),
    ]
