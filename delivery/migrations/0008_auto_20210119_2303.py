# Generated by Django 3.1.5 on 2021-01-19 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0007_auto_20210119_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='userId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(default='../media/default-img.gif', upload_to='../media/ads/'),
        ),
    ]
