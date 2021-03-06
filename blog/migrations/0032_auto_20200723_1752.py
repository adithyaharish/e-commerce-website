# Generated by Django 2.2.14 on 2020-07-23 12:22

from django.db import migrations, models
import django_countries.fields
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20200723_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='start_date',
        ),
        migrations.AddField(
            model_name='order',
            name='appartment_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='order',
            name='street_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='zip',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
