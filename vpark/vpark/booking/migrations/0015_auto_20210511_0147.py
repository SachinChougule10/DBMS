# Generated by Django 3.2 on 2021-05-10 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_auto_20210511_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.ImageField(null=True, upload_to='location_image/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='end_time',
            field=models.TimeField(default='01:47:43'),
        ),
        migrations.AlterField(
            model_name='book',
            name='start_time',
            field=models.TimeField(default='01:47:43'),
        ),
    ]
