# Generated by Django 3.1.5 on 2021-01-28 05:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0027_auto_20210128_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datePosted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 5, 3, 54, 917721)),
        ),
    ]