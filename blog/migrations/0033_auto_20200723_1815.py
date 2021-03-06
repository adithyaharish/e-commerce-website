# Generated by Django 2.2.14 on 2020-07-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20200723_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='appartment_address',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
