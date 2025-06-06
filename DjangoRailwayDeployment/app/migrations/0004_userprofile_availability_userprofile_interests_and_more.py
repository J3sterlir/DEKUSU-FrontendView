# Generated by Django 5.1.7 on 2025-05-16 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_userprofile_availability_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='availability',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='interests',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='languages',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
