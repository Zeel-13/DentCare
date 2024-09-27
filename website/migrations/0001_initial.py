# Generated by Django 5.1.1 on 2024-09-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=20)),
                ('patient_name', models.CharField(max_length=15)),
                ('patient_email', models.EmailField(max_length=50)),
                ('doctor', models.CharField(max_length=15)),
                ('date', models.CharField(max_length=15)),
                ('time', models.CharField(max_length=15)),
            ],
        ),
    ]
