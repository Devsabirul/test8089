# Generated by Django 4.0.6 on 2022-07-29 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]