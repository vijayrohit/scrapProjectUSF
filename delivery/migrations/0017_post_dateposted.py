# Generated by Django 3.1.5 on 2021-01-20 01:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0016_post_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='datePosted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 20, 1, 46, 2, 781155)),
        ),
    ]