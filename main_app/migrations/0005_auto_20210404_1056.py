# Generated by Django 3.1.7 on 2021-04-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_playdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playdate',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
