# Generated by Django 3.1.5 on 2021-01-17 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
