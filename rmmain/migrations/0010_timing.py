# Generated by Django 4.0.3 on 2022-04-11 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rmmain', '0009_slotdelay_bookbefore'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.DateTimeField(blank=True)),
                ('tuesday', models.DateTimeField(blank=True)),
                ('wednesday', models.DateTimeField(blank=True)),
                ('thursday', models.DateTimeField(blank=True)),
                ('friday', models.DateTimeField(blank=True)),
                ('saturday', models.DateTimeField(blank=True)),
                ('sunday', models.DateTimeField(blank=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmmain.manager')),
                ('roomid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmmain.room')),
            ],
        ),
    ]
