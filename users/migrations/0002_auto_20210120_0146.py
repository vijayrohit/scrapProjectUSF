# Generated by Django 3.1.5 on 2021-01-20 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pro_pic',
            field=models.ImageField(default='../media/default.jpg', upload_to='profile_pics'),
        ),
    ]