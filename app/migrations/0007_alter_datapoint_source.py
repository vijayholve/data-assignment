# Generated by Django 5.0.6 on 2024-07-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_datapoint_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='source',
            field=models.CharField(max_length=2500),
        ),
    ]
