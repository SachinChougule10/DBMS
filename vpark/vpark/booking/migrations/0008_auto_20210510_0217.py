# Generated by Django 3.2 on 2021-05-09 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0007_auto_20210507_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='end_time',
            field=models.TimeField(default='02:17:02'),
        ),
        migrations.AlterField(
            model_name='book',
            name='start_time',
            field=models.TimeField(default='02:17:02'),
        ),
    ]
