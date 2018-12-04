# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-22 14:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='serverrun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_endpoint', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='TestScenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('validation_file', models.FileField(upload_to='', verbose_name='/uploaded_files')),
            ],
        ),
        migrations.AddField(
            model_name='serverrun',
            name='test_scenario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='servervalidation.TestScenario'),
        ),
        migrations.AddField(
            model_name='serverrun',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
