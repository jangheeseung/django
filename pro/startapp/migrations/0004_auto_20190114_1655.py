# Generated by Django 2.1.5 on 2019-01-14 07:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('startapp', '0003_auto_20190114_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 14, 7, 55, 6, 35683, tzinfo=utc)),
        ),
    ]