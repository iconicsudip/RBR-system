# Generated by Django 4.0.3 on 2022-04-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmmain', '0004_roomtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
    ]
