# Generated by Django 2.2.14 on 2020-07-24 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_auto_20200724_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
    ]
