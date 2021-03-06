# Generated by Django 3.1.4 on 2021-04-30 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_auto_20210219_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='descr_en',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='name_en',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='descr_en',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='softskill',
            name='descr_en',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='softskill',
            name='name_en',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
