# Generated by Django 4.0.3 on 2022-04-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmmain', '0011_remove_timing_friday_remove_timing_monday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='location',
            field=models.CharField(max_length=10000),
        ),
    ]
