# Generated by Django 5.0.4 on 2024-06-18 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_flightbooking_alter_contact_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('members', models.IntegerField()),
            ],
        ),
    ]
