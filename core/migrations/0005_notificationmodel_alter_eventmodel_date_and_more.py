# Generated by Django 4.2.10 on 2024-03-18 23:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_eventmodel_alter_videomodel_discription'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('live_link', models.CharField(blank=True, max_length=100)),
                ('discription', models.TextField(blank=True, max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='videomodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
