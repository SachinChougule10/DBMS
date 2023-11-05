# Generated by Django 3.2 on 2021-05-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20210502_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='end_time',
            field=models.TimeField(default='17:56:02'),
        ),
        migrations.AlterField(
            model_name='book',
            name='start_time',
            field=models.TimeField(default='17:56:02'),
        ),
    ]
