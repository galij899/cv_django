# Generated by Django 3.1.4 on 2021-08-07 15:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cv', '0008_remove_skill_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descr', models.CharField(max_length=300)),
                ('name_en', models.CharField(max_length=100)),
                ('descr_en', models.CharField(max_length=300)),
                ('time', models.CharField(max_length=100)),
            ],
        ),
    ]