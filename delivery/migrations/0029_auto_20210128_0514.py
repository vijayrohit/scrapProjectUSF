# Generated by Django 3.1.5 on 2021-01-28 05:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0028_auto_20210128_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datePosted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 5, 14, 24, 199524)),
        ),
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]