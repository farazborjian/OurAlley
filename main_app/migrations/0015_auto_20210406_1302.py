# Generated by Django 3.1.7 on 2021-04-06 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20210405_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='playdate',
            name='dogs',
            field=models.ManyToManyField(to='main_app.Dog'),
        ),
        migrations.DeleteModel(
            name='Invite',
        ),
    ]
