# Generated by Django 4.0.3 on 2022-04-13 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rmmain', '0023_booking_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rmmain.manager'),
        ),
    ]
