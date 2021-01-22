# Generated by Django 3.1.5 on 2021-01-18 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_post_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('HOME APPLIANCES', 'Home Appliances'), ('SMARTPHONES', 'Smart Phones'), ('LAPTOPS', 'Laptops'), ('TABLETS', 'Tablets'), ('BOOKS', 'Books'), ('SPORTS/OUTDOOR', 'Sports and Outdoor'), ('CLOTHING', 'Clothing'), ('FURNITURE', 'Furniture'), ('OTHER', 'Other')], default='OTHER', max_length=100),
        ),
    ]
