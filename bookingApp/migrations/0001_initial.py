# Generated by Django 3.0.7 on 2020-07-13 08:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='default_img.jpg', null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookingApp.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookingApp.Customer')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookingApp.Service')),
            ],
            options={
                'unique_together': {('service', 'date', 'time')},
            },
        ),
    ]
