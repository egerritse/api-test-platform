# Generated by Django 2.2a1 on 2019-03-05 14:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('testsession', '0058_auto_20190219_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenariocase',
            name='url',
            field=models.CharField(help_text="\n    URL pattern that will be compared\n    with the request and eventually matched.\n    Wildcards can be added, e.g. '/test/{uuid}/stop'\n    will match the URL '/test/c5429dcc-6955-4e22-9832-08d52205f633/stop'.\n    ", max_length=200),
        ),
        migrations.AlterField(
            model_name='vngendpoint',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(code='Invalid_name', message='The name cannot contain spaces', regex='^[^ ]*$')]),
        ),
        migrations.AlterField(
            model_name='vngendpoint',
            name='test_file',
            field=filer.fields.file.FilerFileField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.File'),
        ),
    ]
