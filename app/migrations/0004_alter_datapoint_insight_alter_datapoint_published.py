# Generated by Django 5.0.6 on 2024-07-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='insight',
            field=models.TextField(default='No'),
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='published',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
