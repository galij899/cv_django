# Generated by Django 3.1.4 on 2021-08-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cv', '0009_workexperience'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='time_en',
            field=models.CharField(default='-', max_length=100),
            preserve_default=False,
        ),
    ]
