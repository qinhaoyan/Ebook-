# Generated by Django 2.0.1 on 2019-05-09 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebookapp', '0009_auto_20190509_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userhead',
            field=models.ImageField(upload_to='userhead'),
        ),
    ]
