# Generated by Django 3.1.7 on 2021-04-14 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_auto_20210404_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='loginapp\\static\\Images'),
        ),
    ]