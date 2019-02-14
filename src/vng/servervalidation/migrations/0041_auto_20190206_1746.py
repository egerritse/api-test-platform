# Generated by Django 2.2a1 on 2019-02-06 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servervalidation', '0040_auto_20190205_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='server_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servervalidation.ServerRun'),
        ),
        migrations.AlterField(
            model_name='postmantestresult',
            name='server_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servervalidation.ServerRun'),
        ),
    ]