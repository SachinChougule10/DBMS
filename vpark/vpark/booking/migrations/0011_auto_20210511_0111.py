# Generated by Django 3.2 on 2021-05-10 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_auto_20210510_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='end_time',
            field=models.TimeField(default='01:11:47'),
        ),
        migrations.AlterField(
            model_name='book',
            name='start_time',
            field=models.TimeField(default='01:11:47'),
        ),
        migrations.AlterField(
            model_name='location',
            name='location_name',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
