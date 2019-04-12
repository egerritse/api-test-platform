# Generated by Django 2.2a1 on 2019-04-11 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servervalidation', '0055_auto_20190410_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverrun',
            name='status',
            field=models.CharField(choices=[('starting', 'starting'), ('running', 'running'), ('shutting down', 'shutting down'), ('stopped', 'stopped'), ('Error deployment', 'error deploy'), ('Scheduled', 'Scheduled')], default='starting', max_length=20),
        ),
    ]
