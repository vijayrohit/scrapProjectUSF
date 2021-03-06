# Generated by Django 3.1.5 on 2021-01-21 02:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0017_post_dateposted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='condition',
            field=models.CharField(choices=[('NEW', 'New'), ('LIKE NEW', 'Like New'), ('FAIR', 'Fair'), ('ACCEPTABLE', 'Acceptable'), ('POOR', 'Poor')], default='FAIR', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='datePosted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 2, 38, 42, 203190)),
        ),
    ]
