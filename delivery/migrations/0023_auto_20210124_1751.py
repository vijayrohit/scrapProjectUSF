# Generated by Django 3.1.5 on 2021-01-24 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0022_auto_20210121_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('HOME_APPLIANCES', 'Home Appliances'), ('SMARTPHONES', 'Smart Phones'), ('LAPTOPS', 'Laptops'), ('TABLETS', 'Tablets'), ('BOOKS', 'Books'), ('SPORTS/OUTDOOR', 'Sports and Outdoor'), ('CLOTHING', 'Clothing'), ('FURNITURE', 'Furniture'), ('OTHER', 'Other')], default='OTHER', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='datePosted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 24, 17, 51, 13, 413682)),
        ),
    ]
