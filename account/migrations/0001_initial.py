# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-28 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(max_length=254, unique=True)),
                ('first_name', models.CharField(default='', max_length=254)),
                ('middle_name', models.CharField(blank=True, default='', max_length=254)),
                ('last_name', models.CharField(default='', max_length=254)),
                ('phone', models.CharField(default='', max_length=10, unique=True)),
                ('picture', models.CharField(blank=True, max_length=508, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
