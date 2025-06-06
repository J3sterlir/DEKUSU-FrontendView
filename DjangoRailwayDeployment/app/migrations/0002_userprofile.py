# Generated by Django 5.1.7 on 2025-05-16 03:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('year_course', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('department', models.CharField(max_length=100)),
                ('subjects_taken', models.TextField()),
                ('skills', models.TextField()),
                ('support_areas', models.TextField()),
                ('tickets_raised', models.IntegerField(default=0)),
                ('ongoing_requests', models.CharField(max_length=200)),
                ('support_hours', models.CharField(max_length=100)),
                ('languages', models.CharField(max_length=200)),
                ('availability', models.CharField(max_length=100)),
                ('interests', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
