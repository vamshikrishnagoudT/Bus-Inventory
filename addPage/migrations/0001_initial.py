# Generated by Django 5.1.5 on 2025-01-17 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_number', models.CharField(max_length=50, unique=True)),
                ('brand', models.CharField(max_length=100)),
                ('no_of_seats', models.PositiveIntegerField()),
                ('trip', models.CharField(max_length=200)),
                ('trip_duration', models.DurationField()),
                ('conductor', models.CharField(max_length=100)),
                ('driver', models.CharField(max_length=100)),
            ],
        ),
    ]
