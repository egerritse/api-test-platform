# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-16 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servervalidation', '0018_auto_20190116_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverrun',
            name='client_id',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serverrun',
            name='secret',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='server_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servervalidation.ServerRun'),
        ),
    ]
