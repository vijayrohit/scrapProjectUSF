# Generated by Django 3.1.5 on 2021-01-19 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0009_auto_20210119_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='userId',
        ),
    ]